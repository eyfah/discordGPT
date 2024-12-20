import ollama

from errlog import log, read_log
from tools import web_search, search_link, read_google_doc
from webscrape import parse

tools = [web_search(), search_link(), read_google_doc()]


async def get_response(memory, model, options, info):
    try:

        response = ollama.chat(
            model=model,
            messages=[{'role': 'user', 'content': memory}],
            options=options,
            tools=tools
        )

        model_output = response['message']['content']

        system = {
            "model": response.get("model"),
            "created": response.get("created_at"),
            "done": response.get("done"),
            "donereason": response.get("done_reason"),
            "time": response.get("total_duration"),
            "loadtime": response.get("load_duration"),
            "promptcount": response.get("prompt_eval_count"),
            "evalcount": response.get("eval_count"),
        }

        tool_calls = response.get('message', {}).get('tool_calls', [])
        if tool_calls:
            for tool_call in tool_calls:
                toolname = tool_call.get('function', {}).get('name')

                if toolname:
                    log(f"used tool: {toolname}")

                    if toolname == 'web_search':
                        query = tool_calls[0]['function']['arguments']['query']
                        url = f"https://www.google.com/search?q={query}"
                        parsed = parse(url=url)
                        memory += f"parsed data from search result: [{parsed}]"
                        model_output = await get_response(
                            memory=memory,
                            info=info,
                            model=model,
                            options=options)
                        print(f'{model}: "{model_output}"')
                        memory += f'searched: [{query}]\n\n{model_output}'
                        return f'searched: {query}\n\n{model_output}'


                    elif toolname == 'read_google_doc':
                        from googleclient import googledoc
                        doc_id = tool_calls[0]['function']['arguments']['doc_id']
                        log(f"read: {doc_id}")
                        content = googledoc(doc_id)
                        if content:
                            print(content)
                            memory += f"content:\n\n{content}"
                            model_output = await get_response(
                                memory=memory,
                                info=info,
                                model=model,
                                options=options)
                            print(f'{model}: "{model_output}"')
                            return model_output
                        else:
                            print("Couldn't read document")
                            return "Couldn't read document"

                    elif toolname == 'edit_google_doc':
                        from googleclient import googledoc
                        doc_id = tool_calls[0]['function']['arguments']['doc_id']
                        log(f"edit: {doc_id}")
                        edit_request = tool_calls[0]['function']['arguments']['edit_request']
                        print(f"{doc_id}\n\n")
                        print(edit_request)


                    elif toolname == 'search_link':
                        urls = tool_calls[0]['function']['arguments']['url']
                        for url in urls:
                            log(f"search: {url}")
                            content = parse(url)
                            memory += f"\n\nparsed data from {url}:\n\n{content}"
                            continue
                        model_output = await get_response(
                            memory=memory,
                            info=info,
                            model=model,
                            options=options)
                        print(f'{model}: "{model_output}"')
                        memory += f"visited link(s): {urls}\n\n{model_output}"
                        return f"visited link: {urls}\n\n{model_output}"


        print(f'{model}: "{model_output}"')
        return model_output

    except TypeError as te:
        error = f"TypeError: {te}"
        log(error)
        return error
    except KeyError as ke:
        error = f"KeyError: {ke}"
        log(error)
        return error
    except Exception as e:
        error = f"UnexpectedError: {e}"
        log(error)
        return error

from helpcommands import helpcommands
from llama import get_models, pull_models, delete_models
from responses import get_response
from errlog import log, read_log, end_log

default_context = "You are a Discord AI chatbot/assistant."
default_rules = "Keep chats short and easy to read, always respond in English."
default_model = "qwen2.5"
default_vision_model = "llava"
default_temp = 0.8
default_clim = 2000
default_mlim = 20000

context = default_context
rules = default_rules
model = default_model
vision_model = default_vision_model
temp = float(default_temp)
clim = int(default_clim)
mlim = default_mlim

info = {
    "context": context,
    "rules": rules,
    "model": model,
    "vmodel": vision_model,
    "models": str(get_models()),
    "temp": temp,
    "clim": clim,
    "mlim": mlim
}

options = {
    'num_predict': clim,
    'temperature': int(info["temp"]),

}

memory = str(info)


commands = {
    "!clear all": lambda: clear_all(),
    "!clear context": lambda: clear_context(),
    "!clear log": lambda: clear_log(),
    "!clear memory": lambda: clear_memory(),
    "!clear rules": lambda: clear_rules(),
    "!clear temp": lambda: clear_temp(),
    "!help": lambda: show_help(),
    "!reset all": lambda: reset_all(),
    "!reset clim": lambda: reset_clim(),
    "!reset context": lambda: reset_context(),
    "!reset memory": lambda: reset_memory(),
    "!reset mlim": lambda: reset_mlim(),
    "!reset rules": lambda: reset_rules(),
    "!reset temp": lambda: reset_temp(),
    "!show all": lambda: show_all(),
    "!show clim": lambda: show_clim(),
    "!show context": lambda: show_context(),
    "!show list": lambda: show_list(),
    "!show log": lambda: show_log(),
    "!show memory": lambda: show_memory(),
    "!show mlim": lambda: show_mlim(),
    "!show model": lambda: show_model(),
    "!show rules": lambda: show_rules(),
    "!show temp": lambda: show_temp(),
}



def reset_all():
    global memory, info
    info = {
        "context": default_context,
        "rules": default_rules,
        "model": default_model,
        "vision_model": default_vision_model,
        "models": str(get_models()),
        "temp": default_temp,
        "clim": default_clim,
        "mlim": default_mlim
    }
    memory = str(info)
    log("user command: !reset all")
    return memory


def reset_context():
    global info
    info["context"] = default_context
    log("user command: !reset context")
    return f"Current context: {info["context"]}"


def reset_temp():
    global info
    info["temp"] = default_temp
    log("user command: !reset temp")
    return f"Current temp: {info["temp"]}"


def reset_rules():
    global info
    info["rules"] = default_rules
    log("user command: !reset rules")
    return f"Current rules: {info["rules"]}"


def reset_memory():
    global memory, info
    memory = str(info)
    log("user command: !reset memory")
    return f"Conversation history: {memory}"


def reset_clim():
    global info
    info["clim"] = default_clim
    log("user command: !reset clim")
    return f"Character limit: {info["clim"]}"

def reset_mlim():
    global info
    info["mlim"] = default_mlim
    log("user command: !reset mlim")
    return f"Memory limit: {info["mlim"]}"


def clear_all():
    global memory, info
    memory = ""
    info = {
        "context": "",
        "rules": "",
        "model": "",
        "models": "",
        "temp": 0.0,
        "clim": 2000,
        "mlim": 20000
    }
    log("user command: !clear all")
    return info


def clear_context():
    global info
    info["context"] = ""
    log("user command: !clear context")
    return f"Current context: {info["context"]}"


def clear_temp():
    global info
    info["temp"] = 0
    log("user command: !temp")
    return f"Current temp: {info["temp"]}"


def clear_rules():
    global info
    info["rules"] = ""
    log("user command: !rules")
    return f"Current rules: {info["rules"]}"


def clear_memory():
    global memory
    memory = ""
    log("user command: !memory")
    return f"Conversation history: {memory}"

def clear_log():
    return end_log()




def show_all():
    log("user command: !show all")
    return str(info)


def show_context():
    log("user command: !show context")
    return f"Context: {info["context"]}"


def show_model():
    log("user command: !show model")
    return f"Current model: {info["model"]}"


def show_list():
    log("user command: !show list")
    return f"Available models: {str(get_models())}"


def show_temp():
    log("user command: !show temp")
    return f"Temp: {info["temp"]}"


def show_clim():
    log("user command: !show clim")
    return f"Character limit: {info["clim"]}"


def show_rules():
    log("user command: !show rules")
    return f"Rules: {info["rules"]}"


def show_memory():
    log("user command: !show memory")
    return f"Conversation history:\n\n{memory}"

def show_mlim():
    log("user command: !show mlim")
    return f"Memory limit: {len(memory)}/{info["mlim"]}"

def show_log():
    log("user command: !show log")
    return read_log()


def show_help():
    log("user command: !help")
    return helpcommands


async def prompt_logic(prompt):
    global model, rules, context, temp, clim, memory, mlim, info
    memory += f"\n\n{prompt}"
    try:
        if '!model' in prompt:
            modelprompt = prompt.split(" ")
            new_model = modelprompt[1]
            if new_model in str(get_models()):
                model = new_model
                info["model"] = model
                log(f"model set to: {info["model"]}")
                return f"Current model: {info["model"]}"
            else:
                return f"Please provide a valid model!: {str(get_models())}"

        if '!vmodel' in prompt:
            modelprompt = prompt.split(" ")
            new_model = modelprompt[1]
            if new_model in str(get_models()):
                vmodel = new_model
                info["vmodel"] = vmodel
                log(f"vision model set to: {info["vmodel"]}")
                return f"Current vision model: {info["vmodel"]}"
            else:
                return f"Please provide a valid model!: {str(get_models())}"

        elif '!rules' in prompt:
            ruleprompt = prompt.split(" ")
            rules = " ".join(ruleprompt[1:])
            info["rules"] = rules
            log(f"user set new rules")
            return f"Current rules: {rules}"

        elif '!context' in prompt:
            contextprompt = prompt.split(" ")
            context = " ".join(contextprompt[1:])
            info["context"] = context
            log(f"user set new context")
            return f"Current context: {context}"

        elif '!temp' in prompt:
            tempprompt = prompt.split(" ")
            temp = float(tempprompt[-1])
            info["temp"] = temp
            log(f"temp set to: {info["temp"]}")
            return f"Current temp: {temp}"

        elif '!clim' in prompt:
            climprompt = prompt.split(" ")
            clim = int(climprompt[-1])
            info["clim"] = clim
            log(f"clim set to: {info["clim"]}")
            return f"Character limit: {clim}"

        elif '!mlim' in prompt:
            mlimprompt = prompt.split(" ")
            mlim = int(mlimprompt[-1])
            info["mlim"] = mlim
            log(f"mlim set to: {info["mlim"]}")
            return f"Memory limit: {mlim}"



        elif prompt == '!help':
            log("user command: !help")
            return helpcommands

        elif '!pull' in prompt:
            pullprompt = prompt.split(" ")
            pull = pullprompt[1]
            pulled = pull_models(pullmodel=pull)
            log(f"user pulled model: {pull}, Status: {pulled}")
            return f"Pulled Model: {pull}, Status: {pulled}"

        elif '!delete' in prompt:
            deleteprompt = prompt.split(" ")
            delete = deleteprompt[1]
            deleted = delete_models(deletemodel=delete)
            log(f"user deleted model: {delete}, Status: {deleted}")
            return f"Deleted Model: {delete}, Status: {deleted}"




        if prompt in commands:
            return commands[prompt]()


        elif prompt.startswith("!") and any(k not in prompt for k in ["model", "rules", "context", "temp"]):
            return "Invalid command! type !help for more options."

        elif prompt == "":
            return

        elif len(memory) >= info["mlim"]:
            reset_memory()
            return "Memory Cleared!"

        else:
            response = await get_response(memory=memory, options=options, model=model, info=info)

            memory += f"\n\n{response}"
            return response

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

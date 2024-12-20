def web_search():
    return {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "search the web for real-time data",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "search prompt",
                    },
                },
                "required": ["query"],
            },
        },
    }


def search_link():
    return {
        "type": "function",
        "function": {
            "name": "search_link",
            "description": "goes to a link and parses the text content",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "paste url to search (as a list if multiple)",
                    },
                },
                "required": ["url"],
            },
        },
    }


def read_google_doc():
    return {
        "type": "function",
        "function": {
            "name": "read_google_doc",
            "description": "get the google doc ID",
            "parameters": {
                "type": "object",
                "properties": {
                    "doc_id": {
                        "type": "string",
                        "description": "google doc ID",
                    },
                },
                "required": ["doc_id"],
            },
        },
    }

def edit_google_doc():
    return {
        "type": "function",
        "function": {
            "name": "edit_google_doc",
            "description": "make an edit request for the google docs api",
            "parameters": {
                "type": "object",
                "properties": {
                    "doc_id": {
                        "type": "string",
                        "description": "google doc ID",
                    },
                    "edit_request": {
                        "type": "json",
                        "description": "edit request in json format",
                    },
                },
                "required": ["doc_id", "edit_request"]
            },
        },
    }


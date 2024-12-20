import json

import ollama


def get_models():
    getmodels = str(ollama.list())
    fixed = getmodels.replace("'", '"')
    parsed = json.loads(fixed)
    models = [model['name'] for model in parsed['models']]
    return models


def pull_models(pullmodel):
    try:
        pull = ollama.pull(f'{pullmodel}')
        print(pull)
        return pull
    except Exception as e:
        print(e)
        return f"unable to pull {pullmodel}. reason: {e}"


def delete_models(deletemodel):
    try:
        delete = ollama.delete(f'{deletemodel}')
        print(delete)
        return delete
    except Exception as e:
        print(e)
        return f"unable to delete model {deletemodel}. reason: {e}"

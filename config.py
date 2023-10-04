import json

def get_config():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
        return config
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
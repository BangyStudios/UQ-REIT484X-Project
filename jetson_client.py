import config as conf
import os
import socket
import json
import shutil
import pickle

def send_file(s, path_file):
    with open(path_file, "rb") as f:
        while (chunk := f.read(1024)):
            s.sendall(chunk)

def send_dir_zip(s, path_dir, path_zip):
    shutil.make_archive(path_zip, "zip", path_dir)
    send_file(s, f"{path_zip}.zip")

def send_command(command, config):
    config_pickle = pickle.dumps(config)
    jetson_host = config.get("jetson").get("host")
    jetson_port = config.get("jetson").get("port")
    path_state = config.get("path").get("state")
    path_recording_generated = config.get("path").get("recording_dataset")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((jetson_host, jetson_port))

        s.sendall(command.encode())
        s.send(config_pickle)
        send_file(s, "config.py")

        if command == "predict":
            send_file(s, path_state)
            send_dir_zip(s, path_recording_generated, "latest")
            send_file(s, "dataset.py")
            send_file(s, "predict.py")

            data = b""
            while True:
                chunk = s.recv(1024)
                if not chunk:
                    break
                data += chunk
            predictions = json.loads(data.decode())
            return predictions

if __name__ == "__main__":
    config = conf.get_config()
    send_command("predict", config)

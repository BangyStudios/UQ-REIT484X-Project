import socket
import json
import os
import shutil
import pickle
import importlib

def receive_file(conn, file_path):
    with open(file_path, "wb") as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

def run_script(script_path):
    os.system(f"python3 {script_path}")

def reload_modules():
    importlib.reload(dataset)
    importlib.reload(predict)

HOST = "127.0.0.1"
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    while True:  # Loop to accept multiple clients
        conn, addr = s.accept()
        with conn:
            command = conn.recv(1024).decode()

            config_pickle = conn.recv(1024)
            config = pickle.loads(config_pickle)
            receive_file(conn, "./config.py")

            path_state = config.get("path").get("state")
            path_recording = config.get("path").get("recording")
            path_recording_generated = config.get("path").get("recording_generated")
            file_recording_generated = os.path.join(path_recording, "generated.zip")

            if command == "predict":
                receive_file(conn, path_state)
                receive_file(conn, file_recording_generated)
                receive_file(conn, "./dataset.py")
                receive_file(conn, "./predict.py")
                
                shutil.unpack_archive(file_recording_generated, path_recording_generated)

                import dataset
                import predict
                
                reload_modules()  # Reload in case the files were updated

                ds = dataset.Dataset()
                dl = ds.get_dl_predict(path_recording, size_batch=5)

                predictor = predict.Predict()
                probabilities_dict = predictor.predict(dl)

                conn.sendall(json.dumps(probabilities_dict).encode())

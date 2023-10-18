import config as conf
import preprocessor
import dataset
import predict

import os
import shutil
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

config = conf.get_config()
generator = preprocessor.Generator()
ds = dataset.Dataset()
predictor = predict.Predict()

# Flask configuration
host = config.get("jetson").get("api_host")
port = config.get("jetson").get("api_port")
debug = config.get("jetson").get("api_debug")

@app.route("/api/jetson/receive", methods=["post"])
def jetson_receive():
    received_file = request.files["file"]
    received_path = request.form.get("path", "")
    if not os.path.exists(received_path):
        os.makedirs(received_path)
    if (received_file.filename != ""):
        path_file = os.path.join(received_path, received_file.filename)
        received_file.save(path_file)
        return f"File {received_file.filename} uploaded successfully.", 200
    else:
        return "No file selected", 400

@app.route("/api/jetson/init_folder", methods=["GET"])
def init_folder():
    path_folder = request.args.get("path", default="")
    if not os.path.exists(path_folder):
        os.mkdir(path_folder)
    return jsonify({"message": f"Folder created: {path_folder}"}), 200
        
@app.route("/api/jetson/clear_folder", methods=["GET"])
def clear_folder():
    path_folder = request.args.get("path", default="")
    for input_file in os.listdir(path_folder):
        path_file = os.path.join(path_folder, input_file)
        try:
            if os.path.isfile(path_file):
                os.unlink(path_file)
            elif os.path.isdir(path_file):
                shutil.rmtree(path_file)
        except Exception as e:
            print(f'Failed to delete {path_file}. Reason: {e}')
    return jsonify({"message": f"Folder cleared: {path_folder}"}), 200

@app.route("/api/jetson/preprocess", methods=["GET"])
def jetson_preprocess():
    # Load configuration
    path_recording = config.get("path").get("recording")
    path_recording_latest = os.path.join(path_recording, "latest.wav")
    path_recording_latest_generated = os.path.join(path_recording, "latest/")
    
    length_segment = config.get("preprocessor").get("length_segment")
    
    rpi_api_host = config.get("rpi").get("host")
    rpi_api_address = f"http://{rpi_api_host}"
    
    generator.generate_features_to_images(path_recording_latest, path_recording_latest_generated, length_segment)
    
    for filename in os.listdir(path_recording_latest_generated):
        path_file = os.path.join(path_recording_latest_generated, filename)
        if os.path.isfile(path_file):
            with open(path_file, "rb") as file:
                files = {"file": file}
                data = {"path": path_recording_latest_generated}
                response = requests.post(f"{rpi_api_address}/api/rpi/receive", files=files, data=data)
    
    return "Preprocessed...", 200
    
"""Warning: This does not work"""
@app.route("/api/jetson/predict", methods=["GET"])
def jetson_predict():
    # Load configuration
    path_recording = config.get("path").get("recording")
    size_batch = config.get("dataset").get("size_batch")

    # Generate dataloaders
    dl = ds.get_dl_predict(path_recording, size_batch)
    
    # Run prediction
    probabilities_dict = predictor.predict(dl)
    
    print(probabilities_dict)
    
    return jsonify(probabilities_dict), 200

if (__name__ == "__main__"):
    app.run(host=host, port=port, debug=debug) # host="0.0.0.0"
from flask import Flask, jsonify
 
app = Flask(__name__)
VERSION = "1"
 
@app.get("/")
def index():
    return jsonify(message="hello from python", version=VERSION)
 
@app.get("/healthz")
def healthz():
    return jsonify(status="ok")


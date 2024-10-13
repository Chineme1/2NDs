from flask import Flask
import requests

app = Flask(__name__)

@app.route("/webhookcallback", methods=["GET"])

def hook(data):
    #returns json object
    return data

if __name__=="__main__":
    app.run()
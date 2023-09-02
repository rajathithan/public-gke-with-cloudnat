from flask import Flask
import requests
import config 

app = Flask(__name__)

@app.route("/getmyip")
def getmyip():
    url = "https://ipinfo.io/ip"
    response = requests.get(url)
    return response.content

@app.route("/")
def welcome():
    return "GKE Egress static ip with Cloud NAT - Testing << use URI /getmyip to verify if the egress connections are using cloud NAT's Ip Address  >>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT,debug=config.DEBUG_MODE)
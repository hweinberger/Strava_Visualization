from flask import Flask
app = Flask(__name__)

from stravalib import Client
client = Client(access_token=0a50886d4490182dd5578de192462b97f5de5a8d)

@app.route("/")
def hello():
    return client.get_athlete()
if __name__ == "__main__":
    app.run()

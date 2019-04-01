import os
from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello World ... again!"


# LOCAL
#if __name__ == "__main__":
    #app.run(host=os.getenv("IP", "127.0.0.1"),
            #port=os.getenv("PORT", "5000"),
            #debug=True)

# HEROKU
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)

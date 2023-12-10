from flask import Flask
from time import sleep

app = Flask(__name__)

@app.route("/")
def main():
    sleep(20)
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)
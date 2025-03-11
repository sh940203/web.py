from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello 張書浩"

if __name__ == "__main__":
    app.run()

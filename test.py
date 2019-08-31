from flask import Flask
print("Hello World!")
print(__name__)
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
if __name__=="main":
	print("Hello main!")
	app = Flask(__name__)

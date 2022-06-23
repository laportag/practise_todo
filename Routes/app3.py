from flask import Flask, redirect, url_for

app = flask(__name__)

@app.route("/")
@app.route("/home")

def home():
    return redirect("url_for("redirect"))

@app.route("/redirect")

def redirect():
    return "youve been redirected here from home"

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0', port=5000)
from flask import Flask

app = flask(__name__)

@app.route("/")
@app.route("/home/<int:number>")

def home(number):
    output = number * 5
    return str(output)


if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0', port=5000)
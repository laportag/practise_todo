from flask import Flask

app = flask(__name__)

@app.route("/")
@app.route("/home/"), methods=['GET', 'POST']

def home():
    if  request.method == 'POST':
        return 'This is a post method'
    else:
        return 'this is a get request'


if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0', port=5000)
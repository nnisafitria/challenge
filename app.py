from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def portofolio():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)

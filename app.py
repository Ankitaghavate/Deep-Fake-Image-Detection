from flask import Flask, render_template, jsonify
#import mysql.connector

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def Home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port=9090)

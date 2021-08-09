from flask import Flask, url_for, redirect, request, render_template
import pyshorteners

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return render_template('index.html')
    except:
        return redirect('/error')

@app.route('/error')
def error():
    return render_template('error.html')
from flask import Flask,render_template,redirect,url_for
from whatsapp_chat_analyse import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')


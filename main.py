from flask import Flask, url_for, redirect, request, make_response, render_template, session
import os

app = Flask('Prva flask aplikacija')

app.secret_key = '_de5jRRR83x'

@app.before_request
def before_request_func():
    if request.path == '/login':
        return
    if session.get('username') is None:
        return redirect(url_for('login'))

#1.zad
@app.get('/')
def home():
    response = render_template('index.html')
    return response, 200

@app.get('/login')
def login():
    response = render_template('login.html')
    return response, 200

#2.-4.zad
@app.get('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login'))


@app.post('/login')
def log1n():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == 'PURS' and password == '1234':
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)
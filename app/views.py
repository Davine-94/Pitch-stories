from flask import render_template
from app import app

@app.route('/')
def home():
    
    title = 'Pitch Stories'
    return render_template('index.html', title=title)
from flask import render_template
from app import app
from .forms import RegistrationForm, LoginForm

app.config['SECRET_KEY'] = '5617b591905a7c411a5c7379e4092bc9'

posts = [
    {
        'author': 'Davine Phylis',
        'title': 'Film Pitch',
        'content':'I have a degree in English and a minor in Film Studies, from the UPpen University.I work as a freelance copywriter for local businesses and nonprofits, and a movie critic for the Huffington Post: actually, my recent review of The Favorite got 52 thousand shares on Twitter. Maybe you’ve come across it? Anyways, if you know someone in need of unique, buzz-worthy content, feel free to send them my way',
        'date_posted':'May 7, 2022'
    },
    {
        'author': 'Paul Durr',
        'title': 'Interview Pitch',
        'content':'As a marketing director at KPMG, I coordinate all stages of creating audiovisual marketing materials: from the concept, to execution, to promotion. At the beginning of last year, I got a list of 15 campaigns and a set budget for all of them. Together with our Technology Department, we came up with a strategy of cross-departmental communications calibrating the tech solutions with all team’s talents to cut redundant costs and increase efficiency. Under my leadership, we completed all 15 projects on time and over 10% below budget. By the end of the year, sales from all campaigns contributed to increasing revenue by 48%.',
        'date_posted':'April 18, 2022'  
    },
    {
        'author': 'Nalah Mumbi',
        'title':'School Pitch',
        'content':'Our local high school football team has not won a game in four weeks; the coach is implementing a new strategy that involves a pre-game workout. The players are discouraged. However, the plan is go to our local high school over a three-week period to see what other players are implementing and why it works for them.',
        'date_posted': 'February 14, 2022' 
    }  
    ]

@app.route('/')
def home():
    title = 'Pitch Stories'
    return render_template('index.html', title=title, posts=posts)

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
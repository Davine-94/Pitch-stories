from flask import render_template, request, Blueprint
from app.models import Post 

main = Blueprint('main',__name__)

@main.route('/')
def home():
    page = request.args.get('page', 1, type =int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    title = 'Pitch Stories'
    return render_template('index.html', title=title, posts=posts)




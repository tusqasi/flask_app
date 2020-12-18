from flask import Flask, render_template, url_for   
from form import RegForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dd1435ed1e2298ddda0594ac7d2699a0'

posts = [
        {
            'title': "First post",
            'author': "tusqasi",
            'date_posted': "December, 12th, 2020",
            'content': "Is this working"
        },

        {
            'title': "Second post",
            'author': "tusqasi",
            'date_posted': "December, 14th, 2020",
            'content': "hi There"
        },
        {
            'title': "Third post",
            'author': "tusqasi",
            'date_posted': "December, 15th, 2020",
            'content': "you still here"
        }
    ]

@app.route("/")
@app.route("/home/")
def home(var="hi", posts=posts):
    return render_template('home.html',title=var, posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

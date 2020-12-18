from flask import Flask, render_template

app = Flask(__name__)

posts = [
        {
            'title': "First post",
            'author': "tusqasi",
            'date_posted': "December, 12th, 2020"
        },

        {
            'title': "Second post",
            'author': "tusqasi",
            'date_posted': "December, 14th, 2020"
        },
        {
            'title': "Third post",
            'author': "tusqasi",
            'date_posted': "December, 15th, 2020"
        }
    ]

@app.route("/")
@app.route("/home/")
def home(var="hi", posts=posts):
    return render_template('home.html',title=var, posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

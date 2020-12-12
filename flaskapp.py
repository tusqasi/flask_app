from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home/<var>")
def home(var="hi"):
    return render_template('home.html',title=var)

@app.route("/about")
def about():
    return render_template('about.html',)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template

#creating a Flask instance
app = Flask(__name__, template_folder='templates')

#create a route (decorator)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/experience')
def experience():
    return render_template("experience.html")

if (__name__) == '__main__':
    app.run(debug=True)
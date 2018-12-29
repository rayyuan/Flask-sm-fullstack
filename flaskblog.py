from flask import Flask, render_template
app = Flask(__name__)

posts=[
    {
        'name':'Ray',
        'content':'test post 1 please work',
        'date':'12/28/2018'
    },
    {
        'name':'Kevin',
        'content':'test post 2 this is the second post.',
        'date':'12/29/2018'
    },
    {
        'name':'Kevin',
        'content':'test post 3 this is the second post.',
        'date':'12/31/2018'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts,title='TESTBITCH')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

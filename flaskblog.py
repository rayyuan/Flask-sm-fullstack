from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/temp")
def hello():
    return "<h1>hellaefao</h1>"

@app.route("/about")
def about():
    return "<h1>aboutpage</h1>"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

all_scores = open("TextFiles/Scores.txt").read().split()
name = all_scores[0]
score = all_scores[1]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', score=score, name=name)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)

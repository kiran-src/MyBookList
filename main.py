from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'GET':
        return render_template("add.html")
    all_books.append({'name': request.form['name'], 'author': request.form['author'], 'rating': request.form['rating']})
    print(all_books)
    return render_template("index.html")




if __name__ == "__main__":

    app.run(debug=True)


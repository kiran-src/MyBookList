from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)


db.create_all()



@app.route('/')
def home():
    all_books = []
    for i in db.session.query(Book).all():
        all_books.append({'title': i.title, 'author': i.author, 'rating': i.rating})
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'GET':
        return render_template("add.html")
    new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/edit/<title>-<rating>", methods=['POST', 'GET'])
def edit(title, rating):
    print("title")
    if request.method == 'POST':
        Book.query.filter_by(title=title).first().rating = request.form['rating']
        print(title)
        db.session.commit()
        print(rating)
        return redirect(url_for('home'))
    return render_template("edit.html", title=title, rating=rating)


if __name__ == "__main__":

    app.run(debug=True)


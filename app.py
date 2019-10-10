import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'TrainerMate'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00t123@myfirstcluster-rieqe.mongodb.net/TrainerMate?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/categories')
def categories():
    return render_template("base.html", categories=mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP','0.0.0.0'),
            port=int(os.environ.get('PORT','8000')),
            debug=True)
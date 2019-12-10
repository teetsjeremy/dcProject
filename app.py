import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'dcProject'
app.config["MONGO_URI"] = 'mongodb+srv://Teets:Lexi1013@myfirstcluster-oq2u3.mongodb.net/dcProject?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("main.html", tasks=mongo.db.E9Xissues.find())
    
@app.route('/contact')
def contact():
    return render_template("contact.html")
    
@app.route('/add_task')
def add_task():
    return render_template("addtask.html")
    
@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.dbE9Xissues
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))    

@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task =  mongo.db.E9Xissues.find_one({"_id": ObjectId(task_id)})
    all_categories =  mongo.db.E9Xissues.find()
    return render_template('edit.html', task=the_task, categories=all_categories)    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
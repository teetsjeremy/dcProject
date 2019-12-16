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
    
@app.route('/diagnostic')
def diagnostic():
    return render_template("main.html", tasks=mongo.db.E9Xissues.find(diagnostic))
    
@app.route('/tab')
def tab():
    return render_template("tab.html")
    
@app.route('/contact')
def contact():
    return render_template("contact.html")
    
@app.route('/shop')
def shop():
    return render_template("shop.html")
    
@app.route('/add_task')
def add_task():
    return render_template("addtask.html")
    
    
@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.E9Xissues
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))    

@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task =  mongo.db.E9Xissues.find_one({"topic": ObjectId(task_id)})
    all_categories =  mongo.db.E9Xissues.find({"topic": ObjectId(task_id)})
    return render_template('edit.html', task=the_task, categories=all_categories)
    
@app.route('/update_task/<task_id>', methods=["POST"])
def update_task(task_id):
    tasks = mongo.db.E9Xissues
    tasks.update( {'_id': ObjectId(task_id)},
        {
            'topic':request.form.get('topic'),
            'title':request.form.get('title'),
            'desc_of_problem': request.form.get('desc_of_problem'),
            'work_performed': request.form.get('work_performed'),
            'fixed':request.form.get('fixed'),
            'need.help':request.form.get('need.help')
        })
    return redirect(url_for('get_tasks'))
    
@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db. E9Xissues.remove({"_id": ObjectId(task_id)})
    return redirect(url_for('get_tasks'))    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
import os
from flask import Flask, render_template, redirect, request, url_for



app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'dcProject'
app.config["MONGO_URI"] = 'mongodb+srv://Teets:Lexi1013@myfirstcluster-oq2u3.mongodb.net/dcProject?retryWrites=true&w=majority'


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
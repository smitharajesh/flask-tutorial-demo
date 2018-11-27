"""
Flask app to host my simple bio
Habit: Develop -> test -> commit -> deploy -> test

"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    "The search page"
    return render_template('index.html')

#----START OF SCRIPT
if __name__=='__main__':
    app.run(host='0.0.0.0',port=6464)

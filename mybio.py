"""
Flask app to host my simple bio
Habit: Develop -> test -> commit -> deploy -> test
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index_page():
    "The search page"
    return "Hello"

#----START OF SCRIPT
if __name__=='__main__':
    app.run(host='0.0.0.0',port=6464)

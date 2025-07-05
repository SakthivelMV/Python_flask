from flask import Flask, request, redirect, url_for, render_template, jsonify
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI=os.getenv('MONGO_URI')
app = Flask(__name__)

# Replace this with your MongoDB Atlas connection string
client = pymongo.MongoClient(MONGO_URI)
db = client.email
collection = db['test_email']

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = {
            'name': request.form['name'],
            'email': request.form['email']
        }
        collection.insert_one(data)
        return redirect(url_for('success'))
    except Exception as e:
        return render_template('form.html', error=str(e))

@app.route('/success')
def success():
    return "<h2>Data submitted successfully</h2>"

if __name__ == '__main__':
    app.run(debug=True)

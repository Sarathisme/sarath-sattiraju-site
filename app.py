from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongodb://admin:tablet50@ds157204.mlab.com:57204/contacts')

db = client['contacts']
messages = db.messages

result = False

@app.route('/', methods=['POST', 'GET'])
def homepage():
    return render_template('index.html', result=result)

@app.route('/send_data', methods=['POST'])
def send_data():
    if request.method == 'POST':
        results = request.form
        data = {
            'email':results['email'],
            'message':results['message'],
            'time':str(datetime.now())
        }
        
        global result
        try:
            messages.insert_one(data)
            result = True
            print('Here!')
            return redirect(url_for('homepage'))
        except Exception as e:
            print(e)
            result = None
            return redirect(url_for('homepage'))


if __name__ == "__main__":
    app.run(debug=False)
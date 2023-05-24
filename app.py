from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.rgsaqvn.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/music", methods=["GET"])
def mars_get():
    music_data = list(db.music.find({},{'_id':False}))
    return jsonify({'result':music_data})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

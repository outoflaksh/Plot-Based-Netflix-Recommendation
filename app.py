from flask import Flask, request, jsonify
from main import recommendations
from datasets import DATASET_FULL

app = Flask(__name__)

@app.route("/recommend", methods = ["POST"])
def recommend():
    title = request.get_json()['title']
    recom = recommendations(title)
    
    return jsonify({'message' : recom})
    

if __name__ == "__main__":
    app.run()
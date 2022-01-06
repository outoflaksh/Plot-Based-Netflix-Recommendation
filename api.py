from flask import Flask, request, jsonify
from main import recommendations
from datasets import DATASET_FULL

app = Flask(__name__)


@app.route("/recommend", methods=["GET"])
def get_recommendation():
    title = request.args.get("title")
    recom = recommendations(title)

    return jsonify({'data': recom, "status": 200})


@app.route("/titles", methods=["GET"])
def read_all_movies():
    movies = list(DATASET_FULL['title'])
    return jsonify({"status": 200, "data": movies})


if __name__ == "__main__":
    app.run(debug=True)

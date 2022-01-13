from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from main import recommendations
from datasets import DATASET_FULL

app = Flask(__name__)
CORS(app)

@app.route("/recommend", methods=["GET"])
@cross_origin()
def get_recommendation():
    title: str = request.args.get("title")
    recom = recommendations(title.title())
    if not recom:
        return jsonify({"status": 404, "data": recom }), 404

    return jsonify({'data': recom, "status": 200})


@app.route("/titles", methods=["GET"])
@cross_origin()
def read_all_movies():
    movies = list(DATASET_FULL['title'])
    return jsonify({"status": 200, "data": movies}), 200


if __name__ == "__main__":
    app.run(debug=True)

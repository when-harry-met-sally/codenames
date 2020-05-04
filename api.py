from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from solver import solve, getAssociatedWords
app = Flask(__name__)
CORS(app)
def handleArgs(words):
    dictionary = {}
    for word in words:
        dictionary[word] = getAssociatedWords(word)
    return dictionary

@app.route("/api", methods=['POST'])
def api():
    data = request.get_json()
    words = data["words"]
    dictionary = handleArgs(words)
    solution = solve(dictionary)
    return jsonify(solution)

@app.route("/", methods=['GET'])
def main():
    return "Post to /api"

if __name__ == '__main__':
    app.run()


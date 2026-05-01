import os
from flask import Flask, make_response, request, jsonify, send_file, send_from_directory

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = "payload"
FLAG = "TillerCTF{blu9_sh1rt_k1d}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        key = request.form.get("server")
        if key == SECRET_KEY:
            return jsonify({"key": FLAG})
        return jsonify({"error": "Wrong key"}), 403

    if request.method == "GET":
        user_agent = request.headers.get("User-Agent", "")
        if "curl" in user_agent.lower():
            return "Try using -d or --data flag 😉", 200

    response = make_response(send_file(os.path.join(BASE_DIR, "mask.html")))
    response.set_cookie("hint", "The key is --server-- and the value is --payload--")
    return response

@app.route('/<path:filename>')
def serve_static(filename):
    if filename.startswith("bildet/"):
        return send_from_directory(BASE_DIR, filename)
    return "Nothing here ", 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
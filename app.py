from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando 🔥"

@app.route("/like", methods=["GET"])
def like():
    uid = request.args.get("uid")

    if not uid:
        return jsonify({"error": "UID requerido"}), 400

    return jsonify({
        "status": "success",
        "uid": uid,
        "message": "Like simulado enviado"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
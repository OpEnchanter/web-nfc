from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

ids = []

@app.route("/")
def root():
    return render_template("/index.html")

@app.route("/api/validatetag", methods=['POST'])
def validate():
    data = request.get_json()
    if (int(data["tag_data"]) in ids):
        print("Valid")
        ids.remove(int(data["tag_data"]))
        return jsonify({"result":"valid"})
    else:
        print("Invalid")
        return jsonify({"result":"invalid"})

@app.route("/api/gentag", methods=['GET'])
def generate():
    id = random.randint(111111,999999)
    ids.append(id)
    print(f"New valid ID generated: {id}")
    return jsonify({ "id":str(id) })

if __name__ == "__main__":
    app.run("0.0.0.0", 80, True)
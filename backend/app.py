from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Sentinel-AI Running"

@app.route("/scan", methods=["POST"])
def scan():
    url = request.json.get("url")

    try:
        r = requests.get(url)

        result = {
            "url": url,
            "status_code": r.status_code,
            "length": len(r.text),
            "possible_vulnerability": []
        }

        # basic checks (start)
        if "login" in r.text.lower():
            result["possible_vulnerability"].append("Login Page Found")

        if "error" in r.text.lower():
            result["possible_vulnerability"].append("Error Message Exposure")

        return jsonify(result)

    except:
        return jsonify({"error": "Scan failed"})
        
if __name__ == "__main__":
    app.run(debug=True)
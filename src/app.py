from flask import Flask, jsonify, request

# create an example app  with Flask
app = Flask(__name__)


# create a route for the app
@app.route("/api", methods=["GET"])
def api():
    # get the data from the request
    data = {"request.get_json(force=True)": "oi"}

    # return a JSON response
    return jsonify(data)


# run the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)

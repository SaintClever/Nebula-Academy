from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def get_route():
    return jsonify({"message":'Hello /'})

@app.route('/api/data', methods=['POST'])
def handle_data():
    # Check if the request has JSON data
    if not request.json:
        return jsonify({"error": "Request must contain JSON data"}), 400

    data = request.json
    # Example validation: Check if 'name' is present in the JSON data
    if 'name' not in data:
        return jsonify({"error": "Missing 'name' in JSON data"}), 400

    # Use the data to perform operations, for example, returning a personalized message
    return jsonify({"message": f"Hello, {data['name']}!"})

if __name__ == '__main__':
    app.run(debug=True)
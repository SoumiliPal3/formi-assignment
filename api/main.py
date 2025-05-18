from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Path to your knowledge base JSON files
KB_PATH = os.path.join(os.path.dirname(__file__), '..', 'kb')
DATA_FOLDER = KB_PATH 
@app.route("/kb/<location>", methods=["GET"])
def get_kb(location):
    """
    Serves structured knowledge base data for a specific location.
    Example: /kb/indiranagar or /kb/jpnagar
    """
    filename = f"{location.lower().replace(' ', '_')}.json"
    filepath = os.path.join(KB_PATH, filename)
    
    if not os.path.exists(filepath):
        return jsonify({"error": f"No knowledge base found for '{location}'."}), 404

    with open(filepath, "r") as f:
        data = json.load(f)
    return jsonify(data)


@app.route('/menu', methods=['GET'])
def get_menu():
    file_path = os.path.join(DATA_FOLDER, 'menu.json')

    if not os.path.exists(file_path):
        return jsonify({"status": "error", "message": "Menu file not found"}), 404

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            menu_data = json.load(f)
        return jsonify({"status": "success", "data": menu_data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
@app.route('/properties', methods=['GET'])
def list_available_properties():
    properties = []
    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith('.json') and filename != 'menu.json':
            with open(os.path.join(DATA_FOLDER, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                properties.append({
                    "primary_name": filename.replace('.json', ''),
                    "address": data.get("address", ""),
                    "city": data.get("branch_name", "").split(",")[-1].strip()
                })
    return jsonify({"status": "success", "properties": properties})
if __name__ == "__main__":
    # Start the server on localhost:5000
    app.run(debug=True)

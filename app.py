from flask import Flask, jsonify, request
from engine import run_move, check_status

app = Flask(__name__)

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()

    if not data or 'state' not in data or 'player' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    state = data['state']
    player = data['player']
    

    action = run_move(state, player)
    return jsonify(action)

@app.route('/status', methods=['POST'])
def status():
    data = request.get_json()

    if not data or 'state' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    state = data['state']
    c, w = check_status(state)
    return jsonify({"status": c, "winner": w})

if __name__ == '__main__':
    app.run(port=8000,debug=True)


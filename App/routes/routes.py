from flask import Flask, request, jsonify
from flask_cors import CORS
from services.flashcard_service import main

app = Flask(__name__)
CORS(app)

@app.route('/flashcards/generate', methods=['POST'])
def generate_flashcards():
    data = request.get_json()
    return main(data)

if __name__ == '__main__':
    app.run(debug=True)

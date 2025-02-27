from flask import Flask, request, jsonify
from flask_cors import CORS
from script import get_sentences

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

def get_first_simplified_sentence(results):
    # Access the first item from the dictionary to get the simplified sentence
    _, (first_simplified_sentence, _) = next(iter(results.items()))
    
    return first_simplified_sentence


@app.route('/simplify', methods=['POST'])
def simplify():
    data = request.json  # Get JSON data from the POST request
    input_text = data.get('text', '')  # Extract 'text' field

    try:
        # Simplify the text using script function
        results = get_sentences(input_text)
        simplified_text = get_first_simplified_sentence(results)

        return jsonify({'simplified_text': simplified_text})
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

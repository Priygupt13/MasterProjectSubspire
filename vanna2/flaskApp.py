from flask import Flask, request, jsonify
from add_data_to_postgres import get_answer

app = Flask(__name__)


@app.route('/get_answer', methods=['POST'])
def get_answer_endpoint():
    # Get the input data from the request
    data = request.json

    # Extract the user input from the request data
    user_input = data.get('user_input')

    # Call your function to get the answer
    response = get_answer(user_input)

    # Return the response as JSON
    return jsonify({'answer': response})

if __name__ == '__main__':
    app.run(debug=True)
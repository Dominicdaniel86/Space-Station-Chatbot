from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
feedback_file = "../data/feedback.txt"
CORS(app)  # enable CORS

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/sendmessage', methods=['POST'])
def sendmessage():
    message = request.form['message']
    print(message)
    responses = []
    try:
        rasa_response = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": message})
    except Exception as e:
        print(f"error: {e}")
        responses.append({"type": "text", "content": "Oh, it appears that I'm not availabe. Please try again later!"})
        return jsonify(responses)

    for resp in rasa_response.json():
        if "text" in resp:
            responses.append({"type": "text", "content": resp["text"]})
        if "image" in resp:
            responses.append({"type": "image", "content": resp["image"]})
        if "buttons" in resp:
            responses.append({"type": "buttons", "content": resp["buttons"]})
        
        return jsonify(responses)

@app.route('/feedback', methods=['POST'])
def feedback():
    timestamp = request.form['timestamp']
    name = request.form['name']
    feedback = request.form['feedback']

    input = [
        'timestamp:' + str(timestamp) + '\n',
        'name:' + str(name) + '\n',
        'feedback:' + str(feedback) + '\n\n'
    ]
    with open(feedback_file, 'a') as file:
        file.writelines(input)

    return "feedback received"

if __name__ == '__main__':
    app.run(debug=True)

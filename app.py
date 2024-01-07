from flask import Flask, render_template, request, jsonify
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client with the API key from the .env file
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # Constructing the chat messages for each input
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    for key in request.form:
        input_text = request.form[key]
        messages.append({"role": "user", "content": input_text})

    try:
        print("here")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        print(response)
        # Accessing the content of the last message in the response
        # summary = response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to generate response from OpenAI."})

    # Constructing the response data
    # print(summary)
    data = {"test": "this is a test"}
    # data = {f"input{index+1}": summary for index, _ in enumerate(messages[1:])}

    # Return the summarized data in JSON format
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

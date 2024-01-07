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
    # Constructing the system message for the prompt
    system_message = "Provide a summary for each of the following inputs in the format 'input [number]: [summary]'."
    messages = [{"role": "system", "content": system_message}]

    # Adding user messages for each input
    for key in sorted(request.form):
        input_text = request.form[key]
        messages.append(
            {"role": "user", "content": f"input {key[-1]}: {input_text}"})

    try:
        chat_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        # Extract responses for each input
        responses = [
            msg.message.content for msg in chat_response.choices if msg.message.role == "assistant"]
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to generate response from OpenAI."})

    # Parsing the structured responses
        # "input 1: first\ninput 2: second\ninput 3: third\ninput 4: fourth"
    response_text = responses[0]
    summary_lines = response_text.split("\n")

    data = {}
    for line in summary_lines:
        parts = line.split(":")
        if len(parts) == 2:
            # Removes spaces, e.g., "input1"
            key = parts[0].replace(" ", "").strip()
            value = parts[1].strip()  # e.g., "first"
            data[key] = value

    # Return the parsed data in JSON format
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

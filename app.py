from flask import Flask, render_template, request, jsonify
import os
from openai import OpenAI
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client with the API key from the .env file
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    logging.error("OPENAI_API_KEY not found in environment variables.")
    exit("Please set your OPENAI_API_KEY in the .env file.")

client = OpenAI(api_key=api_key)


def construct_messages(request_form):
    """Construct the messages for GPT-3.5 API request."""
    system_message = "Provide a max 10 word summary for each of the following inputs in the format 'input[number]: [summary]'."
    messages = [{"role": "system", "content": system_message}]
    for key in sorted(request_form):
        input_text = request_form[key]
        messages.append(
            {"role": "user", "content": f"input{key[-1]}: {input_text}"})
    return messages


def generate_summaries(messages):
    """Generate summaries using OpenAI API."""
    try:
        chat_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return [msg.message.content for msg in chat_response.choices if msg.message.role == "assistant"]
    except Exception as e:
        logging.error(f"Error in generating summaries: {e}")
        return None


def parse_summaries(response_text):
    """Parse GPT-3.5 response text into structured data."""
    summary_lines = response_text.split("\n")
    data = {}
    for line in summary_lines:
        parts = line.split(":")
        if len(parts) == 2:
            key = parts[0].replace(" ", "").strip()  # "input1", "input2", etc.
            value = parts[1].strip()  # The summary text
            data[key] = value
    return data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    messages = construct_messages(request.form)

    logging.info("Sending message to GPT-3.5")
    responses = generate_summaries(messages)
    if responses is None:
        return jsonify({"error": "Failed to generate response from OpenAI."})

    data = parse_summaries(responses[0])
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

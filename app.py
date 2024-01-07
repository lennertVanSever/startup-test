from flask import Flask, render_template, request, jsonify
from openai_service import construct_messages, generate_summaries, parse_summaries

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    messages = construct_messages(request.form)
    responses = generate_summaries(messages)
    if responses is None:
        return jsonify({"error": "Failed to generate response from OpenAI."})

    data = parse_summaries(responses[0])
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

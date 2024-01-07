from flask import Flask, render_template, request, jsonify
import time  # Import the time module

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # Delay of 2 seconds
    time.sleep(2)

    # Retrieving data from the form
    data = {key: request.form[key] + ' summarized' for key in request.form}

    # Return the data in JSON format
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

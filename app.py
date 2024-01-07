from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # Retrieving data from the form
    input1 = request.form['input1']
    input2 = request.form['input2']
    input3 = request.form['input3']
    input4 = request.form['input4']

    # Print inputs to the console
    print("Input 1:", input1)
    print("Input 2:", input2)
    print("Input 3:", input3)
    print("Input 4:", input4)

    # You can return a response or redirect to another page
    return "Form submitted and data printed in console."


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world_json():
    return jsonify({'result': 'Hello, World!'})


@app.route('/hello')
def hello_world_html():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
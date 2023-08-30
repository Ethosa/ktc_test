from flask import Flask, render_template, request, jsonify, url_for


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """
    Main endpoint
    """
    return render_template('auth.html')


@app.route('/profile', methods=['GET'])
def profile():
    """
    Profile endpoint
    """
    return render_template('profile.html')


@app.route('/auth', methods=['POST'])
def auth():
    """
    User authorization
    """
    username = request.args.get('username')
    password = request.args.get('password')
    if username == 'admin' and password == 'admin':
      response = jsonify({'response': 'success'})
    else:
      response = jsonify({'response': 'failure'})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True)

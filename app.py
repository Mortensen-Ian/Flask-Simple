from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    message = None
    if request.method == 'POST':
        message = request.form.get('message')
    return render_template('index.html', message=message)

if __name__ == "__main__":
    application.run(debug=True)

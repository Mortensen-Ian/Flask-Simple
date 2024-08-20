from flask import Flask, render_template, request, redirect, url_for

application = Flask(__name__)

@application.route('/', methods=['POST', 'GET'])
def index():
    message = None
    if request.method == 'POST':
        ## I want to get all the items that have been posted. 
        message = request.form.get('message')
    return render_template('index.html', message=message)

if __name__ == "__main__":
    application.run(debug=True)

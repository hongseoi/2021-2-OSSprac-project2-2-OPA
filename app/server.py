from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return render_template('login.html', login = login)


@app.route('/application-form', methods=['GET','POST'])
def application_form():
    if request.method == 'POST':
        return render_template('application_form', form = form)

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        return render_template('submit.html', submit = submit)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)

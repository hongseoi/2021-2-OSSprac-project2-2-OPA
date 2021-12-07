from flask import Flask, render_template, request, flash

app = Flask(__name__)


def is_valid_req(form: dict) -> bool:
    if form['username'] == 'ossp' and form['password'] == 'ossp1234':
        return True
    else:
        return False


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')


@app.route('/application-form', methods=['POST'])
def application_page():
    if is_valid_req(request.form):
        return render_template('application_form.html')
    else:
        return render_template('auth_failed.html')


@app.route('/check', methods=['POST', 'GET'])
def check():
    sub = request.form.to_dict()
    return render_template("check.html", submit=sub)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    uname=request.form.get('uname')
    umajor=request.form.get('umajor')
    grade=request.form.get('grade')

    return render_template('submit.html', submit = sub)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)

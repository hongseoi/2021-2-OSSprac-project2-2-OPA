from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'ossp' or request.form['password'] != 'ossp1234':
            error = "잘못된 정보입니다. 다시 시도해 주세요!"
        
        else:
            return render_template('application_form.html')
    
    return render_template('login.html', error = error)


@app.route('/application-form', methods=['GET','POST'])
def application_form():
    if request.method == 'POST':
        return render_template('application_form', form = form)

@app.route('/check', methods=['POST','GET'])
def check():
    sub = request.form.to_dict()
    return render_template("check.html", submit = sub)

@app.route('/submit', methods=['GET','POST'])
def submit():
    uname=request.form.get('uname')
    umajor=request.form.get('umajor')
    grade=request.form.get('grade')
    
    return render_template('submit.html', submit = sub)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)

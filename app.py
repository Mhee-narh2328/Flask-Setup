from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html' , message = 'hello world!!!')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == 'Mheenarh' and password == 'ade':
            message = model.show_color('Mheenarh')
            return render_template('football.html', message = message)
        else:
            error_message = 'Hint: owner'
            return render_template('index.html', message = error_message)
if __name__ =='__main__':
    app.run(debug = True, port = 7000)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    # print(request.form) 
    name = request.form['name']
    return render_template('home.html', list_name = name)

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8000)
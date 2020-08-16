from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index2():
    message = "hello!"
    li = ["hello", "world"]
    dic = {"name":"AI ACADEMY", "lang":"Python"}

    return render_template('index2.html', message=message, li=li, dic=dic)

if __name__ == '__main__':
    app.run(port=12345, debug=False)


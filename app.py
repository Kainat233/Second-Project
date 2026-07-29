from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def disp():
    name = "Kainat"
    age = 24
    marks = round((600/700)*100, 2)
    return render_template("index.html", name=name, age=age, marks=marks)

if __name__ == '__main__':
    app.run(debug=True)

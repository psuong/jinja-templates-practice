from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('extends_example.html', name='My Name', description='My description')


if __name__ == '__main__':
    app.run(debug=True)

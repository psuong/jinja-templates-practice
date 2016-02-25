from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    # Directly assign the variables in the return statement when rendering the page.
    # Remember that you want to render the HTML file that is extending from the parent HTML file.
    pass

@app.route('/another-link')
def another_link():
    # Create a dictionary and use Python's keyword arguments to assign and pass all the variables to the template.
    pass


if __name__ == '__main__':
    app.run(debug=True)

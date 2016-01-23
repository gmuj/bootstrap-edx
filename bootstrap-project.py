from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def album_details():
    return render_template('album_details.html')


if __name__ == '__main__':
    app.run(debug=True)

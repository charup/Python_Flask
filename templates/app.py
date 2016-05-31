#$ pip install requests==2.9.1 beautifulsoup4==4.4.1 nltk==3.2
#$ pip freeze > requirements.txt
#$ mkdir templates
#$ touch templates/index.html

import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

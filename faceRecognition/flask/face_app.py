import numpy as np
import os
import glob2 as glob
import json

from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# ROOT_PATH = "../data/etl/2018_07_31_10_52/"
ROOT_PATH = '../data/'

@app.route('/')
def possible_ids():
    """ returns a list of files in data folder"""
    dirs = os.listdir(ROOT_PATH)
    return json.dumps(dirs)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
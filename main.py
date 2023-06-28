from flask import Flask
from flask import sessions
from flask import request
from flask import render_template
from flask import redirect, url_for
from werkzeug.utils import secure_filename
import json
import os
from modules.data import *
from definition import *
import mysql.connector
from mysql.connector import Error
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Union
app = Flask(__name__)

@app.route('/', methods=['GET'])
def getin():
    inf =info() 
    information = inf.getinfo()
    return information

if __name__  == "__main__":
    app.run(debug=True)
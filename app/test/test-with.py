"""
create by hanxiao on
"""

from flask import Flask, current_app

__author__ = "hanxiao"

app = Flask(__name__)

with app.app_context():
    a = current_app
    b = current_app.config["DEBUG"]


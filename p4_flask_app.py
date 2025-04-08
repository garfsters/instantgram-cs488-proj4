
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, request, render_template

import example

app = Flask(__name__)

@app.route('/example/listimages')
def example_listimages():
    return example.listimages()

@app.route('/example/uploadfile', methods=['POST'])
def example_uploadfile():
    return example.uploadfile()

@app.route('/example/listfiles')
def example_listfiles():
    return example.listfiles()
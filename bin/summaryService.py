# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 17:20:30 2020

@author: sufiy
"""

import flask
from flask import Flask,request
from summarizer import SummarizeDoc

app = Flask(__name__)

@app.route('/get_summary',methods=['GET'])
def findSummary():
    summarizeObj = SummarizeDoc()
    summary = summarizeObj.findSummary()
    return summary

app.run('localhost',port=8023)
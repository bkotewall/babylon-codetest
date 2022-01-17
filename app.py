from flask import Flask, render_template, redirect, url_for, jsonify
import requests 
import logging
import time

app = Flask(__name__)

@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Heroku Analysis API!
    <br>Available Routes:
    <br>/api/v1.0/heroku_status
    <br>/api/v1.0/app1
    <br>/api/v1.0/app2
    <br>/api/v1.0/app3
    ''')

@app.route("/api/v1.0/heroku_status")
def heroku_status():
    api_url="https://status.heroku.com/api/v4/current-status"
    response =  requests.get(api_url, timeout=10)
    #response = requests.post(api_url, data=post_fields, timeout=10)
    return str(response.elapsed.total_seconds())

@app.route("/api/v1.0/app1")
def app1_status():
    url="https://www.google.com"
    return check_response(url)

@app.route("/api/v1.0/app2")
def app2_status():
    url="https://www.reddit.com"
    return check_response(url) 

@app.route("/api/v1.0/app3")
def app3_status():
    url="https://news.ycombinator.com"
    return check_response(url)

def check_response(url):
    start = time.process_time()
    response = requests.get(url, timeout=20)
    request_time = time.process_time() - start
    logging.info("Request completed in {0:.0f}ms".format(request_time))
    web_response = dict()
    web_response[url]=request_time
    return jsonify(web_response)

if __name__ == '__main__':
    app.run()

import datetime
import os
import requests

from flask import Flask, Response, request

from db import init_db, query_db, close_connection

app = Flask(__name__)


@app.route("/search/<keyword>")
def search(keyword):
    '''
    with app.app_context():
        users = query_db("select * from users")
    '''
    base_url = '/'.join([
        'https://maps.googleapis.com',
        '/maps/api/place/findplacefromtext/json'
    ])
    query_str = [
        'input=%s' % keyword,
        'inputtype=textquery',
        'fields=photos,formatted_address,name,rating,opening_hours,geometry',
        'key=AIzaSyBtuCzmWiqghKRfiHDs-uW5uO8bQkK51ic'
    ]
    url = '%s?%s' % (base_url, '&'.join(query_str))
    # r = requests.get(url)
    return Response(url, mimetype="application/json", status=200)


@app.teardown_appcontext
def _close_connection(exception):
    close_connection(exception)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

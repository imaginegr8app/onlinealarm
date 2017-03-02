#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/setAlarm', methods=['POST'])
def setAlarm():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = {}

    res = json.dumps(res, indent=4)
    # print(res)
    r = {
        "speech": set alarm successfully,
        "displayText": set alarm successfully,
        "data": {},
        # "contextOut": [],
        "source": "onlineAlarm"
    }
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')

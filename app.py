import os, sys
from flask import flask, request

from pymessenger import Bot


access_tkn="wifi chalao bhai"
bot=Bot(access_tkn);

@app.route("/", methods=['GET'])
def verify():
	#verify webhook koi wifi chalado!!!!!!!!!!!
	if request.args.get("hub.mode")=="subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == "wifi":
			return "verify token failed", 

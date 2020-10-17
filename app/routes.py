from app import app
from flask import render_template, jsonify, request
from .messages import Message

HTTP_OK = 200
HTTP_BAD_REQUEST = 400

# This would be replaced by a database setup with more time.
messages = []

# This was added as part of troubleshooting the pytests.
@app.route('/')
def heartbeat():
	response = jsonify({"message": "heartbeat"})
	response.status_code = HTTP_OK
	return response	

@app.route('/messages', methods=['GET'])
def get_all_messages():
	recipient = request.args.get('recipient')

	if recipient != None:
		response = jsonify(Message.filter_to_collection_dict(recipient, messages))
		response.status_code = HTTP_OK
		return response

	else:
		response = jsonify(Message.to_collection_dict(messages))
		response.status_code = HTTP_OK
		return response

@app.route('/messages', methods=['POST'])
def post_message():
	request_data = request.get_json()
	saved_message = Message()

	# With more time, I would break this out by field in order to provide the user with exactly which field(s) were missing
	if 'recipient' not in request_data or 'sender' not in request_data or 'message' not in request_data:
		error_payload = {'message': 'Input must include recipient, sender and message fields'}
		response = jsonify(error_payload)
		response.status_code = HTTP_BAD_REQUEST
		return response

	Message.from_dict(saved_message, request_data)
	messages.append(saved_message)
	response = jsonify(Message.to_dict(saved_message))
	response.status_code = HTTP_OK
	return response
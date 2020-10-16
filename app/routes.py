from app import app
from flask import render_template, jsonify, request

@app.route('/messages', methods=['GET'])
def get_all_messages():
	pass#return jsonify(Message.query.get_or_404()).to_dict())

@app.route('/messages/<int:recipient>', methods=['GET'])
def get_messages_by_recipient(recipient):
	pass

@app.route('/messages', methods=['POST'])
def post_message():
	request_data = request.get_json()
	saved_message = Message()
	Message.from_dict(saved_message, request_data)
	return '''
	Request data:
	message is: {}
	'''.format(Message.to_dict(saved_message))

	

class Message():
	recipient = ""
	sender = ""
	message = ""
	sentOn = 0

	def to_dict(self):
		data = {
			'recipient': self.recipient,
			'sender': self.sender,
			'message': self.message,
			'sentOn': self.sentOn
		}
		return data

	def from_dict(self, data):
		for field in ['recipient', 'sender', 'message']:
			if field in data:
				setattr(self, field, data[field])


	# pagination
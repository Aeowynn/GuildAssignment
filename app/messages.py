from datetime import datetime

class Message:
	recipient = ""
	sender = ""
	message = ""
	sent_on = 0

	def to_dict(self):
		data = {
			'recipient': self.recipient,
			'sender': self.sender,
			'message': self.message,
			'sent_on': self.sent_on
		}
		return data

	def from_dict(self, data):
		for field in ['recipient', 'sender', 'message']:
			if field in data:
				setattr(self, field, data[field])
		# Setting the date automatically; the user shouldn't provide this field
		setattr(self, 'sent_on', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

	def to_collection_dict(messages):
		data = {
			'messages': [item.to_dict() for item in messages]
		}
		return data

	def filter_to_collection_dict(recipient, messages):
		filtered_messages = []
		for item in messages:
			if item.recipient == recipient:
				filtered_messages.append(item)
		data = {
			'messages': [item.to_dict() for item in filtered_messages]
		}
		return data
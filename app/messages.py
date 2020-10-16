
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
				setattr(seld, field, data[field])


	# pagination
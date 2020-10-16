# Service tests // Would be integration with database setup

# Message Helpers
#postMessage()
	#hits the post endpoint to submit; returns response

#postMessageAndAssertStatus
	#calls postMessage()
	#asserts status

#getMessagesByRecipient()
	#hits the get endpoint to submit; returns response

#getMessagesByRecipientAndAssertStatus()
	#calls getMessagesByRecipient()
	#asserts status

#getAllMessages()
	#hits the get all endpoint to submit; returns response

#getAllMessagesAndAssertStatus()
	#calls getAllMessages()
	#asserts status

#assertMessageFields()


# Post Endpoint Tests
#postMessageReturns201
	#sets up message
	#calls postMessageAndAssertStatus()

#postMessageSavesMessageFields
	#sets up message
	#calls postMessageAndAssertStatus

#postMessageReturns400IfRequiredMessageIsMissing

#postMessageReturns400IfRequiredSenderIsMissing

#postMessageReturns400IfRequiredRecipientIsMissing


# Get Messages by Recipient Endpoint tests
#getMessagesByRecipientReturns200

#getMessagesByRecipientReturnsExpectedDataFields

#getMessagesByRecipientReturns404IfNoMessagesExist

#getMessagesByRecipientReturns404IfMessagesExistForAnotherRecipient


#Get All Messages endpoint tests
#getAllMessagesReturns200

#getAllMessagesReturnsExpectedDataFields

#getAllMessagesReturns404IfNoMessagesExist
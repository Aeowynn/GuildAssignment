# Service tests

# Please note I was not able to get these working - the server was inaccesible and I could not troubleshoot it quickly.
# However, they still show how I structure tests as well as the cases that I would cover for this set of functionality.

import pytest
from .__init__ import app 
from flask import json

message = 'Hello'
recipient = 'To'
sender = 'From'

test_data = json.dumps({
	'message': message,
	'recipient': recipient,
	'sender': sender
})

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client

# Heartbeat test
def test_heartbeat():
	response = app.test_client().get('/')
	assert 'beat' in response.data

# Message Helpers
# I like to separate these out both to reduce duplicated lines and to make the tests more readable
def post_message_and_assert_status(input_code, data):
	response = app.test_client().post('/messages', data=data, content_type='application/json')
	
	assert response.status_code == input_code

	return response

def get_messages_by_recipient_and_assert_status(input_code):
	response = app.test_client().get('/messages')

	assert response.status_code == input_code

	return response

def get_all_messages_and_assert_status(input_code):
	response = app.test_client().get('/messages/?recipient=To')

	assert response.status_code == input_code

	return response

# This reduces duplicated lines; for larger models, sometimes I would break this up to into multiple sections.
# Ex: if our model includes driver and vehicle information
#	 then those would be split across two methods - one for drivers and one for vehicles
def assert_message_fields(response_data):
	assert response_data['message'] == message
	assert response_data['recipient'] == recipient
	assert response_data['sender'] == sender


# Post Endpoint Tests
def test_post_message_returns_200():
	post_message_and_assert_status(200, test_data)

def test_post_message_returns_saved_message_fields():
	response = post_message_and_assert_status(200, test_data)

	assert_message_fields(response.data)

def test_post_message_returns_400_if_required_message_is_missing():
	no_message = json.dumps({
		'recipient': recipient,
		'sender': sender
	})

	post_message_and_assert_status(400, no_message)

def test_post_message_returns_400_if_required_sender_is_missing():
	no_recipient = json.dumps({
		'message': message,
		'sender': sender
	})

	post_message_and_assert_status(400, no_recipient)

def test_post_message_returns_400_if_required_recipient_is_missing():
	no_sender = json.dumps({
		'message': message,
		'recipient': recipient,
	})

	post_message_and_assert_status(400, no_sender)


# Get Messages by Recipient Endpoint tests
def test_get_messages_by_recipient_returns_200():
	post_message_and_assert_status(200, test_data)

	get_messages_by_recipient_and_assert_status(200)

# Given more time, I would add a few more messages to this test and assert on those as well
def test_get_messages_by_recipient_returns_expected_data_fields():
	post_message_and_assert_status(200, test_data)

	response = get_messages_by_recipient_and_assert_status(200)

	assert_message_fields(response.data[0])

def test_get_messages_by_recipient_returns_empty_list_if_no_messages_exist():
	response = get_messages_by_recipient_and_assert_status(200)
	assert len(response.data) == 0

def test_get_messages_by_recipient_returns_empty_list_if_messages_exist_for_another_recipient():
	different_recipient = json.dumps({
		'message': message,
		'recipient': recipient,
		'sender': sender
	})

	post_message_and_assert_status(200, different_recipient)

	response = get_messages_by_recipient_and_assert_status(200)
	assert len(response.data) == 0


#Get All Messages endpoint tests
def test_get_all_messages_returns_200():
	get_all_messages_and_assert_status(200)

# Given more time, I would add a few more messages to this test and assert on those as well
def test_get_all_messages_returns_expected_data_fields():
	post_message_and_assert_status(200, test_data)

	response = get_all_messages_and_assert_status(200)
	assert_message_fields(response.data)

def test_get_all_messages_returns_empty_list_if_no_messages_exist():
	response = get_all_messages_and_assert_status(200)
	assert len(response.data) == 0
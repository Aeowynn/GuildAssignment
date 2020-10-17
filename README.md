# Chat API for Guild Education

## Running and Testing the code
To run the app, you'll need Python (I used 3.9.0) and Flask (I used 1.1.2). Then, add the flask environment variable with **$ export FLASK_APP=chatapp.py** and then start the server with **$ flask run**

I have provided my Postman tests for exercising these endpoints; I built out service tests, however please note that I was unable to get them working fully.

# Endpoint Documentation

## POST chat message endpoint

**Endpoint**: /messages

**Request body**:

  sender: some_string (required)
  
  recipient: some_string (required)
  
  message: some_string (required)
  
**Response body**:

  response_code: 201

  resonse_data:

      sender: some_string

      recipient: some_string

      message: some_string

      sent_on: some_date
  
  
  
**Possible response codes**:

201 - message stored

400 - missing required field


## GET chat messages for a recipient

**Endpoint**: /messages?recipient=some_string

**Request body**: None
  
**Response body**:

  response code: 200
  
  resonse data:
  
    List of:
    
      sender: some_string
      
      recipient: some_string
      
      message: some_string
      
      sent_on: some_date
      
      
      
**Possible response codes**:

200 - messages found

404 - no messages found for the provided recipient


## GET chat messages for all senders

**Endpoint**: /messages

**Request body**: None

  
**Response body**:

  response code: 200
  
  response data:
  
    List of:
    
      sender: some_string
      
      recipient: some_string
      
      message: some_string
      
      sent_on: some_date
      
      
      
**Possible response codes**:

200 - messages found

404 - no messages found for the provided sender

# Where would I go with more time?

## Troubleshoot the Service Tests
Having a suite of functional tests with good coverage of my code is incredibly important to me; it helps me have confidence that any new code I check in has not broken existing functionality. And, if I fix a bug that was not caught by a test, I do my best to add in a test to cover that to prevent that bug from being re-introduced.

I'd also like to expand on the validation some more. For example, ensuring that empty strings are not being passed in for message, sender and recipient.

## Implement a Database For Storing Messages
I'd start storing the messages in a database, rather than the list they're currently being stored in. Here are the fields that would be in the database table:

**Table**

Sender VARCHAR(64)

Recipient VARCHAR(64)

Sent_On DATETIME

Message VARCHAR(128)




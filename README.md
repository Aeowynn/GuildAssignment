# GuildAssignment
Chat API for Guild Education

## Database fields:
Sender

Recipient

SentOn

Message


## POST chat message endpoint

**Endpoint**: /messages

**Request body**:

  senderName: someString (required)
  
  recipientName: someString (required)
  
  message: someString (required)
  
  
  
**Possible response codes**:

204 - message stored

400 - missing required field


## GET chat messages for a recipient (100 most recent || all messages in last 30 days) ordered by newest to oldest

**Endpoint**: /messages

**Request body**:

  recipientName: someString
  
**Response body**:

  responseCode: 200
  
  resonseData:
  
    List of:
    
      senderName: someString
      
      recipientName: someString
      
      message: someString
      
      sentOn: someDate
      
      
      
**Possible response codes**:

200 - messages found

404 - no messages found for the provided recipient


## GET chat messages for all senders (100 most recent || all messages in last 30 days) ordered by newest to oldest

**Endpoint**: /messages

**Request body**: None

  
**Response body**:

  responseCode: 200
  
  responseData:
  
    List of:
    
      senderName: someString
      
      recipientName: someString
      
      message: someString
      
      sentOn: someDate
      
      
      
**Possible response codes**:

200 - messages found

404 - no messages found for the provided sender


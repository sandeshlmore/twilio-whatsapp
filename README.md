# Twilio-Whatsapp

#### Whatsapp Messaging with Twilio Apis
A Restful API which acts webhook for receiving incoming message to a twilio whatsapp number and sends dummy reply to the same user.

## Installation

### Setup Database:
    
- MongoDB database is used to save messages sent by user.
- Refer to this article for setting up mongodb cluster: https://www.mongodb.com/basics/mongodb-atlas-tutorial
- setup database named ***messaging*** user with ***read/write*** access.
- create collection named ***messages***.


### Clone the repository:
    
      https://github.com/sandeshlmore/twilio-whatsapp.git

### Set environment variables:
      
      MONGO_URI : mongodb connection string ("mongodb+srv://{DBUsername}:{UserPassword}@clusterName.example.mongodb.net/DBNAME?retryWrites=true&w=majority")
      DB_NAME : MongoDB database name
      TWILIO_WHATSAPP_NUMBER : twilio whatsapp number
      TWILIO_API_KEY: twilio account token
      TWILIO_SID : twilio account sid

- Reference for setting up twilio account and using sdk: https://www.twilio.com/docs/whatsapp

### Configure webhook url in twilio account

- Webhook Endpoint: ***/messaging/webhook/dummy-reply***
- Reference: https://www.twilio.com/docs/usage/webhooks/getting-started-twilio-webhooks
- Note: If you are running locally you might need to use ngrok or something similar to be able to receive messages.

## Run :
- Create a virtual environment and activate it:

        python3 -m venv venv OR virtualenv --python=python3 venv
        source venv/bin/activate
        pip install -r requirements.txt
      
- run flask server:

       python3 wsgi.py


    

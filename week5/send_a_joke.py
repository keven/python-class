# /usr/bin/env python
# -*- coding: UTF-8 -*-
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import random

app = Flask(__name__)

jokes = [
"Why didn’t the skeleton want to go to school?  His heart wasn’t in it.",
"What is a vampire’s favorite fruit? ..... A necktarine!",
"Why are ghosts so bad at lying? .....  Because you can see right through them!",
"What do you call a fat pumpkin? ..... A plumpkin.",
"When is it bad luck to be followed by a black cat? ..... When you’re a mouse.",
"Why are ghosts so bad at lying? ..... Because you can see right through them!",
"How do you make a witch itch? ..... Take away the W.",
"Why did the vampire need mouthwash? ..... Because he had bat breath.",
"Know why skeletons are so calm? ..... Because nothing gets under their skin."
]

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
    # Try adding your own number to this list!
    callers = {
        "+16047641525": "Keven",
    }
    from_number = request.values.get('From', None)

    message = callers[from_number] if from_number in callers else ""

    body_message = request.values.get('Body', None)
    if body_message and "joke" in body_message.lower():
        message = "Hey {}   {}".format(message, random.choice(jokes))
    else:
        message = "Hello {}".format(message)

    resp = MessagingResponse()
    resp.message(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

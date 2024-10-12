from flask import Flask, request, jsonify

from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

school_info = {
    "courses": "Our school offers Math, Science, and Computer Science.",
    "calendar": "The school year starts in January and ends in December.",
    "fees": "The annual fee is $2000.",
}

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    # Basic logic to respond based on input
    if "courses" in incoming_msg:
        response = school_info["courses"]
    elif "calendar" in incoming_msg:
        response = school_info["calendar"]
    elif "fees" in incoming_msg:
        response = school_info["fees"]
    else:
        response = "I'm sorry, I don't understand your question. Try asking about courses, calendar, or fees."
    
    msg.body(response)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)




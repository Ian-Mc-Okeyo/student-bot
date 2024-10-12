from flask import Flask, request, jsonify
from openai import OpenAI

from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

client = OpenAI()

school_info = {
    "courses": "Our school offers Math, Science, and Computer Science.",
    "calendar": "The school year starts in January and ends in December.",
    "fees": "The annual fee is $2000.",
}

def generate_answer(question):
    # completion = client.chat.completions.create(
    #     model="babbage-002",
    #     messages=[
    #         {"role": "user", "content": "Explain RAG in ML"}
    #     ]
    # )

    # return completion.choices[0].message
    if question == 'how can i begin to prepare to file my taxes':
        return "1. Applied for an SSN (or ITIN) 2. Requeste for the tax form  from the HR"

    return "Sorry, I can't quite get that"

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    answer = generate_answer(incoming_msg.lower())

    print(answer)
    
    msg.body(answer)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)




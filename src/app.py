
from flask import Flask, request
import sendEmail

app = Flask(__name__)

@app.route('/email', methods=['POST'])
def sendEmailR():
    email = request.json['email']
    message = request.json['message']
    subject = request.json['subject']
    sendEmail.emailCheck(email,subject,message)
    return "email"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
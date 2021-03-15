from flask import Flask, request
from pprint import pprint
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

email_add = 'codemistritm@gmail.com'
email_pass = 'oggjrzwqktacqddh'


@app.route('/')
def verify():
    return "app is running"


@app.route('/contact', methods=['POST'])
def post_email():
    request_data = request.json
    pprint(request_data)

    if 'email' and 'message' and 'name' and 'subject' in request_data:
        msg = EmailMessage()
        msg['Subject'] = request_data['subject']
        msg['From'] = request_data['email']
        msg['To'] = email_add
        name = request_data['name']
        msg.set_content(
            "   From " + name + ", " + "\n\n" + "  " + request_data['message'] + "\n\n" + "My email: " + request_data[
                'email'])
        pprint(request_data['subject'])

        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp.login(email_add, email_pass)
        smtp.send_message(msg)
        return "received"
    else:
        return "sorry"


if __name__ == '__main__':
    app.run()

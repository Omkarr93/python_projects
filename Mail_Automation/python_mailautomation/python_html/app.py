from flask import Flask, render_template, request
from decouple import config
from flask_mail import Mail, Message



email = config("user")
app_password = config("password")

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = app_password
app.config['MAIL_DEFAULT_SENDER'] = email

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send():
    to_email = request.form['to_email']
    subject = request.form['subject']
    message = request.form['message']

    msg = Message(subject=subject, recipients=[to_email])
    msg.body = message

    mail.send(msg)

    return 'Email sent!'


if __name__ == '__main__':
    app.run(debug=True)



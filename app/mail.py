from flask_mail import Mail, Message

mail = None


def setMail(app):
    global mail
    mail = Mail(app)

    return mail, app

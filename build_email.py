#!/usr/bin/env python3

import os.path
import smtplib
import getpass
import mimetypes
from email.message import EmailMessage

attachment_path = os.path.join(os.getcwd(), "cat.jpg")
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

sender = "ericrohner22@gmail.com"
recipient = "ericrohner22@gmail.com"

body = """Hello Dog,

I am Cat."""


if __name__ == "__main__":
	message = EmailMessage()
	message['From'] = sender
	message['To'] = recipient
	message.set_content(body)
	with open(attachment_path, 'rb') as att:
		message.add_attachment(att.read(),
		maintype = mime_type,
		subtype = mime_subtype,
		filename = attachment_path)
	mail_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
	mail_server.ehlo()
	mail_pass = getpass.getpass("password?")
	mail_server.login(sender, mail_pass)
	mail_server.send_message(message)
	mail_server.quit()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "your_email@gmail.com"
sender_password = "your_email_password"
recipient_email = "recipient_email@example.com"
subject = "Test Email"
message_body = "This is a test email sent from Python."

# Create a MIME message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject

# Attach the message body
msg.attach(MIMEText(message_body, "plain"))

# SMTP server configuration (for Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Create an SMTP connection
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())
    print("Email sent successfully!")

except smtplib.SMTPException as e:
    print("Email could not be sent. Error:", str(e))

finally:
    # Close the SMTP connection
    server.quit()

import smtplib
import email.message

def send_email():
    email_body = """
    <p>Line1</p>
    <p>Line2</p>
    """

    msg = email.message.Message()
    msg["Subject"] = "Subject"
    msg["From"] = "Sender"
    msg["To"] = "Receiver"
    password = "password"
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(email_body)

    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg["From"], password)
    s.sendmail(msg["From"], msg["To"], msg.as_string().encode("utf-8"))
    print("Email sent")

send_email()
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as dt

def get_email_body(name, role, company):
    now = dt.datetime.now().time()
    if now < dt.datetime.strptime('12:00', '%H:%M').time():
        greeting = "Good morning"
    elif now < dt.datetime.strptime('17:00', '%H:%M').time():
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    email = (
        f"{greeting} {name}!\n\n"
        f"Hope you are doing well! "
        f"My name is Yash and I am a representative of Fierceli Inc. I got to know that there is a {role} role open "
        f"at {company}. I understand {company} uses an agency help to fill such roles and I have a stellar candidate. "
        f"I was wondering if you would be the correct person to whom I would send their resume? If not, who would "
        f"be the best person to reach out to?\n\n"
        f"We at Fierceli are local to the Bay Area and have been successfully helping clients with superior talent "
        f"for over fifteen years to date. I would be extremely grateful for the opportunity to help find the right candidate "
        f"for your needs!\n\n"
        f"I would love to set up some time to discuss those needs if you are open to a fifteen minute in person conversation? "
        f"If you prefer virtual, I'm also happy to set up a fifteen minute call via Teams!\n\n"
        f"Looking forward to connecting!\n"
    )
    return email

def send_email(email_body, role, company):

    sender_email = "<example@example.com>"
    password = "password"
    smtp_server = "smtp.office365.com"
    port = 587


    receiver_email = "<example@example.com>"
    subject = f"Regarding {role} at {company}"
    body = email_body

    # Create the MIMEText object for the email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Establish a secure connection with the SMTP server using TLS
    context = ssl.create_default_context()

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)  # Start TLS encryption
        server.login(sender_email, password)  # Login to your Outlook account
        print("reached")
        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        server.quit()  # Close the SMTP connection

if __name__ == '__main__':
    pass

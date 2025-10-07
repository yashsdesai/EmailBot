import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as dt

def get_credentials() -> List[str, str]:
    with open("credentials.txt", "r") as f:
        email = f.readline()
        password = f.readline()

    return [email, password]


def get_email_body(name: str) -> str:
    now = dt.datetime.now().time()
    if now < dt.datetime.strptime('12:00', '%H:%M').time():
        greeting = "Good morning"
    elif now < dt.datetime.strptime('17:00', '%H:%M').time():
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    email = (
        f"{greeting} {name}!\n\n"
        f"<Insert body content here>\n"
    )
    return email

def send_email(sender_email: str, password:str, email_body:str) -> bool:

    smtp_server = "smtp.office365.com"
    port = 587


    receiver_email = "<example@example.com>"
    subject = "<example subject>"
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

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    finally:
        server.quit()  # Close the SMTP connection
        return True

if __name__ == '__main__':
    email, password = get_credentials()
    email_body = get_email_body("<name>")
    send_email(email, password, email_body)
    
    



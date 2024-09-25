import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from os.path import exists
from src.logger import log_err , log_info 
def send_email(html_content, img_paths, password, sender_email, receiver_email, smtp_server="smtp.gmail.com", port=587):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "Attendance Report."

        msg.attach(MIMEText(html_content, 'html'))
        # Attach images
        if img_paths:
            for cid , image_path in img_paths:
                if exists(image_path):
                    with open(image_path, 'rb') as img_file:
                        img = MIMEImage(img_file.read())
                        img.add_header('Content-ID', f'<{cid}>')
                        msg.attach(img)
        
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls()
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            log_info(f"Email send succesfully to {receiver_email}")
            return True
        
    except Exception as e:
        log_err(f"Error: {e}")
    return False

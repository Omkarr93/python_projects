from decouple import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

# Set your email login credentials
email = config("user")
app_password = config("password")
DEBUG = config('DEBUG', default=False, cast=bool)


# Create a message
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = email
msg['Subject'] = "Python Automation"
body = "Python Automation"
msg.attach(MIMEText(body, 'plain'))

# Add an image attachment (optional)
# img_path = "path/to/your/image.jpg"
# with open(img_path, 'rb') as f:
#     img_data = f.read()
# img = MIMEImage(img_data, name="image.jpg")
# msg.attach(img)

# Add a file attachment (optional)
# file_path = "path/to/your/file.pdf"
# with open(file_path, 'rb') as f:
#     file_data = f.read()
# file = MIMEBase('application', 'octet-stream')
# file.set_payload(file_data)
# encoders.encode_base64(file)
# file.add_header('Content-Disposition', 'attachment', filename="file.pdf")
# msg.attach(file)

# Send the message
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, app_password)
text = msg.as_string()
server.sendmail(email,email, text)
server.quit()
print("Mail sent")
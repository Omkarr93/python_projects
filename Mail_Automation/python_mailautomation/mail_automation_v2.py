import tkinter as tk
import smtplib
from decouple import config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders


email = config("user")
app_password = config("password")
DEBUG = config('DEBUG', default=False, cast=bool)

def send_email():
    # Get the email details from the user
    from_email = email
    to_email = to_entry.get()
    subject = subject_entry.get()
    body = body_entry.get("1.0", tk.END)

    # Send the email
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = from_email
    smtp_password = app_password

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        message = f"From: {from_email}\nTo: {to_email}\nSubject: {subject}\n\n{body}"
        server.sendmail(from_email, to_email, message)

        server.quit()

        status_label.config(text="Email sent successfully!")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

# Create the GUI window
window = tk.Tk()
window.title("Send Email")

# Create the input fields
# from_label = tk.Label(window, text="From:")
# from_label.grid(row=0, column=0)
# from_entry = tk.Entry(window)
# from_entry.grid(row=0, column=1)

to_label = tk.Label(window, text="To:")
to_label.grid(row=1, column=0)
to_entry = tk.Entry(window,width=30)
to_entry.grid(row=1, column=1)

subject_label = tk.Label(window, text="Subject:")
subject_label.grid(row=2, column=0)
subject_entry = tk.Entry(window)
subject_entry.grid(row=2, column=1)

body_label = tk.Label(window, text="Body:")
body_label.grid(row=3, column=0)
body_entry = tk.Text(window, height=10, width=30)
body_entry.grid(row=3, column=1)

# password_label = tk.Label(window, text="Password:")
# password_label.grid(row=4, column=0)
# password_entry = tk.Entry(window, show="*")
# password_entry.grid(row=4, column=1)

send_button = tk.Button(window, text="Send", command=send_email)
send_button.grid(row=5, column=1)

status_label = tk.Label(window, text="")
status_label.grid(row=6, column=1)

# Start the GUI event loop
window.mainloop()

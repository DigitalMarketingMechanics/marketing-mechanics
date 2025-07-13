import csv
import smtplib
from email.message import EmailMessage

# Replace with your own email config
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'

def load_leads(file_path):
    with open(file_path, newline='') as csvfile:
        return list(csv.DictReader(csvfile))

def load_template(file_path):
    with open(file_path) as f:
        return f.read()

def send_email(to_email, subject, content):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg.set_content(content)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def main():
    leads = load_leads('leads.csv')
    template = load_template('email_template.txt')

    for lead in leads:
        personalized = template.replace('{{name}}', lead['name'])
        send_email(lead['email'], 'A Quick Tip from DMM', personalized)
        print(f"Sent email to {lead['name']} at {lead['email']}")

if __name__ == '__main__':
    main()

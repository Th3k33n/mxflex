import asyncio
from aiosmtpd.controller import Controller
from aiosmtpd.smtp import SMTP as SMTPServer
import dns.resolver
import smtplib
import socket
import argparse
import sys

class EmailValidator:
    def __init__(self, sender_email):
        self.sender_email = sender_email

    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        if self.validate_email(address):
            envelope.rcpt_tos.append(address)
            return '250 OK'
        return '550 Invalid email address'

    def validate_email(self, email):
        domain = email.split('@')[1]
        try:
            answers = dns.resolver.resolve(domain, 'MX')
            mx_record = str(answers[0].exchange)
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            return False

        try:
            with smtplib.SMTP(mx_record, timeout=10) as server:
                server.set_debuglevel(0)
                server.ehlo()
                if server.has_extn('STARTTLS'):
                    server.starttls()
                    server.ehlo()
                server.mail(self.sender_email)
                code, message = server.rcpt(email)
                return code == 250
        except (smtplib.SMTPException, socket.error) as e:
            print(f"Error validating {email}: {str(e)}")
            return False

def validate_emails(emails, sender_email):
    validator = EmailValidator(sender_email)
    results = {}
    for email in emails:
        email = email.strip()  # Remove any leading/trailing whitespace
        if email:  # Skip empty lines
            is_valid = validator.validate_email(email)
            results[email] = "Valid" if is_valid else "Invalid"
    return results

async def amain(loop):
    controller = Controller(EmailValidator("sender@yourdomain.com"), hostname='127.0.0.1', port=1025)
    controller.start()

def main():
    parser = argparse.ArgumentParser(description='Validate email addresses')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--email', help='Single email address to validate')
    group.add_argument('-f', '--file', help='File containing list of email addresses')
    parser.add_argument('-s', '--sender', default='sender@yourdomain.com', help='Sender email address for validation')
    
    args = parser.parse_args()

    if args.email:
        emails = [args.email]
    elif args.file:
        try:
            with open(args.file, 'r') as file:
                emails = file.readlines()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            sys.exit(1)

    results = validate_emails(emails, args.sender)
    
    for email, status in results.items():
        print(f"{email}: {status}")

if __name__ == '__main__':
    main()
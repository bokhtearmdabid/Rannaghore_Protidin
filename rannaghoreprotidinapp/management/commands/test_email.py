from django.core.management.base import BaseCommand
from utils.email_service import send_simple_email


class Command(BaseCommand):
    help = 'Test email configuration'

    def handle(self, *args, **kwargs):
        result = send_simple_email(
            subject='Test Email from Django',
            message='If you receive this, your email setup is working!',
            recipient_list=['test@example.com']  # Replace with your email
        )

        if result:
            self.stdout.write(self.style.SUCCESS('Email sent successfully!'))
        else:
            self.stdout.write(self.style.ERROR('Failed to send email'))
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_simple_email(subject, message, recipient_list):
    """Send a simple text email"""
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def send_html_email(subject, template_name, context, recipient_list):
    """Send an HTML email using a template"""
    try:
        html_content = render_to_string(template_name, context)
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=recipient_list
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        return True
    except Exception as e:
        print(f"Error sending HTML email: {e}")
        return False


def send_email_with_attachment(subject, message, recipient_list, file_path):
    """Send an email with attachment"""
    try:
        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=recipient_list
        )
        email.attach_file(file_path)
        email.send()
        return True
    except Exception as e:
        print(f"Error sending email with attachment: {e}")
        return False
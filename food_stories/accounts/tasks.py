from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from accounts.tools.tokens import account_activation_token
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model
from django.conf import settings

USER_MODEL = get_user_model()

def send_confirmation_email(current_site, user_id):
    user = USER_MODEL.objects.get(id=user_id)
    subject = 'Activate Your MySite Account'
    message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, to=(user.email,))
    email.content_subtype = 'html'
    email.send()


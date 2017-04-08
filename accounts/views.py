from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib import messages, auth

from accounts.models import Token


def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
            reverse('login') + '?token=' + str(token.uid)
            )
    message_body = f'Use this link to login:\n\n{url}'
    send_mail(
            'Your login link for Superlists',
            message_body,
            'noreply@superlists',
            [email]
        )
    messages.success(
            request,
            "Check your email, we've send you a link your can use to login."
            )
    return redirect('/')

def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')


'''
dripemail utils
'''
import json

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def get_user_model():
    '''
    get user model
    '''
    # handle 1.7 and back
    try:
        from django.conf import settings
        User = settings.AUTH_USER_MODEL
    except ImportError:
        from django.contrib.auth.models import User
    return User


def dumps(value):
    return json.dumps(value, default=lambda o: None)


def get_model(model_name):
    model = None
    try:
        from django.db.models.loading import get_model
        model = get_model('dripemail', '%s' % model_name)
    except Exception, e:
        try:
            from django.apps import apps
            model = apps.get_model('dripemail', '%s' % model_name)
        except Exception, e:
            print e
        print e
    return model


def save_request(request):
    '''
    save request session for analytics
    '''
    meta = request.META.copy()
    meta.pop('QUERY_STRING', None)
    meta.pop('HTTP_COOKIE', None)
    remote_addr_fwd = None

    if 'HTTP_X_FORWARDED_FOR' in meta:
        remote_addr_fwd = meta[
            'HTTP_X_FORWARDED_FOR'].split(",")[0].strip()
        if remote_addr_fwd == meta['HTTP_X_FORWARDED_FOR']:
            meta.pop('HTTP_X_FORWARDED_FOR')
    uri = request.build_absolute_uri()
    WebRequest = get_model('WebRequest')
    webrequest = WebRequest(
        host=request.get_host(),
        path=request.path,
        uri=request.build_absolute_uri(),
        user_agent=meta.pop('HTTP_USER_AGENT', None),
        remote_addr=meta.pop('REMOTE_ADDR', None),
        remote_addr_fwd=remote_addr_fwd,
        meta=None if not meta else dumps(meta),
    )
    webrequest.save()
    return webrequest


def hashid(hashid, reverse=False):
    '''
    convert the hashid to an id or reverse
    '''
    if reverse:
        try:
            return str(self.pk ^ 0xABCDEFAB)
        except Exception, e:
            print e
    else:
        pk = None
        try:
            hashid = int(hashid)
            pk = str(hashid ^ 0xABCDEFAB)
        except Exception, e:
            print e
        return pk


def get_messages():
    '''
    get messages framework or resort to plan b
    '''
    messages = None
    try:
        from django.contrib import messages
    except Exception, e:
        pass
    return messages

#@background(schedule=20)


def send_email(subject, text_content, sender, receipient, html_content):
    '''schedule email sending'''
    msg = EmailMultiAlternatives(subject, text_content, sender, [receipient])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print "Mail sent to %s from %s" % (receipient, sender)


def mailer(to, subject, template, data, sender=None):
    '''
    send cron mail
    does not require request
    '''
    html_content = render_to_string(template, data)
    text_content = strip_tags(html_content)
    send_email(subject, text_content, sender, to, html_content)

'''
djangodrip utils
'''
import json


def get_user_model():
    '''
    get user model
    '''
    # handle 1.7 and back
    try:
        from django.contrib.auth import get_user_model as django_get_user_model
        User = django_get_user_model()
    except ImportError:
        from django.contrib.auth.models import User
    return User


def dumps(value):
    return json.dumps(value, default=lambda o: None)


def save_request(request, response):
    '''
    save request session for analytics
    '''
    User = get_user_model()
    if hasattr(request, 'user'):
        user = request.user if type(request.user) == User else None
    else:
        user = None

    meta = request.META.copy()
    meta.pop('QUERY_STRING', None)
    meta.pop('HTTP_COOKIE', None)
    remote_addr_fwd = None

    if 'HTTP_X_FORWARDED_FOR' in meta:
        remote_addr_fwd = meta[
            'HTTP_X_FORWARDED_FOR'].split(",")[0].strip()
        if remote_addr_fwd == meta['HTTP_X_FORWARDED_FOR']:
            meta.pop('HTTP_X_FORWARDED_FOR')

    post = None
    uri = request.build_absolute_uri()
    if request.POST and uri != '/login/':
        post = dumps(request.POST)

    models.WebRequest(
        host=request.get_host(),
        path=request.path,
        method=request.method,
        uri=request.build_absolute_uri(),
        status_code=response.status_code,
        user_agent=meta.pop('HTTP_USER_AGENT', None),
        remote_addr=meta.pop('REMOTE_ADDR', None),
        remote_addr_fwd=remote_addr_fwd,
        meta=None if not meta else dumps(meta),
        cookies=None if not request.COOKIES else dumps(request.COOKIES),
        get=None if not request.GET else dumps(request.GET),
        post=None if (not request.POST or getattr(
            request, 'hide_post') == True) else dumps(request.POST),
        raw_post=None if getattr(
            request, 'hide_post') else request.raw_post_data,
        is_secure=request.is_secure(),
        is_ajax=request.is_ajax(),
        user=user
    ).save()

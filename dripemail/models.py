from __future__ import unicode_literals
from django.db import models
from dripemail.utils import get_user_model
from .widgets import ColorPickerWidget
User = get_user_model()
# Create your models here.


class WebRequest(models.Model):

    '''
    store WebRequest for analytics
    '''
    time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=1000)
    path = models.CharField(max_length=1000)
    method = models.CharField(max_length=50)
    uri = models.CharField(max_length=2000)
    status_code = models.IntegerField()
    user_agent = models.CharField(max_length=1000, blank=True, null=True)
    remote_addr = models.GenericIPAddressField()
    remote_addr_fwd = models.GenericIPAddressField(blank=True, null=True)
    meta = models.TextField()
    cookies = models.TextField(blank=True, null=True)
    get = models.TextField(blank=True, null=True)
    post = models.TextField(blank=True, null=True)
    raw_post = models.TextField(blank=True, null=True)
    is_secure = models.BooleanField()
    is_ajax = models.BooleanField()
    user = models.ForeignKey(
        User, blank=True, null=True
    )


class ColorField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)


class Dripbox(models.Model):

    '''
    configurations for the Dripbox
    '''
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, blank=True, null=True)
    submit_button = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Submit Button text")
    font_color = ColorField(blank=True, verbose_name="Font Color")
    body_color = ColorField(blank=True, verbose_name="Body Color")
    require_name = models.BooleanField(
        default=False, verbose_name="Require Name")

    def __unicode__(self):
        _str = self.title
        if len(_str) < 1:
            _str = "DripBox"
        return unicode(_str)

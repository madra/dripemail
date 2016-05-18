from __future__ import unicode_literals
from django.db import models
from dripemail.utils import get_user_model, hashid

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
    user_agent = models.CharField(max_length=1000, blank=True, null=True)
    remote_addr = models.GenericIPAddressField()
    remote_addr_fwd = models.GenericIPAddressField(blank=True, null=True)
    meta = models.TextField()


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
    subscribe_message = models.CharField(
        max_length=1000, blank=True, null=True)
    unsubscribe_message = models.CharField(
        max_length=1000, blank=True, null=True)
    success_message = models.CharField(
        max_length=1000, blank=True, null=True)

    def __unicode__(self):
        _str = self.title
        if len(_str) < 1:
            _str = "DripBox"
        return unicode(_str)


class Lead(models.Model):

    '''
    lead from lead-capture box
    '''
    dripbox = models.ForeignKey(
        Dripbox,
        related_name="lead_capture_box",
    )
    request = models.ForeignKey(
        WebRequest, blank=True, null=True)
    email = models.EmailField(
        help_text='user email.')
    name = models.CharField(
        max_length=1000,
        verbose_name="Lead Name",
        blank=True,
        null=True
    )
    added = models.DateTimeField(auto_now_add=True)
    subscribed = models.BooleanField(
        default=False, verbose_name="Subcription Confirmed")
    subscribed_when = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ("email", "dripbox", )

    def subscribe_url(self):
        hashedid = hashid(
            self.pk,
            reverse=True
        )
        return ('subscribe_url', ({hashedid}))

    def unsubscribe_url(self):
        hashedid = hashid(
            self.pk,
            reverse=True
        )
        return ('unsubscribe_url', ({hashedid}))

    def __unicode__(self):
        _str = self.email
        subed = 'Not subscribed'
        if self.subscribed:
            subed = "Subscribed"
        _str = "%s [%s]" % (
            _str,
            subed
        )
        return unicode(_str)

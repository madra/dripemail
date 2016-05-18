'''
color picker
'''
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe


class ColorPickerWidget(forms.TextInput):

    class Media:
        css = {
            'all': (
                settings.STATIC_URL + 'admin/dripemail/css/colorpicker.css',
                settings.STATIC_URL + 'admin/dripemail/css/layout.css',
            )
        }
        js = (

            settings.STATIC_URL + 'admin/dripemail/js/jquery.js',
            settings.STATIC_URL + 'admin/dripemail/js/colorpicker.js',
            settings.STATIC_URL + 'admin/dripemail/js/eye.js',
            settings.STATIC_URL + 'admin/dripemail/js/utils.js',
            settings.STATIC_URL + 'admin/dripemail/js/layout.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(ColorPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(ColorPickerWidget, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript"> jQuery(document).ready(function($) {$('#id_%s').ColorPicker({
    color: '#0000ff',
    onShow: function (colpkr) {
        $(colpkr).fadeIn(500);
        return false;
    },
    onHide: function (colpkr) {
        $(colpkr).fadeOut(500);
        return false;
    },
    onChange: function (hsb, hex, rgb) {
        $('#id_%s').val('#' + hex);
    }
});
        })
            </script>''' % (name, name))

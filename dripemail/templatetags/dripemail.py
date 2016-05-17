from django.template.defaulttags import register
import os
from django.template import Library, loader, Context
from django.template import RequestContext


@register.simple_tag(takes_context=True)
def dripbox(context, title=False):
    #context = RequestContext(request)
    request = context['request']
    font_color = body_color = description = submit_button = None
    require_name = False
    uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
    template_name = "%s/templates/dripbox.html" % uppath(__file__, 2)
    static_dir = "%s/static/" % uppath(__file__, 2)
    t = loader.get_template(template_name)
    try:
        from django.db.models.loading import get_model
        Dripbox = get_model('dripemail', 'Dripbox')
    except Exception, e:
        try:
            from django.apps import apps
            Dripbox = apps.get_model('dripemail', 'Dripbox')
        except Exception, e:
            print e
        print e

    try:
        dripbox = Dripbox.objects.all()[:1][0]
        font_color = dripbox.font_color
        body_color = dripbox.body_color
        description = dripbox.description
        submit_button = dripbox.submit_button
        require_name = dripbox.require_name
        if not title:
            title = dripbox.title
    except Exception, e:
        print e
    return t.render({
        'title': title,
        'font_color': font_color,
        'body_color': body_color,
        'description': description,
        'submit_button': submit_button,
        'require_name': require_name,
    }, request)


"""
@register.inclusion_tag('dripemail/dripbox.html')
def dripbox(title=False):
    return {'title': title}
"""

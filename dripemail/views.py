from django.template import RequestContext
from django.shortcuts import render_to_response, HttpResponseRedirect
from .models import Dripbox
from .utils import save_request, get_model, hashid, get_messages
from django.utils import timezone


def render_view(request, template, data):
    '''
    wrapper for rendering views , loads RequestContext
    @request  request object
    @template  string
    @data  tumple
    '''
    return render_to_response(
        template, data,
        context_instance=RequestContext(request)
    )


def add_dripemail(request):
    '''
    add leads from leadcapture box
    '''
    if request.POST:
        data = request.POST.copy()
        email = data.get('email', None)
        name = data.get('name', None)
        if email:
            Lead = get_model('Lead')
            Dripbox = get_model('Dripbox')
            dripbox = Dripbox.objects.all()[:1][0]
            lead = Lead(
                dripbox=dripbox,
                email=email,
                name=name
            )
            lead.save()
            webrequest = save_request(request)
            if webrequest:
                lead.request = webrequest
                lead.save()
                request.session['new_dripemail'] = True
            messages = get_messages()
            if messages:
                messages.success(
                    request,
                    dripbox.success_message
                )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def subscribe(request, name):
    pk = hashid(name)
    try:
        Lead = get_model('Lead')
        lead = Lead.objects.get(pk=pk)
        lead.subscribe = True
        lead.subscribed_when = timezone.now()
        lead.save()
        Dripbox = get_model('Dripbox')
        dripbox = Dripbox.objects.all()[:1][0]
        messages = get_messages()
        if messages:
            messages.success(
                request,
                dripbox.subscribe_message
            )
    except Exception, e:
        print e
    return HttpResponseRedirect('/')


def unsubscribe(request, name):
    pk = hashid(name)
    try:
        Lead = get_model('Lead')
        lead = Lead.objects.get(pk=pk)
        lead.subscribe = False
        lead.save()
        Dripbox = get_model('Dripbox')
        dripbox = Dripbox.objects.all()[:1][0]
        messages = get_messages()
        if messages:
            messages.success(
                request,
                dripbox.unsubscribe_message
            )
    except Exception, e:
        print e
    return HttpResponseRedirect('/')

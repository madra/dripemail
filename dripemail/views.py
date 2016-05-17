from django.template import RequestContext
from django.shortcuts import render_to_response


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
    return render_view(
        request,
        'index.html',
        {}
    )

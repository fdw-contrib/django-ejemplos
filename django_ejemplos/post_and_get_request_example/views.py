# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def post_view(request):
    context = RequestContext(request)
    data = {}
    if request.method == "POST":
        template_name = "post_request_result.html"
        data['result'] = request.POST.get("word")
    elif request.method == "GET":
        template_name = "post_request_form.html"
    return render_to_response(template_name, data, context_instance=context)

def get_view(request):
    context = RequestContext(request)
    data = {}
    template_name = "get_request_form.html"
    if request.method == "GET" and "word" in request.GET:
        data['result'] = request.GET["word"]
        template_name = "get_request_result.html"
    return render_to_response(template_name, data, context_instance=context)

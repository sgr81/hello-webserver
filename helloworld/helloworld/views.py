from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello world from Django!\n", content_type='text/plain')

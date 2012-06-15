from django.views.generic.simple import direct_to_template

#from django.http import HttpResponse

def homepage(request):
    return direct_to_template(request, 'index.html', locals())
    #return HttpResponse("Hello, world. You're at the poll index.")
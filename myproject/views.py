"""Project views"""
#Django
from django.http import HttpResponse
import json

def hello_world(request):
    return HttpResponse('hola mundo')

def sort(request):
    numbers =[int(i) for i in request.GET['numbers'].split(',')]
    num_ord=sorted(numbers)
    data = {
        'status':'ok',
        'numbers': num_ord,
        'message':'sorted numbers successfully.'

    } 
    return HttpResponse(json.dumps(data),content_type='application/json')
def say_hi(request,name,age):
    if age < 12:
        message='Sorry {} you aren\'t allowed here'.format(name)
    else:
        message='Hi {}'.format(name)
    return HttpResponse(message)
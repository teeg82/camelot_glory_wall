from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def glory_wall_post(request):
    if request.method == "POST":
        print "Request was: %s" % str(request.POST)
        return HttpResponse("Glory wall post successfully submitted!!")
    else:
        return HttpResponse("Glory wall: There's nothing to do here")

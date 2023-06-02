from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant

# Create your views here.
def homepage(request):
    if request.method == "GET":
        restaurants = Restaurant.objects.all()
        context = {"restaurants": restaurants}
        return render(request, "index.html", context)
    else:
        return HttpResponse("Invalid, only GET method is allowed")
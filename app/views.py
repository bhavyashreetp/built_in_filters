from django.shortcuts import render

# Create your views here.
def built_in_filters(request):
    d={'data':'TODAY is weekend','d':1}
    return render(request,'built_in_filters.html',d)

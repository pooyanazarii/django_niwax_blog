
from django.shortcuts import render, get_object_or_404

def upgrating_view1(request):
    return render(request, "upgreat.html")

def upgrating_view(request, exception):
    context = {}
    response = render(request, "upgreat.html", context=context)
    response.status_code = 404
    return response
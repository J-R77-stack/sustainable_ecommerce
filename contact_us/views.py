from django.shortcuts import render

from django.http import HttpResponse


def contact_view(request):
    return render(request, 'contact_us/contact_us.html')

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Unit

def index(request):
    latest_unit_list = Unit.objects.order_by('-mfg_date')[:5]
    context = {
        'latest_unit_list': latest_unit_list,
    }
    return render(request, 'assets/index.html', context)

def units(request, unit_id):
    latest_unit_list = Unit.objects.order_by('-mfg_date')[:5]
    output = ', '.join([u.id for u in latest_units_list])
    return HttpResponse(output)

def modules(request, module_id):
    return HttpResponse("You're looking at module %s" % module_id)

    

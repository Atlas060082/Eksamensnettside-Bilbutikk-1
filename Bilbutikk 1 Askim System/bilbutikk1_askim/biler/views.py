from django.shortcuts import render, get_object_or_404
from .models import Bil, Service

def oversikt(request):
    biler = Bil.objects.all()
    
    innkommet = biler.filter(status='innkommet').count()
    under_service = biler.filter(status='under_service').count()
    klar_salg = biler.filter(status='klar_salg').count()
    solgt = biler.filter(status='solgt').count()
    
    context = {
        'biler': biler,
        'statistikk': {
            'innkommet': innkommet,
            'under_service': under_service,
            'klar_salg': klar_salg,
            'solgt': solgt,
            'totalt': biler.count()
        }
    }
    return render(request, 'biler/oversikt.html', context)

def bildetaljer(request, bil_id):
    bil = get_object_or_404(Bil, id=bil_id)
    servicer = bil.servicer.all()
    
    context = {
        'bil': bil,
        'servicer': servicer,
        'aktive_servicer': servicer.filter(fullført=False),
        'fullførte_servicer': servicer.filter(fullført=True)
    }
    return render(request, 'biler/bildetaljer.html', context)

def serviceoversikt(request):
    ventende = Service.objects.filter(fullført=False).order_by('planlagt_dato')
    fullført = Service.objects.filter(fullført=True).order_by('-fullført_dato')[:20]
    
    context = {
        'ventende_servicer': ventende,
        'fullførte_servicer': fullført
    }
    return render(request, 'biler/serviceoversikt.html', context)
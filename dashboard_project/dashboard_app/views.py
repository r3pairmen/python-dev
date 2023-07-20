from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from .models import DataEntry

def get_filtered_data(request):
    # Get filter parameters from the request
    end_year = request.GET.get('end_year')
    topics = request.GET.getlist('topics')
    sector = request.GET.get('sector')
    region = request.GET.get('region')
    pestle = request.GET.get('pestle')
    source = request.GET.get('source')
    swot = request.GET.get('swot')
    country = request.GET.get('country')
    city = request.GET.get('city')

    # Build the queryset based on the filter parameters
    queryset = DataEntry.objects.all()

    if end_year:
        queryset = queryset.filter(end_year=end_year)
    
    if topics:
        queryset = queryset.filter(topics__in=topics)
    
    if sector:
        queryset = queryset.filter(sector=sector)
    
    if region:
        queryset = queryset.filter(region=region)
    
    if pestle:
        queryset = queryset.filter(pestle=pestle)
    
    if source:
        queryset = queryset.filter(source=source)
    
    if swot:
        queryset = queryset.filter(swot=swot)
    
    if country:
        queryset = queryset.filter(country=country)
    
    if city:
        queryset = queryset.filter(city=city)

    # Serialize the queryset into JSON
    serialized_data = [
        {
            'intensity': entry.intensity,
            'likelihood': entry.likelihood,
            'relevance': entry.relevance,
            'country': entry.country,
            'topics': entry.topics,
            'region': entry.region,
            'city': entry.city,
            'end_year': entry.end_year,
            'start_year': entry.start_year,
            'insight': entry.insight,
            'url': entry.url,
            'impact': entry.impact,
            'added': entry.added,
            'published': entry.published,
            'pestle': entry.pestle,
            'source': entry.source,
            'title': entry.title
        }
        for entry in queryset
    ]

    return JsonResponse(serialized_data, safe=False)


from django.shortcuts import render
from facts.models import Fact


def home_page(request):
    facts = Fact.objects.all()

    return render(request, 'facts/home.html', {
        "facts": facts
    })

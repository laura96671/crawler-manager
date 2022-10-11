from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView

from .models import CrawlerManager

from datetime import datetime

provider_field_mapper = {"yFinance": ["ticker", {"interval": ["1m", "5m"]}],
                         "aVantage": ["ticker", {"endpoint": ["Intraday", "Daily"]}],
                         "finviz": ["ticker"]}


def table_data_db(request):
    template_name = "crawler_homepage.html"
    history_table = CrawlerManager.objects.all().order_by("-created_on")
    context = {"fields": provider_field_mapper,
               "providers": list(provider_field_mapper.keys()),
               "history_table": history_table}

    if request.method == "POST":
        provider = request.POST.get("provider")

        if provider in provider_field_mapper:
            params = {k: v for k, v in request.POST.items() if k not in ["provider", "csrfmiddlewaretoken"]}
            CrawlerManager.objects.create(name=provider, params=params, created_on=datetime.now())

            return HttpResponseRedirect(reverse("homepage"), context)

        else:
            print("The provider selected is not allowed.")

    return render(request, template_name, context)


class DataDelete(DeleteView):
    model = CrawlerManager
    success_url = reverse_lazy("homepage")

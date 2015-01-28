from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf

from userregistry.forms import TorUserModelForm


def index(request):
    data = {}
    data.update(csrf(request))

    human = False

    if request.POST:
        form = TorUserModelForm(request.POST)

        if form.is_valid():
            human = True
    else:
        form = TorUserModelForm()

    data["form"] = form
    data["human"] = human

    return render_to_response('userregistry/index.html', data)

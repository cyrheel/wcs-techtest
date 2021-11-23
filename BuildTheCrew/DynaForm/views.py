from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Argonaute
from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data
            new_name = str(form['your_name'].value())
            a = Argonaute.objects.create(
                argo_name=new_name,
                add_date=timezone.now()
            )
            a.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/index/')
        else:
            # redisplay the blank form and the last added
            latest_argonaute_list = Argonaute.objects.order_by('-add_date')[:15]
            argo_list5 = latest_argonaute_list[:5]
            argo_list10 = latest_argonaute_list[5:10]
            argo_list15 = latest_argonaute_list[10:]
            form = NameForm()
            context = {
                'form': form,
                'latest_argonaute_list': latest_argonaute_list,
                'argo_list5': argo_list5,
                'argo_list10': argo_list10,
                'argo_list15': argo_list15,
            }

            return render(request, 'DynaForm/index.html', context)

    # if a GET (or any other method) we'll create a blank form and display the last added
    else:
        latest_argonaute_list = Argonaute.objects.order_by('-add_date')[:15]
        argo_list5 = latest_argonaute_list[:5]
        argo_list10 = latest_argonaute_list[5:10]
        argo_list15 = latest_argonaute_list[10:]
        form = NameForm()
        context = {
            'form': form,
            'latest_argonaute_list': latest_argonaute_list,
            'argo_list5': argo_list5,
            'argo_list10': argo_list10,
            'argo_list15': argo_list15,
        }

        return render(request, 'DynaForm/index.html', context)

from inspect import getmembers

from django.shortcuts import render

from utilities import get_wps_service_engine, list_wps_service_engines, abstract_is_link


def home(request):
    """
    Home page for Tethys WPS tool. Lists all the WPS services that are linked.
    """
    wps_services = list_wps_service_engines()

    context = {'wps_services': wps_services}

    return render(request, 'tethys_wps/home.html', context)


def service(request, service):
    """
    View that lists the processes for a given service.
    """

    wps = get_wps_service_engine(service)

    context = {'wps': wps,
               'service': service}

    return render(request, 'tethys_wps/service.html', context)


def process(request, service, identifier):
    """
    View that displays a detailed description for a WPS process.
    """
    wps = get_wps_service_engine(service)
    wps_process = wps.describeprocess(identifier)

    context = {'process': wps_process,
               'service': service,
               'is_link': abstract_is_link(wps_process)}

    return render(request, 'tethys_wps/process.html', context)

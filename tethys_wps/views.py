from django.shortcuts import render


def home(request):
    """
    Home page for Tethys Datasets
    """
    context = {}

    return render(request, 'tethys_datasets/home.html', context)

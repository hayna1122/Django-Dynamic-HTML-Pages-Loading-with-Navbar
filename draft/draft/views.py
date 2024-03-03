from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def profile(request):
    return render(request, 'profile.html')

def orders(request):
    return render(request, 'orders.html')

def payments(request):
    return render(request, 'payments.html')

def records(request):
    return render(request, 'records.html')

def charts(request):
    return render(request, 'charts.html')
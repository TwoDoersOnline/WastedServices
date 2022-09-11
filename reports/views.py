from django.shortcuts import render


def dex(request):
    return render(request, 'index.html')

def reports(request):
    return render(request, 'reports/reports.html', {})
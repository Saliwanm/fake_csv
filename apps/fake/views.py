from django.shortcuts import render


def fake(request):
    return render(request, "fake/fakecsv.html")

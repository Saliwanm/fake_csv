from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def sign_in(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request, user)
            return redirect("fake")
        return redirect("/")
    else:
        return render(request, "main/sign_in.html")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")
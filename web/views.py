from django.shortcuts import render
from .forms import Theme
# Create your views here.


def page(request):
    if request.method == 'POST':
        form = Theme(request.POST)
        if form.is_valid():
            request.session["dark"] = form.cleaned_data['checkbox']
            return render(request, "web/landing.html", {"form": form, "dark": form.cleaned_data['checkbox']})
        else:
            print(form.errors)
    else:
        form = Theme(initial={'checkbox': request.session.get("dark")})
    print("dios")
    return render(request, "web/landing.html", {"form": form, "dark": request.session.get("dark")})

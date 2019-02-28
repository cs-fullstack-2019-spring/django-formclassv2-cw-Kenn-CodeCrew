from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeApplicationForm


# Create your views here.
def index(request):
    newForm = EmployeeApplicationForm
    context = {
        "form": newForm,
    }

    return render(request, "EmployeeAppApp/index.html", context)


def gotThatInfo(request):
    print(request.POST)

    context = {
        "name": request.POST["name"],
        "dateOfBirth": request.POST["dateOfBirth"],
        "position": request.POST["position"],
        "salary": request.POST["salary"],
    }

    return render(request, "EmployeeAppApp/gotThatInfo.html", context)
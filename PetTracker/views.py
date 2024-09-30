from django.shortcuts import render, redirect
from PetTracker.forms import PetForm, OrgForm, FosterForm

# Create your views here.


def index(request):
    return render(request, 'index.html')

def viewPet(request):
    return render(request, 'viewpets.html')

def petSubmit(request):
    return render(request, 'petsubmit.html')

def orgSubmit(request):
    return render(request, 'orgsubmit.html')

def fosterSubmit(request):
    return render(request, 'fostersubmit.html')

def addPet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the pet form data to the database
            return redirect('petsubmit')
        else:
            form = PetForm()
    context = {'petFormKey': form}
    return render(request, 'addpet.html', context)


def addOrg(request):
    if request.method == 'POST':
        form = OrgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the pet form data to the database
            return redirect('orgsubmit')
        else:
            form = PetForm()
    context = {'orgFormKey' : form}
    return render(request, 'addorg.html', context)

def addFoster(request):
    if request.method == 'POST':
        form = FosterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the pet form data to the database
            return redirect('fostersubmit')
        else:
            form = PetForm()
    context = {'fosterFormKey' : form}
    return render(request, 'addfoster.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from PetTracker.forms import PetForm, OrgForm, FosterForm
from .models import Pet, Foster, Organization

# Create your views here.

def index(request):
    return render(request, 'index.html')


def viewPet(request):
    pets = Pet.objects.all()
    return render(request, 'viewpets.html', {'pets':pets})

def petDetail(request, petID):
    pet = get_object_or_404(Pet, pk=petID)
    return render(request, 'petdetail.html', {'pet':pet})

def viewFoster(request):
    fosters = Foster.objects.all()   
    return render(request, 'viewfosters.html', {'fosters':fosters})

def fosterDetail(request, fosterID):
    foster = get_object_or_404(Foster, pk=fosterID)
    fostering = Pet.objects.filter(petFoster=fosterID)
    return render(request, 'fosterdetail.html', {'foster':foster, 'fostering':fostering,})

def viewOrg(request):
    organizations = Organization.objects.all()
    return render(request, 'vieworgs.html', {'organizations':organizations})

def orgDetail(request, orgID):
    org = get_object_or_404(Organization, pk=orgID)
    current = Pet.objects.filter(petOrganization=orgID)
    return render(request, 'orgdetail.html', {'org':org, 'current':current})




def addPet(request):
    form = PetForm()
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
    form = OrgForm()
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
    form = FosterForm()
    if request.method == 'POST':
        form = FosterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the pet form data to the database
            return redirect('fostersubmit')
        else:
            form = PetForm()
    context = {'fosterFormKey' : form}
    return render(request, 'addfoster.html', context)

def petsubmit(request):
    return render(request, 'petsubmit.html')

def orgsubmit(request):
    return render(request, 'orgsubmit.html')

def fostersubmit(request):
    return render(request, 'fostersubmit.html')
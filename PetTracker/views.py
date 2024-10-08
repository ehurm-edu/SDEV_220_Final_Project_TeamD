from django.shortcuts import render, redirect, get_object_or_404
from PetTracker.forms import PetForm, OrgForm, FosterForm, ImagesForm, FilesForm
from .models import Pet, Foster, Organization, File_Upload, Image_Upload

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
    return render(request, 'fosterdetail.html', {'foster':foster})

def viewOrg(request):
    organizations = Organization.objects.all()
    return render(request, 'vieworgs.html', {'organizations':organizations})

def orgDetail(request, orgID):
    org = get_object_or_404(Organization, pk=orgID)
    return render(request, 'orgdetail.html', {'org':org})




def addPet(request):
    form = PetForm()
    file_form = FilesForm()
    image_form = ImagesForm()
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        file_form = FilesForm(request.POST, request.FILES)
        records = request.FILES.getlist('record')
        image_form = ImagesForm(request.POST, request.FILES)
        pics = request.FILES.getlist('pic')
        
        if form.is_valid() and file_form.is_valid() and image_form.is_valid():
            form.save()  # Save the pet form data to the database
            for r in records:
                record_instance = File_Upload(record=r)
                record_instance.save()
            for p in pics:
                image_instance = Image_Upload(pic=p)
                image_instance.save()
            return redirect('petsubmit')
        else:
            form = PetForm()
            file_form = FilesForm()
            image_form = ImagesForm()
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
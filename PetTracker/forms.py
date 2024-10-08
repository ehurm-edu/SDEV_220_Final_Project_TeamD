from django import forms
from PetTracker.models import Pet, Foster, Organization


#This entire thing might be unncessary

typeSelection = [('cat','Cat'), ('dog', 'Dog'), ('other','Other')]
sexSelection = [('female','Female'), ('male', 'Male'), ('unknown','Unknown')]
fixSelection = [('no','No'), ('yes', 'Yes'), ('unknown','Unknown')]
statusSelection = [('available','Available'), ('notReady', 'Not Ready Yet'), ('adopted','Already Adopted')]
stateSelection = [('al', 'AL'), ('ak', 'AK'), ('az', 'AZ'), ('ar', 'AR'), ('ca', 'CA'), ('co', 'CO'), ('ct', 'CT'), ('de', 'DE'), ('fl', 'FL'), 
    ('ga', 'GA'), ('hi', 'HI'), ('id', 'ID'), ('il', 'IL'), ('in', 'IN'), ('ia', 'IA'), ('ks', 'KS'), ('ky', 'KY'), ('la', 'LA'), ('me', 'ME'), 
    ('md', 'MD'), ('ma', 'MA'), ('mi', 'MI'), ('mn', 'MN'), ('ms', 'MS'), ('mo', 'MO'), ('mt', 'MT'), ('ne', 'NE'), ('nv', 'NV'), ('nh', 'NH'), 
    ('nj', 'NJ'), ('nm', 'NM'), ('ny', 'NY'), ('nc', 'NC'), ('nd', 'ND'), ('oh', 'OH'), ('ok', 'OK'), ('or', 'OR'), ('pa', 'PA'), ('ri', 'RI'), 
    ('sc', 'SC'), ('sd', 'SD'), ('tn', 'TN'), ('tx', 'TX'), ('ut', 'UT'), ('vt', 'VT'), ('va', 'VA'), ('wa', 'WA'), ('wv', 'WV'), ('wi', 'WI'), 
    ('wy', 'WY')]

'''
class PetForm(forms.Form):
    petMicrochipID = forms.CharField(label="Microchip ID", required=False)
    petName = forms.CharField(widget=forms.TextInput, label="Name")
    petType = forms.ChoiceField(choices=typeSelection, label="Animal Type")
    petSex = forms.ChoiceField(choices=sexSelection, label="Sex")
    petDOB = forms.DateField(widget=forms.SelectDateWidget, label="Date of Birth", required=False)
    petSpayNeuter = forms.ChoiceField(choices=fixSelection,  label="Spayed or Neutered")
    petStatus = forms.ChoiceField(choices=statusSelection, label="Adoption Status")
    petImage = forms.FileField(widget=forms.FileInput, label="Upload Pictures", required=False)
    petRecords = forms.FileField(widget=forms.FileInput, label="Upload Vet Records", required=False)
    petBio=forms.CharField(widget = forms.Textarea, required=False)
    petFoster = forms.ModelChoiceField(queryset=Foster.objects.all(), label="Foster Home", required=False)
    petOrganization = forms.ModelChoiceField(queryset=Organization.objects.all(), label="Organization", required=False)
    
class OrgForm(forms.Form):
    orgName = forms.CharField(widget=forms.TextInput, label="Organization Name")
    orgContact = forms.CharField(widget=forms.TextInput, label ="Primary Contact Name")
    orgStreet = forms.CharField(widget=forms.TextInput, label="Street")
    orgCity = forms.CharField(widget=forms.TextInput, label="City")
    orgState = forms.ChoiceField(choices=stateSelection, label="State")
    orgZip = forms.CharField(widget=forms.NumberInput(attrs={'max':99999}),  label="Zip")
    orgEmail = forms.EmailField(widget=forms.TextInput,label="Email")
    orgPhone = forms.CharField(widget=forms.TextInput, label="Phone Number")
    
class FosterForm(forms.Form):
    fosterName = forms.CharField(widget=forms.TextInput, label = "Name")
    fosterStreet = forms.CharField(widget=forms.TextInput, label = "Street")
    fosterCity = forms.CharField(widget=forms.TextInput, label = "City")
    fosterState = forms.ChoiceField(choices=stateSelection, label="State")
    fosterZip = forms.CharField(widget=forms.NumberInput(attrs={'max':99999}),  label="Zip")
    fosterEmail = forms.EmailField(widget=forms.TextInput,label="Email")
    fosterPhone = forms.CharField(widget=forms.TextInput, label="Phone Number")
'''
    
class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['petMicrochipID', 'petName', 'petType', 'petSex', 'petDOB', 'petSpayNeuter', 'petStatus', 
                  'petImage', 'petRecords', 'petBio', 'petFoster', 'petOrganization']
        
        widgets = {
            'petDOB': forms.SelectDateWidget,
            'petBio': forms.Textarea(attrs={'rows': 4}),
            'petImage': forms.FileInput,
            'petRecords': forms.FileInput,
            }
        
class OrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['orgID','orgName','orgContact','orgStreet','orgCity','orgState','orgZip','orgEmail','orgPhone']
        widgets = {
            'orgState': forms.Select(choices=stateSelection),
            'orgZip': forms.NumberInput(attrs={'max':99999}),
            'orgEmail': forms.EmailInput,
                }
    
class FosterForm(forms.ModelForm):
    class Meta:
        model = Foster
        fields = ['fosterID','fosterName','fosterStreet','fosterCity','fosterState','fosterZip','fosterEmail','fosterPhone']
        widgets = { 
            'fosterState': forms.Select(choices=stateSelection),
            'fosterZip': forms.NumberInput(attrs={'max':99999}),
            'fosterEmail':forms.EmailInput,  
                   }
        
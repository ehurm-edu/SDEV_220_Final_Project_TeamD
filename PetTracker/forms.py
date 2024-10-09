from django import forms
from PetTracker.models import Pet, Foster, Organization

  
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
            'orgZip': forms.NumberInput(attrs={'max':99999}),
            'orgEmail': forms.EmailInput,
                }
    
class FosterForm(forms.ModelForm):
    class Meta:
        model = Foster
        fields = ['fosterID','fosterName','fosterStreet','fosterCity','fosterState','fosterZip','fosterEmail','fosterPhone']
        widgets = { 
            'fosterZip': forms.NumberInput(attrs={'max':99999}),
            'fosterEmail':forms.EmailInput,  
                   }
        
from django import forms
from PetTracker.models import Pet, Foster, Organization


#This entire thing might be unncessary

# typeSelection = [('cat','Cat'), ('dog', 'Dog'), ('other','Other')]
# sexSelection = [('female','Female'), ('male', 'Male'), ('unknown','Unknown')]
# fixSelection = [('no','No'), ('yes', 'Yes'), ('unknown','Unknown')]
# statusSelection = [('available','Available'), ('notReady', 'Not Ready Yet'), ('adopted','Already Adopted')]
# stateSelection = [('al', 'AL'), ('ak', 'AK'), ('az', 'AZ'), ('ar', 'AR'), ('ca', 'CA'), ('co', 'CO'), ('ct', 'CT'), ('de', 'DE'), ('fl', 'FL'), 
#     ('ga', 'GA'), ('hi', 'HI'), ('id', 'ID'), ('il', 'IL'), ('in', 'IN'), ('ia', 'IA'), ('ks', 'KS'), ('ky', 'KY'), ('la', 'LA'), ('me', 'ME'), 
#     ('md', 'MD'), ('ma', 'MA'), ('mi', 'MI'), ('mn', 'MN'), ('ms', 'MS'), ('mo', 'MO'), ('mt', 'MT'), ('ne', 'NE'), ('nv', 'NV'), ('nh', 'NH'), 
#     ('nj', 'NJ'), ('nm', 'NM'), ('ny', 'NY'), ('nc', 'NC'), ('nd', 'ND'), ('oh', 'OH'), ('ok', 'OK'), ('or', 'OR'), ('pa', 'PA'), ('ri', 'RI'), 
#     ('sc', 'SC'), ('sd', 'SD'), ('tn', 'TN'), ('tx', 'TX'), ('ut', 'UT'), ('vt', 'VT'), ('va', 'VA'), ('wa', 'WA'), ('wv', 'WV'), ('wi', 'WI'), 
#     ('wy', 'WY')]
    
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
        
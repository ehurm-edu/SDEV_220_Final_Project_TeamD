from django.db import models


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
    
    # Create your models here.

class Organization(models.Model):
    orgID = models.AutoField(primary_key=True)
    orgName = models.CharField(max_length=50)
    orgContact = models.CharField(max_length=50)
    orgStreet = models.CharField(max_length=50)
    orgCity = models.CharField(max_length=50)
    orgState = models.CharField(choices=stateSelection, max_length=2)
    orgZip = models.CharField(max_length=5)
    orgEmail = models.EmailField(max_length=75)
    orgPhone = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.orgName

class Foster(models.Model):
    fosterID = models.AutoField(primary_key=True)
    fosterName = models.CharField(max_length=50)
    fosterStreet = models.CharField(max_length=50)
    fosterCity = models.CharField(max_length=50)
    fosterState = models.CharField(choices=stateSelection, max_length=2)
    fosterZip = models.CharField(max_length=5)
    fosterEmail = models.EmailField(max_length=70)
    fosterPhone = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.fosterName

class Pet(models.Model):
    petID = models.AutoField(primary_key=True)
    petMicrochipID = models.CharField(max_length=50, blank=True, null=True)
    petName = models.CharField(max_length=50)
    petType = models.CharField(choices=typeSelection, max_length=10)
    petSex = models.CharField(choices=sexSelection, max_length=10)
    petDOB = models.DateField(blank=True, null=True)
    petSpayNeuter = models.CharField(choices=fixSelection, max_length=10)
    petStatus = models.CharField(choices=statusSelection, max_length=15)
    petImage = models.FileField(blank=True, null=True)
    petRecords = models.FileField(blank=True, null=True)
    petBio=models.TextField(max_length=5000, blank=True, null=True)
    petOrganization=models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    petFoster=models.ForeignKey(Foster, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"{self.petName} - {self.petSex} - DOB: {self.petDOB}"
    

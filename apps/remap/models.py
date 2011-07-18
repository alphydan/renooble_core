from django.db import models

class Project(models.Model):

#####
# Address related information
    # rawAddress = models.CharField("Your Address", max_length=255, help_text="Tell us your address or simply your zipcode and country") # User information, mendatory
    # locality = models.CharField(max_length=255, help_text="Your address")
    # streetName = models.CharField(max_length=255, help_text="Your Street", null=True, blank=True)
    # houseNumber = models.CharField(max_length=10, null=True, blank=True)
    locality = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=100)
    # zipcode = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=10, decimal_places=7)
    lng = models.DecimalField(max_digits=10, decimal_places=7)
    hideLocation = models.BooleanField("Want to hide your exact location?", default=True, help_text="We want to protect your privacy. If you select this option, we will not display the exact location of your installation") # User information, mendatory

#####
# General project information
    rawTechnology = models.CharField("Product name", max_length=150, null=True, blank=True, help_text="What is the product name of your installation?")
    installationDate = models.DateField("Installation date", null=True, blank=True, help_text="When did you install your renewable energy installation?") # User information, mendatory
    installedPower = models.DecimalField("Power rating", max_digits=7, decimal_places=4, help_text="What is the power rating in kilo watt (kW) of your installation?") # in kW User information, mendatory
    AEP = models.DecimalField("Annual energy production (AEP)", max_digits=10, decimal_places=4, null=True, blank=True, help_text="What is the annual energy production (AEP) of your installation? Only answer if your installation is running more than one year.") # in kWh User information, voluntary
    installationCosts = models.DecimalField("Installation costs", max_digits=10, decimal_places=4, null=True, blank=True, help_text="How much did your installation cost?") 
    TECHNOLOGIES = (
    ('WIND', 'Wind turbine'),
    ('SOLAR', 'Photovoltaic panel'),
    )
    technologyType=models.CharField("Type of installed technology", max_length = 5, choices=TECHNOLOGIES, help_text="What type of renewable energy device have you installed?") # User information, voluntary
    PROJECT_BUILDING = (
    ('UNSP', 'Unspecified'),
    ('PRHO', 'Private House'),
    ('APART', 'Apartment'),
    ('SCHOO', 'School'),
    ('APARC', 'Apartment Complex'),
    ('FARM', 'Farm'),
    ('GOVB', 'Governmental Building'),
    ('OTHER', 'Other'),
    )
    projectBuilding = models.CharField("Property of installation", max_length=10, choices = PROJECT_BUILDING, blank=True, null=True, help_text="On what kind of property did you install the renewable energy device?") # User information, voluntary
    GRID=(
        ('ON', 'Grid Connected'),
        ('OFF', 'Off-Grid / Stand alone'),
        )
    gridConnection = models.CharField("Grid connected?", max_length = 3, choices=GRID, blank=True, null=True, help_text="Is your installation connected to the electric grid?") # User information, voluntary
    SURROUND = (
    ('GDN', 'Garden'),
    ('FLD', 'Field'),
    ('ROF', 'Roof'),
    ('BOT', 'Boat'),
    ('MAR', 'Marina'),
    ('BAL', 'Balcony'),
    )
    surroundings=models.CharField("Surrondings of installation", max_length = 10, choices=SURROUND, blank=True, null=True, help_text="Please describe the surrondings of your installation. This can give other users in your area a good understanding of their possible performance.") # User information, voluntary
    commercialInstallation = models.BooleanField("Commercial installation", default=False, help_text="Is your installation of larger scale (more than 500kW) or do you have a power-purchase agreement with a third-party?") # User information, voluntary

#####
# User information
    # userID = models.ForeignKey(User)
    userEmail = models.EmailField("Contact email", help_text="What is your email address? You can modify your listing by using your email on the renooble website.") # in kW User information, mendatory
    entryDate = models.DateTimeField()  
    agreementToTerms = models.BooleanField("Agreement to terms", default=False, help_text="Please review the terms.") # in kW User information, mendatory

#####
# Misc information
    userComments = models.TextField("Your comments", blank=True, null=True, help_text="Do you have any comments about your installation to share with other interested users? Where you satisfied with your investment?") # in kW User information, voluntary
    adminComments = models.TextField(blank=True, null=True)
    # pic = models.ImageField(upload_to='media/user/photos/', null=True)

#####
# Admin information about the entry
    activationKey = models.CharField(max_length = 30, blank=True)
    activated = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    # reviewer = models.ForeignKey(One of us!!!)
    reviewDate = models.DateField(null=True, blank=True)

    
    def __unicode__(self):
        return self.locality
        # return self.cleanAddress

class WindProject(models.Model):
# Wind Project specific information
    projectID = models.ForeignKey(Project)
#    windID = models.ForeignKey(Windturbine, null=True, blank=True)
    hubHeight = models.IntegerField(null=True, blank=True)



class SolarProject(models.Model):
# Solar Project specific information
    projectID = models.ForeignKey(Project)
#    SolarID = models.ForeignKey(PVModule, null=True, blank=True)
    MOUNTING=(
        ('PLA', 'Planetary'),
        ('HOR', 'Horizontal'),
        ('FIX', 'Fixed'),
        )
    Tracking = models.CharField(max_length= 12, choices=MOUNTING, null=True, blank=True)



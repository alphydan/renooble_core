from django.db import models
from django.utils.translation import ugettext_lazy as _

class Project(models.Model):

#####
# Address related information
    address = models.CharField(_('Complete Address'), max_length=100, 
            null=True, blank=True) 
    locality = models.CharField(_('Location'), max_length=50, null=True, blank=True, 
            help_text=_('Where did you install the renewable energy device?'))
    route = models.CharField(_('Street name'), max_length=50, 
            null=True, blank=True) 
    streetNumber = models.CharField(_('Street number'), max_length=50, 
            null=True, blank=True)
    postalCode= models.CharField(_('Zip code'), max_length=50, 
            null=True, blank=True) 
    state = models.CharField(_('State'), max_length=100, null=True, blank=True, 
            help_text=_('In which state did you install the device?'))
    country = models.CharField(_('Country'), max_length=50, null=True, blank=True,  
            help_text=_('In which country did you install the devide?'))
    locationType = models.CharField(_('Precision'), max_length=50, 
            null=True, blank=True) 
    lat = models.DecimalField(_('Latitude'), max_digits=10, decimal_places=7, 
            help_text=_('What is the latitude of the location?'))
    lng = models.DecimalField(_('Longitude'), max_digits=10, decimal_places=7, 
            help_text=_('What is the longitude of the location?'))
    hideLocation = models.BooleanField("Want to hide your exact location?", default=True, 
            help_text="We want to protect your privacy. If you select this option, " + 
            "we will not display the exact location of your installation") # User information, mendatory

#####
# General project information
    projectName = models.CharField("Project Name", max_length=100, 
            help_text="Please give your installation a name. " + 
            "Your entry will be listed at re.nooble under this name.") # Mandatory info
    projectDescription = models.TextField("Project Description", blank=True, null=True, 
            help_text="Please summarize and describe your project.") # voluntary
    rawTechnology = models.CharField("Product name", max_length=150, null=True, blank=True, 
            help_text="What is the product name of your installation?")
    installationDate = models.DateField("Installation date", null=True, blank=True, 
            help_text="When did you install or commissioning your renewable energy installation?") 
            # User information, mendatory
    installedPower = models.DecimalField("Power rating", max_digits=7, decimal_places=4, 
            help_text="What is the power rating in kilo watt (kW) of your installation?") 
            # in kW User information, mendatory
    AEP = models.DecimalField("Annual energy production in kWh", max_digits=10, decimal_places=4, 
            null=True, blank=True, 
            help_text="What is the annual energy production (AEP) of your installation? "
            +"Only answer if your installation is running more than one year.") 
            # in kWh User information, voluntary
    installationCosts = models.DecimalField("Installation costs", max_digits=10, decimal_places=4, 
            null=True, blank=True, 
            help_text="How much did your installation cost?") 
    RESOURCES = (
            ('WIND', 'Wind power'),
            ('SOLAR', 'Photovoltaic'),
            )
    energyResource=models.CharField("Renewable Resource", max_length = 5, choices=RESOURCES, 
            help_text="What type of renewable energy device have you installed?") 
            # User information, mandatory
    PROJECT_BUILDING = (
            ('PRHO', 'Private House'),
            ('APART', 'Apartment'),
            ('SCHOO', 'School'),
            ('APARC', 'Apartment Complex'),
            ('FARM', 'Farm'),
            ('GOVB', 'Governmental Building'),
            ('BOAT', 'Sail boat or vessel'),
            ('UNSP', 'Unspecified'),
            # ('OTHER', 'Other'),
            )
    projectBuilding = models.CharField("Property of installation", max_length=10, 
            choices = PROJECT_BUILDING, blank=True, null=True, 
            help_text="At what kind of property did you install the renewable energy device?") 
            # User information, voluntary
    GRID=(
            ('ON', 'Grid Connected'),
            ('OFF', 'Off-Grid / Stand alone'),
            )
    gridConnection = models.CharField("Grid connected?", max_length = 3, choices=GRID, 
            blank=True, null=True, 
            help_text="Is your installation connected to the electric grid?") 
            # User information, voluntary
    SURROUND = (
            ('GDN', 'Garden'),
            ('FLD', 'Field'),
            ('ROF', 'Roof'),
            ('BOT', 'Boat'),
            ('MAR', 'Marina environment'),
            ('BAL', 'Balcony'),
            )
    surroundings=models.CharField("Surrondings of installation", max_length = 10, choices=SURROUND,
            blank=True, null=True, 
            help_text="Please describe the surrondings of your installation. "+
            "This can give other users in your area a good understanding of their possible performance.") 
            # User information, voluntary
    commercialInstallation = models.BooleanField("Commercial installation", default=False, 
            help_text="Please check this box if your installation of larger scale (more than 500kW) or " +
            "if you have a power-purchase agreement with a third-party?") # User information, voluntary

#####
# User information
    # userID = models.ForeignKey(User)
    userEmail = models.EmailField("Contact email", 
            help_text="What is your email address? You can modify your listing " +
            "by using your email on the renooble website.") # mandatory, if empty, we create a new user account 
    entryDate = models.DateTimeField()  # automatically set in the views.py
    agreementToTerms = models.BooleanField("Agreement to terms", default=False, 
            help_text="Please review the terms.") # mandatory

#####
# Misc information
    userComments = models.TextField("Your comments", blank=True, null=True, 
            help_text="Do you have any comments about your installation to share with other interested users? " + 
            "Where you satisfied with your investment?") # voluntary
    adminComments = models.TextField(blank=True, null=True) # set by the re.nooble team if necessary, e.g. for mass imported data
    picture = models.ImageField(upload_to='media/user/photos/', null=True, blank=True) # voluntary

#####
# Admin information about the entry
    activationKey = models.CharField(max_length = 30, blank=True, null=True) 
    activated = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False) # set by the re.nooble team after project review
    # reviewer = models.ForeignKey(One of us!!!)
    reviewDate = models.DateField(null=True, blank=True) # set automatically when reviewed


    def __unicode__(self):
        return self.projectName


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
    Tracking = models.CharField(_('Solar Tracking Device'), max_length= 3, choices=MOUNTING, 
            null=True, blank=True, help_text=_('Which type of tracking device is ' + 
                'installed for the solar installation?'))
    avgPeakSun = models.DecimalField(_('Average Peak Sun Hours'), max_digits=6, decimal_places=3, 
            help_text=_('How many hours of sun are available on average?'))
    arrayAzimuth = models.DecimalField(_('Azimuth of Installation'), max_digits=10, decimal_places=7, 
            help_text=_('What is the azimuths of the solar installation?'))
    tiltAngle = models.DecimalField(_('Tilt Angle of Installation'), max_digits=10, decimal_places=7, 
            help_text=_('What is the tilt angle of the solar installation?'))


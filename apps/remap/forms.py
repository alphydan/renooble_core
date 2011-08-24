from django import forms
from django.forms import ModelForm
from django.forms.widgets import RadioSelect
from django.contrib.formtools.wizard import FormWizard
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.sessions.backends.db import SessionStore
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# from api.fields import ModelAutoCompleteField
import datetime

from remap.models import Project

class ReMapLocationForm(ModelForm):
    class Meta:
        model = Project
        fields = (
                'address', 
                'route', 
                'streetNumber', 
                'postalCode', 
                'locality', 
                'state', 
                'country', 
                'lat', 
                'lng', 
                'locationType',
                'energyResource', 
                )
        widgets = {
            'route': forms.HiddenInput(), 
            'streetNumber': forms.HiddenInput(), 
            'postalCode': forms.HiddenInput(), 
            'locality': forms.HiddenInput(), 
            'state': forms.HiddenInput(), 
            'country': forms.HiddenInput(), 
            # 'location_type': forms.HiddenInput(), 
            # 'lat': forms.TextInput(attrs={'disabled':'disabled'}), 
            # 'lng': forms.TextInput(attrs={'disabled':'disabled'}), 
            }

class ReMapProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = (
                'entryDate',
                'adminComments',
                'activationKey',
                'activated', 
                'reviewed',
                'reviewDate',
                )
        widgets = {
                'installationDate': SelectDateWidget(years=range(1980, 2011)), 
                'projectDescription': forms.Textarea, 
                'userComments': forms.Textarea, 
                'locality': forms.TextInput(attrs={'disabled':'disabled'}), 
                'state': forms.TextInput(attrs={'disabled':'disabled'}), 
                'country': forms.TextInput(attrs={'disabled':'disabled'}), 
                'lat': forms.TextInput(attrs={'disabled':'disabled'}), 
                'lng': forms.TextInput(attrs={'disabled':'disabled'}),                
                'energyResource': forms.TextInput(attrs={'disabled':'disabled'}),                
                }

class ReMapUserEditProject(ModelForm):
    class Meta:
        model = Project
        fields = ('projectName', 'projectDescription',  'rawTechnology', 'installationDate', 'installedPower', 'AEP', 'hideLocation', 'picture', 'projectBuilding', 'surroundings', 'gridConnection', 'commercialInstallation', 'userEmail', 'userComments')
        widgets = {'installationDate': SelectDateWidget(years=range(1980, 2011)), 'projectDescription': forms.Textarea, 'userComments': forms.Textarea}


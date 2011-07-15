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
# import hashlib 

from remap.models import Project

class ReMapLocationForm(ModelForm):
    class Meta:
        model = Project
        fields = ('cleanAddress', 'city', 'state', 'country', 'lat', 'lng')

class ReMapProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('cleanAddress', 'city', 'state', 'country', 'lat', 'lng', 'rawTechnology', 'installationDate', 'installedPower', 'AEP', 'hideLocation', 'projectBuilding', 'surroundings', 'gridConnection', 'commercialInstallation', 'userEmail', 'userComments')
        widgets = {'installationDate': SelectDateWidget(years=range(1970, 2011)), 'userComments': forms.Textarea}

class ReMapUserEditProject(ModelForm):
    class Meta:
        model = Project
        fields = ('rawTechnology', 'installationDate', 'installedPower', 'AEP', 'hideLocation', 'projectBuilding', 'surroundings', 'gridConnection', 'commercialInstallation', 'userComments')
        widgets = {'installationDate': SelectDateWidget(years=range(1970, 2011)), 'userComments': forms.Textarea}


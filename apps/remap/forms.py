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
import hashlib 

from reMap.models import Project
from reTech.models import Windturbine
from geoCodeAPI import getLocation

class ReMapNewRawAddressForm(ModelForm):
    class Meta:
        model = Project
        fields = ('rawAddress', 'technologyType')

class ReMapConfirmAddressSelectionForm(forms.Form):
   locations = forms.CharField()

class ReMapMandatoryForm(ModelForm):
    class Meta:
        model = Project
        fields = ('rawTechnology', 'installationDate', 'installedPower', 'AEP', 'hideLocation')
        widgets = {'installationDate': SelectDateWidget(years=range(1970, 2011))}

class ReMapAdditionalProjectInfoForm(ModelForm):
    class Meta:
        model = Project
        fields = ('projectBuilding', 'surroundings', 'gridConnection', 'commercialInstallation')

class ReMapUserInformationForm(ModelForm):
    class Meta:
        model = Project
        fields = ('userEmail', 'userComments')
        widgets = {'userComments': forms.Textarea}

class reMapWizard(FormWizard):

    def render_template(self, request, form, previous_fields, step, context=None):
        if step == 1: 
            location = request.POST.get('0-rawAddress')
            data = getLocation(location)

            # s = SessionStore()
            # s['locations'] = data
            # s.save()

            form.fields['locations'] = forms.ChoiceField(widget=RadioSelect(), choices = [])
            form.fields['locations'].choices = [(data[i]['formatted_address'], data[i]['formatted_address']) for i in range(len(data))]
        return super(reMapWizard, self).render_template(request, form, previous_fields, step, context)

    def done(self, request, form_list):
        # request.session['_ReMapFormList'] = form_list
        instance = Project()
        for form in form_list:
            for field, value in form.cleaned_data.iteritems():
                setattr(instance, field, value)
        data = getLocation(instance.locations)
        instance.lat = str(data[0]['lat'])
        instance.lng = str(data[0]['lng'])
        instance.country = str(data[0]['country'])
        instance.cleanAddress= str(data[0]['formatted_address'])
        instance.entryDate = datetime.datetime.now()
        instance.activationKey = hashlib.md5(str(data[0]['lat']) + str(data[0]['lng']) + str(data[0]['formatted_address']) + str(instance.entryDate)).hexdigest()[:30]
        instance.save()
        LINK_DOMAIN = '127.0.0.1:8000'
        send_mail('Activate your Project', 'Here is the message. Click here: http://' + LINK_DOMAIN + '/renooble/reMap/activate/' + str(instance.activationKey) + '/', 'hannes@renooble.net', [str(instance.userEmail)], fail_silently=False)

        return HttpResponseRedirect("http://www.google.com")

class ReMapUserEditProject(ModelForm):
    class Meta:
        model = Project
        fields = ('rawTechnology', 'installationDate', 'installedPower', 'AEP', 'hideLocation', 'projectBuilding', 'surroundings', 'gridConnection', 'commercialInstallation', 'userComments')
        widgets = {'installationDate': SelectDateWidget(years=range(1970, 2011)), 'userComments': forms.Textarea}


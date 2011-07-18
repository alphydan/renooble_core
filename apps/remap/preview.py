from django.http import HttpResponseRedirect
import datetime

from django.contrib.formtools.preview import FormPreview
from remap.models import Project 

class ProjectRegistrationFormPreview(FormPreview):

    preview_template = 'remap/preview.html'
    form_template = 'remap/form.html'

    def done(self, request, cleaned_data):
        # Do something with the cleaned_data, then redirect
        # to a "success" page.

        instance = Project()
        for field, value in cleaned_data.iteritems():
            setattr(instance, field, value)
        instance.entryDate = datetime.datetime.now()
        instance.activationKey = "blabla"
        instance.save()
            
        return HttpResponseRedirect('../thanks')

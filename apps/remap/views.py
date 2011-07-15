# Django imports
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

# Re.nooble imports
from remap.models import Project
from remap.forms import ReMapLocationForm, ReMapProjectForm, ReMapUserEditProject

def projects(request):
#
# Insert code for reading the database with the projects
# and adding it to the google map
#
    return redirect('http://www.django.org')

def add_project(request):
    locationForm = ReMapLocationForm()
    return render_to_response('remap/add_project_location.html', {
        'locationForm': locationForm,
    }, context_instance = RequestContext(request))

def add_project_details(request):
    if request.method == 'POST': # If the form has been submitted...
        locationForm = ReMapLocationForm(request.POST) 
        if locationForm.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            # extract the address
            country = locationForm.cleaned_data['country']
            projectForm = ReMapProjectForm()
            return render_to_response('remap/add_project_details.html', {
                 'projectForm': projectForm,
                 'user_country': country,
                 }, context_instance = RequestContext(request))

        else:
            return HttpResponseRedirect('../') # Redirect to the location reg if site is requested w/o proper location 
    else:
        return HttpResponseRedirect('../') # Redirect to the location reg if site is requested w/o proper location

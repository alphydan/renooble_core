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
    locationForm = ReMapLocationForm(auto_id='%s')
    return render_to_response('remap/add_project_location.html', {
        'locationForm': locationForm,
    }, context_instance = RequestContext(request))

def add_project_details(request):
    if request.method == 'POST': # If the form has been submitted...
        locationForm = ReMapLocationForm(request.POST) 
        # if True: # All validation rules pass
        if locationForm.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            # extract the address
            print "Valid form .............................."
            locality = locationForm.cleaned_data['locality']
            # cleanAddress = locationForm.cleaned_data['cleanAddress']
            state = locationForm.cleaned_data['state']
            country = locationForm.cleaned_data['country']
            lat = locationForm.cleaned_data['lat']
            lng = locationForm.cleaned_data['lng']
            projectForm = ReMapProjectForm(initial = { 
                 # 'cleanAddress': cleanAddress, 
                 'locality': locality, 
                 'state': state, 
                 'country': country, 
                 'lat': lat,
                 'lng': lng,
            })
            return render_to_response('remap/add_project_details.html', {
                 'projectForm': projectForm,
                 'country': country,
                 }, context_instance = RequestContext(request))

        else:
            print locationForm.errors 
            return HttpResponseRedirect('../') # Redirect to the location reg if site is requested w/o proper location 
    else:
        return HttpResponseRedirect('../') # Redirect to the location reg if site is requested w/o proper location

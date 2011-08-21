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

    #def add_project_details(request):
#    projectForm = ReMapProjectForm()
#    return render_to_response('remap/add_project_details.html', {
#        'projectForm': projectForm,
#        }, context_instance = RequestContext(request))

    # add project details    
def add_project_details(request):
    if request.method == 'POST': # If the form has been submitted...
        locationForm = ReMapLocationForm(request.POST) 
        if locationForm.is_valid(): # All validation rules pass
            locality = locationForm.cleaned_data['locality']
            state = locationForm.cleaned_data['state']
            country = locationForm.cleaned_data['country']
            lat = locationForm.cleaned_data['lat']
            lng = locationForm.cleaned_data['lng']
            energyResource = locationForm.cleaned_data['energyResource']
            
            projectForm = ReMapProjectForm(initial = { 
                'locality': locality, 
                'state': state, 
                'country': country, 
                'lat': lat,
                'lng': lng,
                'energyResource': energyResource,
            })
            return render_to_response('remap/add_project_details.html', {
                'projectForm': projectForm,
            }, context_instance = RequestContext(request))

        else:
            print locationForm.errors 
            return render_to_response('remap/add_project_location.html', {
                'locationForm': locationForm,
            }, context_instance = RequestContext(request))
    else:
        return HttpResponseRedirect('../') # Redirect to the location reg if site is requested w/o proper location 

def add_project_confirm(request):
    if request.method == 'POST': # If the form has been submitted...
        print "POST worked"
        projectForm = ReMapProjectForm(request.POST)
        if projectForm.is_valid():
            return render_to_response('remap/add_project_preview.html', {
                'projectForm': projectForm,
                }, context_instance = RequestContext(request))
        else: 
            print projectForm.errors
            return render_to_response('remap/add_project_details.html', {
                'projectForm': projectForm,
                }, context_instance = RequestContext(request))



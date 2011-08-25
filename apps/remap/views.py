# Django imports
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
import datetime

# Re.nooble imports
from remap.models import Project
from remap.forms import ReMapLocationForm, ReMapProjectForm, ReMapUserEditProject, ReMapSolarDetails, ReMapWindDetails


    ###################################################################
    #      Display all projects
    ###################################################################

def projects(request):
    #
# Insert code for reading the database with the projects
# and adding it to the google map
#
    return redirect('http://www.django.org')

    ###################################################################
    #     Register project location and start registration process
    ###################################################################

def add_project(request):
    if  request.method == 'POST':
        locationForm = ReMapLocationForm(request.POST)
        if  locationForm.is_valid():
            request.session['session_energyResource'] = locationForm.cleaned_data['energyResource']
            request.session['session_address'] = locationForm.cleaned_data['address']
            request.session['session_locality'] = locationForm.cleaned_data['locality']
            request.session['session_route'] = locationForm.cleaned_data['route']
            request.session['session_streetNumber'] = locationForm.cleaned_data['streetNumber']
            request.session['session_postalCode'] = locationForm.cleaned_data['postalCode']
            request.session['session_state'] = locationForm.cleaned_data['state']
            request.session['session_country'] = locationForm.cleaned_data['country']
            request.session['session_locationType'] = locationForm.cleaned_data['locationType']
            request.session['session_lat'] = locationForm.cleaned_data['lat']
            request.session['session_lng'] = locationForm.cleaned_data['lng']
            return HttpResponseRedirect(reverse('add_project_details'))
    else:
        locationForm = ReMapLocationForm(auto_id='%s', 
                            initial={
                                'address': '34 Pasir Panjang Hill, Singapore 118856',
                            'route': 'Pasir Pajang Hill',
                            'streetNumber': '34',
                            'postalCode': '118856',
                            'locality': 'Singapore', 
                            'state': '', 
                            'country': 'Singapore', 
                            'lat': '1.28', 
                            'lng': '103.78', 
                            'locationType': 'ROOFTOP',
                            })
    return render_to_response('remap/add_project_location.html', {
        'locationForm': locationForm,
        }, context_instance = RequestContext(request))

    ###################################################################
    # add project details    
    ###################################################################
def add_project_details(request):
    print "here"
    if request.session.get('session_address', False):
        print "Session available"
        session_results = {
                'energyResource': request.session['session_energyResource'], 
                'address': request.session['session_address'], 
                'lat': request.session['session_lat'], 
                'lng': request.session['session_lng'],
                }
    else:
        return redirect(add_project)

    if request.method == 'POST': # If the form has been submitted...
        projectForm = ReMapProjectForm(request.POST) 
        if session_results['energyResource'] == 'SOLAR':
            resourceForm = ReMapSolarDetails(request.POST)
            resourceFormValid = resourceForm.is_valid()
        elif session_results['energyResource'] == 'WIND':
            resourceForm = ReMapWindDetails(request.POST)
            resourceFormValid = resourceForm.is_valid()
   

# http://stackoverflow.com/questions/569468/django-multiple-models-in-one-template-using-forms

        if projectForm.is_valid() and resourceFormValid: # All validation rules pass
            print "form is valid"
            foo = ReMapProjectForm(request.POST)
            savedProjectForm = foo.save(commit=False)
            savedProjectForm.lat = session_results['lat']
            savedProjectForm.lng = session_results['lng']
            savedProjectForm.address = session_results['address']
            savedProjectForm.energyResource = session_results['energyResource']
            savedProjectForm.entryDate = datetime.now()
            savedProjectForm.save()
            
            savedResourceForm = resourceForm.save(commit=False)
            resourceForm.projectID = savedProjectForm
            resourceForm.save()
            # save the data to the database
            # return HttpResponseRedirect(reverse('about', args=()))
            # 
            # forward to confirmation site

            return redirect(about)

    else:
        projectForm = ReMapProjectForm()

        if session_results['energyResource'] == 'SOLAR':
            resourceForm = ReMapSolarDetails()
        elif session_results['energyResource'] == 'WIND':
            resourceForm = ReMapWindDetails()
        
        return render_to_response('remap/add_project_details.html', {
            'projectForm': projectForm,
            'session_results': session_results,
            'resourceForm': resourceForm, 
        }, context_instance = RequestContext(request))
        
    ###################################################################
    #    Confirmation page for the registered project
    ###################################################################

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



from remap.models import Project
from remap.forms import ReMapLocationForm, ReMapProjectForm, ReMapUserEditProject

def projects(request):
#
# Insert code for reading the database with the projects
# and adding it to the google map
#
    return redirect('http://www.django.org')

def add_project(request):
    locationForm = ReMapLocationForm
    return render_to_response('add_project_location.html', {
        'locationForm': locationForm
    })

def add_project_details(request):
    projectForm = ReMapProjectForm
    return render_to_response('add_project_details.html', {
        'projectForm': projectForm
    })





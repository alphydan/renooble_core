#from django
from django.conf.urls.defaults import *

# from remap
from remap.models import Project

# for the project registrations form review
from remap.preview import ProjectRegistrationFormPreview
from remap.forms import ReMapProjectForm
from django import forms

urlpatterns = patterns("",
    # url(r"^$", "remap.views.projects", name="all_projects"),
    # url(r"^projects/(\d+)/$", "remap.views.project", name="project_details"),
    # url(r"^your_project/$", "remap.views.your_projects", name="your_projects"),
    # url(r"^user_project/(?P<username>\w+)/$", "remap.views.user_projects", name="user_projects"),

    # CRUD urls
    url(r"^add/$", "remap.views.add_project", name="add_project_location"),
    url(r"^add/details/$", "remap.views.add_project_details", name="add_project_details"),
    # url(r"^add/confirm/$", "remap.views.add_project_confirm", name="add_project_confirm"),
    url(r"^add/confirm/$", ProjectRegistrationFormPreview(ReMapProjectForm), name="add_project_confirm"),
    # url(r"^update/(\d+)/$", "remap.views.update_project", name="update_project"),
    # url(r"^delete/(\d+)/$", "remap.views.delete_project", name="delete_project"),
)


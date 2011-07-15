#from django
from django.conf.urls.defaults import *

# from bookstore
from remap.models import Project

urlpatterns = patterns("",
    # url(r"^$", "remap.views.projects", name="all_projects"),
    # url(r"^projects/(\d+)/$", "remap.views.project", name="project_details"),
    # url(r"^your_project/$", "remap.views.your_projects", name="your_projects"),
    # url(r"^user_project/(?P<username>\w+)/$", "remap.views.user_projects", name="user_projects"),

    # CRUD urls
    url(r"^add/$", "remap.views.add_project", name="add_project_location"),
    url(r"^add/details/$", "remap.views.add_project_details", name="add_project_details"),
    # url(r"^update/(\d+)/$", "remap.views.update_project", name="update_project"),
    # url(r"^delete/(\d+)/$", "remap.views.delete_project", name="delete_project"),
)


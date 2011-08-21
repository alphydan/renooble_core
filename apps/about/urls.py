from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
    url(r"^$", direct_to_template, {"template": "about/about.html"}, name="about"),
    url(r"^support_us/$", direct_to_template, {"template": "about/support_us.html"}, name="support_us"),
    url(r"^contact/$", direct_to_template, {"template": "about/contact.html"}, name="contact"),
    url(r"^contact/thanks/$", direct_to_template, {"template": "about/contact_thanks.html"}, name="contact_thanks"),
    url(r"^sitemap/$", direct_to_template, {"template": "about/sitemap.html"}, name="sitemap"),
    url(r"^what_next/$", direct_to_template, {"template": "about/what_next.html"}, name="what_next"),
)

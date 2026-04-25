from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('program-components', views.programcomponents, name='program-components'),
    path('initiatives', views.initiatives, name='initiatives'),
    path('news', views.news, name='news'),
    path('mentors', views.mentors, name='mentors'),
    path('mentors-signup-success', views.mentorssignupsuccess, name='mentors-signup-success'),
    path('mentees', views.mentees, name='mentees'),
    path('mentees-signup-success', views.menteessignupsuccess, name='mentees-signup-success'),
    path('contact', views.contact, name='contact'),
    path('contact-success', views.contactsuccess, name='contact-success'),
    path('donate', views.donate, name='donate'),
]
from django import forms
from .models import Mentee
from .models import Mentor
from .models import Contact

class Mentee(forms.ModelForm):
    class Meta:
        model = Mentee
        fields = ["menteeFirstName", "menteeLastName", "menteeEmail", "menteePhone", "parentFirstName", "parentLastName", "parentPhone", "parentEmail", "dateOfBirth", "currentSchool", "careerInterest", "commentOrMessage"]
        labels = {
            'menteeFirstName': 'First Name',
            'menteeLastName': 'Last Name',
            'menteeEmail': 'Email',
            'menteePhone': 'Phone',
            'parentFirstName': 'Parent First Name',
            'parentLastName': 'Parent Last Name',
            'parentPhone': 'Parent Phone',
            'parentEmail': 'Parent Email',
            'dateOfBirth': 'Date of Birth',
            'currentSchool': 'Current School',
            'careerInterest': 'Career Interest',
            'commentOrMessage': 'Comment or Message'
        }

class Mentor(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ["mentorFirstName", "mentorLastName", "mentorEmail", "mentorPhone", "mentorProfession", "mentorResume", "commentOrMessage"]
        labels = {
            'mentorFirstName': 'First Name',
            'mentorLastName': 'Last Name',
            'mentorEmail': 'Email',
            'mentorPhone': 'Phone',
            'mentorProfession': 'Profession',
            'mentorResume': 'Resume',
            'commentOrMessage': 'Comment or Message'
        }

class Contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["contactFirstName", "contactLastName", "contactEmail", "contactPhone", "commentOrMessage"]
        labels = {
            'contactFirstName': 'First Name',
            'contactLastName': 'Last Name',
            'contactEmail': 'Email',
            'contactPhone': 'Phone',
            'commentOrMessage': 'Comment or Message'
        }
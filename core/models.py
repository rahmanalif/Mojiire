from django.db import models

# Create your models here.
class Mentee(models.Model):
    menteeFirstName = models.CharField(max_length=255)
    menteeLastName = models.CharField(max_length=255)
    menteeEmail = models.EmailField(max_length=255)
    menteePhone = models.CharField(max_length=15)
    parentFirstName = models.CharField(max_length=255)
    parentLastName = models.CharField(max_length=255)
    parentPhone = models.CharField(max_length=15)
    parentEmail = models.EmailField(max_length=255)
    dateOfBirth = models.DateField()
    currentSchool = models.CharField(max_length=255)
    careerInterest = models.CharField(max_length=255)
    commentOrMessage = models.TextField()

    def __str__(self):
        return f"{self.menteeFirstName} {self.menteeLastName} {self.menteeEmail} {self.menteePhone} {self.parentFirstName} {self.parentLastName} {self.parentPhone} {self.parentEmail} {self.dateOfBirth} {self.currentSchool} {self.careerInterest} {self.commentOrMessage}"

class Mentor(models.Model):
    mentorFirstName = models.CharField(max_length=255)
    mentorLastName = models.CharField(max_length=255)
    mentorEmail = models.EmailField(max_length=255)
    mentorPhone = models.CharField(max_length=15)
    mentorProfession = models.CharField(max_length=255)
    mentorResume = models.FileField(upload_to='documents/')
    commentOrMessage = models.TextField()

    def __str__(self):
        return f"{self.mentorFirstName} {self.mentorLastName} {self.mentorEmail} {self.mentorPhone} {self.mentorProfession} {self.mentorResume} {self.commentOrMessage}"

class Contact(models.Model):
    contactFirstName = models.CharField(max_length=255)
    contactLastName = models.CharField(max_length=255)
    contactEmail = models.EmailField(max_length=255)
    contactPhone = models.CharField(max_length=15)
    commentOrMessage = models.TextField()

    def __str__(self):
        return f"{self.contactFirstName} {self.contactLastName} {self.contactEmail} {self.contactPhone} {self.commentOrMessage}"

class Donations(models.Model):
    donorFirstName = models.CharField(max_length=255)
    donorLastName = models.CharField(max_length=255)
    donorEmail = models.EmailField(max_length=255)
    donorPhone = models.CharField(max_length=15)
    donorAmount = models.FloatField(max_length=15)

class EventsGallery(models.Model):
    eventName = models.CharField(max_length=255)
    eventNumber = models.IntegerField()
    eventDate = models.DateField()
    eventSummary = models.CharField(max_length=510)
    eventImage1 = models.FileField(upload_to='media/', blank=True, null=True)
    eventImage2 = models.FileField(upload_to='media/', blank=True, null=True)
    eventImage3 = models.FileField(upload_to='media/', blank=True, null=True)
    eventImage4 = models.FileField(upload_to='media/', blank=True, null=True)
    eventImage5 = models.FileField(upload_to='media/', blank=True, null=True)
    eventImage6 = models.FileField(upload_to='media/', blank=True, null=True)
    eventImage7 = models.FileField(upload_to='media/', blank=True, null=True)
    eventImage8 = models.FileField(upload_to='media/', blank=True, null=True)
    eventImage9 = models.FileField(upload_to='media/', blank=True, null=True)
    eventImage10 = models.FileField(upload_to='media/', blank=True, null=True)


class UpcomingEvent(models.Model):
    title = models.CharField(max_length=255)
    event_date = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    display_order = models.PositiveIntegerField(default=0, help_text="Smaller numbers appear first in the list.")
    is_published = models.BooleanField(default=True, help_text="Uncheck to hide this event from the website without deleting it.")

    class Meta:
        ordering = ["display_order", "event_date", "title"]
        verbose_name = "Upcoming Event"
        verbose_name_plural = "Upcoming Events"

    def __str__(self):
        return f"{self.title} ({self.event_date})"

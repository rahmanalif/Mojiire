from django.contrib import admin

from .models import Contact
from .models import Donations
from .models import EventsGallery
from .models import Mentee
from .models import Mentor
from .models import UpcomingEvent


@admin.register(UpcomingEvent)
class UpcomingEventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "display_order", "is_published")
    list_editable = ("display_order", "is_published")
    list_filter = ("is_published", "event_date")
    search_fields = ("title", "description")
    ordering = ("display_order", "event_date", "title")
    date_hierarchy = "event_date"
    fieldsets = (
        ("Event Details", {
            "fields": ("title", "event_date", "description"),
            "description": "Add the public details that should appear on the News page.",
        }),
        ("Visibility", {
            "fields": ("display_order", "is_published"),
            "description": "Control the order and whether the event is visible on the website.",
        }),
    )


@admin.register(EventsGallery)
class EventsGalleryAdmin(admin.ModelAdmin):
    list_display = ("eventName", "eventDate", "eventNumber")
    list_filter = ("eventDate",)
    search_fields = ("eventName", "eventSummary")
    ordering = ("-eventDate", "eventNumber")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("contactFirstName", "contactLastName", "contactEmail", "contactPhone")
    search_fields = ("contactFirstName", "contactLastName", "contactEmail", "contactPhone")


@admin.register(Mentee)
class MenteeAdmin(admin.ModelAdmin):
    list_display = ("menteeFirstName", "menteeLastName", "menteeEmail", "currentSchool")
    search_fields = ("menteeFirstName", "menteeLastName", "menteeEmail", "currentSchool")


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ("mentorFirstName", "mentorLastName", "mentorEmail", "mentorProfession")
    search_fields = ("mentorFirstName", "mentorLastName", "mentorEmail", "mentorProfession")


@admin.register(Donations)
class DonationsAdmin(admin.ModelAdmin):
    list_display = ("donorFirstName", "donorLastName", "donorEmail", "donorAmount")
    search_fields = ("donorFirstName", "donorLastName", "donorEmail")

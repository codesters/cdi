from django.contrib import admin
from cdi.apps.home.models import Address, College, Event, Club, Note

class AddressAdmin(admin.ModelAdmin):
    list_display=('street', 'city', 'state')

class CollegeAdmin(admin.ModelAdmin):
    list_display=('name', 'college_type', 'website')

class EventAdmin(admin.ModelAdmin):
    list_display=('name', 'venue', 'event_type','start_date')

class ClubAdmin(admin.ModelAdmin):
    list_display=('name', 'college', 'club_type')

class NoteAdmin(admin.ModelAdmin):
    list_display=('name', 'related_course', 'submitted_by')



admin.site.register(Address, AddressAdmin)
admin.site.register(College, CollegeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Note, NoteAdmin)


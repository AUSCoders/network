from django.contrib import admin
from .models import Profile, RelationShip

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=["user", "last_name", "first_name",  "avater", "created", "updated", "country", "slug"]
    list_editable=["last_name", "first_name"]
    search_fields=["last_name", "first_name"]
    # list_filter=["updated"," created"]
    class Meta:
        model=Profile
admin.site.register(Profile, ProfileAdmin)

admin.site.register(RelationShip)
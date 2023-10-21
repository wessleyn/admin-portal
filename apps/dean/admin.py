from django.contrib import admin
from apps.dean.models import Dean, Deputy

# Styling 
@admin.register(Dean)
class DeanAdmin(admin.ModelAdmin):
    list_display = [
        '__str__'
    ]

    # Grouping Fields
    fieldsets = [
        (
            'Personal Information',
            {
                "fields": [
                    "last_name",
                    "first_name",
                    "gender",
                    "profile_pic"
                ]
            }
        ),
        (
            'Credentials',
            {
                "fields": [
                    "identity",
                    "password",
                    "email"
                ]
            }
        )
    ]

@admin.register(Deputy)
class DeputyAdmin(admin.ModelAdmin):
    list_display = [
        '__str__'
    ]

    # Grouping Fields
    fieldsets = [
        (
            'Personal Information',
            {
                "fields": [
                    "last_name",
                    "first_name",
                    "gender",
                    "profile_pic"
                ]
            }
        ),
        (
            'Credentials',
            {
                "fields": [
                    "identity",
                    "password",
                    "email"
                ]
            }
        ),
        (
            'Details',
            {
                "fields": [
                    "optional_job"
                ]
            }
        )
    ]

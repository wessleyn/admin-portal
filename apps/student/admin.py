from django.contrib import admin
from apps.student.models import Student

# Styling for Student Model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        '__str__'
    ]
    
    # Grouping Fields
    fieldsets = [
        (
            'Personal Information',
            {
                "fields" : [
                    (
                        "last_name",
                        "first_name"
                    ),
                    (
                        "gender",
                        "identity"
                    )
                ]
            }
        ),
        (
            'Credentials',
            {
                "fields" : [
                    "password",
                    "email"
                ]
            }
        ),
        (
            'Class Details',
            {
                "fields" : [
                    "combination",
                    "classroom",
                ]
            }
        )
    ]

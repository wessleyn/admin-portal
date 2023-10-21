from django import forms
from teacher.models import Teacher

class CreateTeacher(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
        exclude = [
            "user_permissions",
            'groups',
            'is_active',
            'is_staff',
            'is_admin',
            'is_superuser',
            'identity'
            ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex: john@gmail.com'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 30'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'passing_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-2020'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2018-12-31'}),
            'admission_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: LM01'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'teaching_classrooms': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'optional_subject': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 45000'}),
        }


from django import forms
from classroom.models import ClassRoom as classroom

class CreateClassroom(forms.ModelForm):
    class Meta:
        model = classroom
        fields = "__all__"


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'subjects': forms.Select(attrs={'class': 'form-control'}),
            'class_teacher': forms.Select(attrs={'class': 'form-control'}),
            'combination': forms.Select(attrs={'class': 'form-control'}),
        }


from django.forms import ModelForm, TextInput
from django import forms
from .models import Schema


class SchemaForm(ModelForm):
    class Meta:
        model = Schema
        fields = ["title", "column_separator", "string_character"]

        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter name",
            }),
            "column_separator": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter separator",
            }),
            "string_character": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter character",
            }),
        }


# class SchemasForm(forms.ModelForm):
#     def save(self, commit=True, **kwargs):
#         instance = super(SchemasForm, self).save(commit=False)
#         instance.title = instance.title + "..."
#         if commit:
#             instance.save()
#         return instance
#
#     class Meta:
#         model = Schema
#         fields = ["title", "column_separator", "string_character"]
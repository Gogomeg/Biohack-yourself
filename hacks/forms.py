from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Hack


class HackForm(forms.ModelForm):
    """Form to create a health hack"""

    class Meta:
        model = Hack
        fields = [
            "title",
            "description",
            "content",
            "image",
            "image_alt",
            "hack_type",
        ]

        content = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Health Hack Title",
            "description": "Description",
            "content": "Health Hack content",
            "image": "Health Hack Image",
            "image_alt": "Describe Image",
            "hack_type": "Health Hack Type",
        }

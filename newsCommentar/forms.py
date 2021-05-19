from django.forms import ModelForm, widgets

from .models import User, Kommentar


class KommentarForm(ModelForm):
    class Meta:
        model = Kommentar
        fields = ['post']
        widgets = {
            'post': widgets.Textarea(attrs={
                'cols': 60,
                'rows': 5,
                'class': 'newComment'
            })
        }
        labels = {
            'post':  ''
        }

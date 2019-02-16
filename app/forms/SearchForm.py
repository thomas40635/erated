from django import forms

from app.models import Film


class SearchForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = ['titre']

    def clean_titre(self):
        result = self.cleaned_data.get('titre')
        if result == 'toto':
            self.add_error('titre', "Veuillez remplir le formulaire")
        return result

    def clean(self):
        pass


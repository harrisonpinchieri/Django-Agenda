
from django.core.exceptions import ValidationError
from contact.models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={

                'class': 'class a class -b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro nome',
        help_text='help'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # atualiza widget
        # self.fields['first_name'].widget.attrs.update({
        #    'class': 'class a class -b',
        #    'placeholder': 'Aqui veio do init',
        # })

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
    # cria widget
      # widgets = {
      #     'first_name': forms.TextInput(
      #         attrs={
      #             'placeholder': 'escreva aqui',
      #         }
      #     )
      # }

    def clean(self):

        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        return super().clean()

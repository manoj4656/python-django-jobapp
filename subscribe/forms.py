from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels = {
            'first_name': _('firstname')
        }
        error_message = {
            'first_name' :{
                'required': _('please enter first name')
            },
        }

# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError('Invalid Name')
#     return value

# class SubscribeForm(forms.Form):
    # first_name = forms.CharField(max_length=100, required=False, label='firstname', help_text='characters only')
    # last_name = forms.CharField(max_length=100, disabled=False,validators=[validate_comma])
    # email = forms.EmailField(max_length=100)

    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if "," in data:
    #         raise forms.ValidationError('Invalid first name')
    #     return data
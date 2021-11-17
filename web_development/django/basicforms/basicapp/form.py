from django import forms
from django.core import validators

def check_z(value):
    if value[0].lower()!= 'z':
        raise forms.ValidationError("The value must be start with z!")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_z]) # passing function
    email = forms.EmailField()
    verify_email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False,
                                 widget = forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        """
        In clean check cleaned data
        """

        # grap all clean data.
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail :
            raise forms.ValidationError("Email and Verify email value is not same!")


    def clean_text(self):
        """
        Add clean_ specific method check specific variable.
        """
        text = self.cleaned_data['text']
        if len(text) < 10:
            raise forms.ValidationError("Text lenght should be longer than 10")

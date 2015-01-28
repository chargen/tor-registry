from django import forms
from captcha.fields import CaptchaField

from userregistry.models import TorUserModel

class TorUserModelForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = TorUserModel

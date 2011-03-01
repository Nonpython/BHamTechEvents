#!/usr/bin/env python
# encoding: utf-8
from django import forms
from utils.recaptcha import ReCaptchaField
from floppyforms import AutofocusInput

class LoginForm(forms.Form):
    username = forms.CharField(label=_(u'Username'), widget=AutofocusInput)
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput(render_value=False)) 


#!/usr/bin/env python
# encoding: utf-8
from django import forms
from utils.recaptcha import ReCaptchaField
from floppyforms import AutofocusInput

class LoginForm(forms.Form):
    username = forms.CharField(label=_(u'Username'), widget=AutofocusInput)
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput(render_value=False)) 

class RegisterForm1(forms.Form):
    username = forms.CharField(label=_(u'Username'))
    email = EmailField(label=_(u"Email"))
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput(render_value=False)) 
    passwordconfirm = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput(render_value=False))
    recaptcha = ReCaptchaField()
    
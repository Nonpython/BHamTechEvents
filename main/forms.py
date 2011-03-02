#!/usr/bin/env python
# encoding: utf-8
from django import forms
from utils.recaptcha import ReCaptchaField
from floppyforms import AutofocusInput

class LoginForm(forms.Form):
    username = forms.CharField(label=_(u'Username'), widget=AutofocusInput)
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput(render_value=False)) 

class RegisterForm(forms.Form):
    username = forms.CharField(label=_(u'Username'))
    email = forms.EmailField(label=_(u"Email"))
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput(render_value=False)) 
    passwordconfirm = forms.CharField(label=_(u'Confirm your password'), widget=forms.PasswordInput(render_value=False))
    realname =  forms.CharField(label=_(u'Real name'))
    bio = forms.CharField(label=_(u'Tell us a little about yourself'), widget=forms.Textarea())
    recaptcha = ReCaptchaField(label=_(u'Are you a human?'))
    
    
#!/usr/bin/env python
# encoding: utf-8
from django import forms
from utils.recaptcha import ReCaptchaField
from floppyforms import AutofocusInput
from taggit.utils import parse_tags, edit_string_for_tags
from django.contrib.admin import widgets as admin_widgets
from django.template import loader, Context
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.conf import settings

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
    
class TagAutocompleteWidget(forms.TextInput):
    def render(self, name, value, attrs=None):
        if value is not None and not isinstance(value, basestring):
            value = edit_string_for_tags([o.tag for o in value.select_related("tag")])
        attrs["id"] = "tag_autocomplete"
        return super(TagWidget, self).render(name, value, attrs)

class WMDEditor(forms.Textarea):
    def render(self, name, value, attrs=None):
        # Prepare values
        if not value:
            value = ''
        attrs = self.build_attrs(attrs, name=name)
        # Render widget to HTML
        t = loader.get_template('wmd/widget.html')
        c = Context({
            'attributes' : self._render_attrs(attrs),
            'value' : conditional_escape(force_unicode(value)),
            'id' : attrs['id'],
        })
        return t.render(c)
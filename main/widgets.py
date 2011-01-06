from django import forms
from django.contrib.admin import widgets as admin_widgets
from django.template import loader, Context
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode

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
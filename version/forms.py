from django.forms import ModelForm

from version.models import Version


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
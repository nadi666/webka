from django import forms
from django.conf import settings
from .models import Manager, DailyReport

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'


class DailyReportForm(forms.ModelForm):
    class Meta:
        model = DailyReport
        fields = '__all__'
        widgets = {'report_date': forms.TextInput(attrs={'placeholder': '%Y-%m-%d'})}

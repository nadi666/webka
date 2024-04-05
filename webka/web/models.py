from django.db import models
from importlib.resources import _
import datetime

class Manager(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.last_name

class DailyReport(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    report_name = models.CharField(max_length=50, null=True)
    report_address = models.CharField(max_length=250, null=True)
    report_date = models.DateField(_("Date"), default=datetime.date.today)
    report_sum = models.DecimalField(max_digits=10, decimal_places=2, null=True)
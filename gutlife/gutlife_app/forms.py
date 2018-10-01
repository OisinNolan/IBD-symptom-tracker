from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime

now = datetime.datetime.now()
nearbyYears = { now.year, now.year-1, now.year-2}
timeFormat = str(now.hour) + ":" + str(now.minute)

class BMForm(forms.Form):
    consistency = forms.IntegerField(label='Consistency')
    solidity = forms.IntegerField(label='Solidity')
    datecode = forms.DateField(label='Date', initial=datetime.date.today, widget=forms.SelectDateWidget(years=nearbyYears))
    time = forms.TimeField(label='Time', initial=datetime.datetime.now)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
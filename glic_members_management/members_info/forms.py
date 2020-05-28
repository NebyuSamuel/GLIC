from django import forms
from members_info.models import Profile

class MemberForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo','fullname','sex','job','subcity','woreda','housenum','phonenum',
                'marriage','yearofmarriage','childernnum','yearofsalvation','baptism',
                'yearofbaptism','prevchurch','death'
        ]
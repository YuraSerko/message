# -*- coding=utf-8 -*-
from django import forms

class New_message_form(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'style':"resize:vertical",'cols' : "35", 'rows': "2",  }),
        required=True,
        error_messages={'required': 'Введите, пожалуйста текст сообщения'}
        )
    
    





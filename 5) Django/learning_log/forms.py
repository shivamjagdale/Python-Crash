from django import forms

from . models import Topic, Entry

# Topic Model
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = {"text"}
        labels = {"text":''}

# Entry Model 
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = {"text"}
        labels = {"text":""}
        widgets = {"text": forms.Textarea(attrs = {"cols":80})}
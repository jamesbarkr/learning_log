from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic # which model to base the form on
        fields = ['text'] # include only the text field
        labels = {'text': ''} # don't generate a label
                              # for the text field

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
        # a widget is an HTML form element, such as a single-line text
        # box or a drop-down list. Here, we are telling Django to Create
        # a wider text box (80 cols instead of the typical 40)

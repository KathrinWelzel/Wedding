from django import forms
from bootcamp.questions.models import Question, Answer

class QuestionForm(forms.ModelForm):
    Titel = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), 
        max_length=255)
    Beschreibung = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), 
        max_length=2000)
    Schlagworte = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=255,
        required=False)

    class Meta:
        model = Question
        fields = ['Titel', 'Beschreibung', 'Schlagworte']

class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=Question.objects.all())
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':'4'}), 
        max_length=2000)

    class Meta:
        model = Answer
        fields = ['question', 'description']
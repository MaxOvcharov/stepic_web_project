from models import Answer, Question

from django import forms
from django.forms import ModelForm


class AskForm(ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'text']


class AnswerForm(ModelForm):

    class ModelChoiceFieldTitle(forms.ModelChoiceField):

        def label_from_instance(self, obj):
            return obj.title

    question = ModelChoiceFieldTitle(queryset=Question.objects.all())

    class Meta:
        model = Answer
        fields = ['question', 'text']
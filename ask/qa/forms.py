from models import Answer, Question

from django import forms
# from django.forms import ModelForm
from django.contrib.auth.models import User

# class AskForm(ModelForm):
#
#     class Meta:
#         model = Question
#         fields = ['title', 'text']
#
#
# class AnswerForm(ModelForm):
#
#     class ModelChoiceFieldTitle(forms.ModelChoiceField):
#
#         def label_from_instance(self, obj):
#             return obj.title
#
#     question = ModelChoiceFieldTitle(queryset=Question.objects.all())
#
#     class Meta:
#         model = Answer
#         fields = ['question', 'text']


class AskForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea, max_length=128)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        user, _ = User.objects.get_or_create(username='x', defaults={'password': 'y'})

        q = Question(title=self.cleaned_data['title'], text=self.cleaned_data['text'], author=user)
        q.save()
        return q

    def clean(self):
        return self.cleaned_data


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=Question.objects.all())

    def save(self):
        user, _ = User.objects.get_or_create(username='x', defaults={'password': 'y'})

        ans = Answer(text=self.cleaned_data['text'], question=self.cleaned_data['question'], author=user)
        ans.save()
        return ans

    def clean(self):
        pass
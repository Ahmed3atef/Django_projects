from django import forms
from conversation.models import ConversationsMessage

class ConversationMassageForm(forms.ModelForm):
    class Meta:
        model = ConversationsMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }
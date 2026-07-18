from django import forms
from .models import Article, Paragraph, MediaAttachment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'summary', 'cover_image', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Article title'}),
            'author': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Author name'}),
            'summary': forms.Textarea(attrs={'class': 'input', 'rows': 3, 'placeholder': 'Short intro shown on the landing page'}),
        }


class ParagraphForm(forms.ModelForm):
    class Meta:
        model = Paragraph
        fields = ['text', 'image', 'image_caption']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'input', 'rows': 4, 'placeholder': 'Paragraph text'}),
            'image_caption': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Optional image caption'}),
        }


class MediaAttachmentForm(forms.ModelForm):
    class Meta:
        model = MediaAttachment
        fields = ['file', 'media_type', 'caption']
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Optional caption'}),
            'media_type': forms.Select(attrs={'class': 'input'}),
        }


ParagraphFormSet = forms.inlineformset_factory(
    Article, Paragraph, form=ParagraphForm,
    fields=['text', 'image', 'image_caption'],
    extra=2, can_delete=True
)

MediaFormSet = forms.inlineformset_factory(
    Article, MediaAttachment, form=MediaAttachmentForm,
    fields=['file', 'media_type', 'caption'],
    extra=1, can_delete=True
)

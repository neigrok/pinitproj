from django import forms

class PinForm(forms.Form):
    url = forms.URLField(label='', widget=forms.TextInput(attrs={'placeholder': 'URL',
                                                                 'style': 'width: 300px',
                                                                 'class': 'form-control'}))


class SearchForm(forms.Form):
    text = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Search',
                                                                 'class': 'form-control'}))

# class ShareForm(forms.Form):
#         text = forms.CharField(disabled=True, label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Your link will apper',
#                                                                                        'class': 'form-control'}))

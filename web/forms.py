from django import forms


class Theme(forms.Form):
    checkbox = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={'class': 'toggle', 'id': 'checkbox'}), required=False, label="")

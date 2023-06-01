from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    rate = forms.FloatField()
    article = forms.CharField(max_length=20, required=False)
    title = forms.CharField(max_length=256)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    description = forms.CharField(widget=forms.Textarea())

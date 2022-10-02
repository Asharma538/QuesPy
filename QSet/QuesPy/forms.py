from django import forms

class MyFileUploadForm(forms.Form):
    image_q = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    image_op1 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control op1img'}))
    image_op2 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control op2img'}))
    image_op3 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control op3img'}))
    image_op4 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control op4img'}))
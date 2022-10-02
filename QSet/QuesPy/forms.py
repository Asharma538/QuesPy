from django import forms

class MyFileUploadForm(forms.Form):
    image_q = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}),required=False)
    image_op1 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control op1img'}),required=False)
    image_op2 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control op2img'}),required=False)
    image_op3 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control op3img'}),required=False)
    image_op4 = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control op4img'}),required=False)
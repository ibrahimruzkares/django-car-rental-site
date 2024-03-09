from django import forms

class ReservationForm(forms.Form):
    first_name = forms.CharField(label='Name', max_length=200)
    last_name = forms.CharField(label='Surname', max_length=200)
    email = forms.EmailField(label='Email', max_length=200)
    phone = forms.IntegerField(initial=0)
    message = forms.CharField(label='Message', max_length=400, 
                              widget=forms.TextInput(attrs={'style': 'width: 300px; height: 100px; '}))
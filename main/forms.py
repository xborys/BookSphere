from django import forms
from django.forms import ModelForm
from .models import author, book, borrower, books_loan
from django.forms.widgets import NumberInput
from django.contrib.admin.widgets import AdminDateWidget

class AuthorForm(forms.ModelForm):
    class Meta:
        model = author
        fields = ('name', 'lastname', 'nationality', 'birth')

        labels = {
            'name' : '', 
            'lastname' : '',
            'nationality' : '',
            'birth' : ''
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author name'}),
            'lastname' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Author lastname'}),
            'nationality' : forms.Select(attrs={'class':'form-control', 'placeholder':'Author nationality'}),
            'birth' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ('title', 'author', 'category', 'publish_date', 'description')

        labels = {
            'title' : '',
            'author' : '',
            'category' : '',
            'publish_date' : '',
            'description' : ''
        }

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Book title'}),
            'author' : forms.Select(attrs={'class':'form-control', 'placeholder':'Select book author'}),
            'category' : forms.Select(attrs={'class':'form-control', 'placeholder':'Select book cathegory'}),
            'publish_date' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'})
        }

class BorrowerForm(forms.ModelForm):
    class Meta:
        model = borrower
        fields = ('name', 'lastname', 'email', 'phone')

        labels = {
            'name' : '',
            'lastname' : '',
            'email' : '',
            'phone' : ''
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name'}),
            'lastname' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'email'}),
            'phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number'})
        }

class BookLoanForm(forms.ModelForm):
    class Meta:
        model = books_loan
        fields = ('borrower', 'book', 'end_loan')

        labels = {
            'borrower' : '',
            'book' : '',
            'end_loan' : ''
        }

        widgets = {
            'borrower' : forms.Select(attrs={'class':'form-control', 'placeholder':'Select borrower'}),
            'book' : forms.Select(attrs={'class':'form-control', 'placeholder':'Select book'}),
            'end_loan' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
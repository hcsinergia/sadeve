# make sure this is at the top if it isn't already
from django import forms

# # our new form
# class ContactForm(forms.Form):
#     contact_name = forms.CharField(required=True)
#     contact_email = forms.EmailField(required=True)
#     content = forms.CharField(
#         required=True,
#         widget=forms.Textarea
#     )



class ContactForm(forms.Form):
        contact_name = forms.CharField(required=True)
        contact_email = forms.EmailField(required=True)
        content = forms.CharField(
            required=True,
            widget=forms.Textarea
        )

        def __init__(self, *args, **kwargs):    
            super(ContactForm, self).__init__(*args, **kwargs)
            self.fields['contact_name'].label=''
            self.fields['contact_email'].label=''
            self.fields['content'].label=''

            self.fields['contact_name'].widget.attrs={
                        'required': True,
                        'class': 'form-control',
                        'placeholder': 'Ingrese su nombre',
                        'id': 'contact_name'
                    }
            self.fields['contact_email'].widget.attrs={
                        'class': 'form-control',
                        'required': True,
                        'placeholder': 'Ingrese su email',
                        'id': 'contact_email'
                    }
            self.fields['content'].widget.attrs={
                        'class': 'form-control',
                        'placeholder': 'Ingrese su mensaje',
                        'id': 'content'
                        
                    }

        











        # the new bit we're adding
        # def __init__(self, *args, **kwargs):
        #     super(ContactForm, self).__init__(*args, **kwargs)
        #     self.fields['contact_name'].label = "nombre: "
        #     self.fields['contact_email'].placeholder = "email: "
        #     self.fields['content'].placeholder = "mensaje "



        #     self.fields['contact_name'].label = "nombre:"
        #     self.fields['contact_email'].label = "email:"
        #     self.fields['content'].label = "mensaje"
       
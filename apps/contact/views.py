from django.shortcuts import render, redirect
from django.views.generic import View

# Create your views here.

# add to the top
# from forms import ContactForm
from apps.contact.forms import ContactForm
from django.conf import settings

# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib import messages
from validate_email import validate_email

from django.core.mail import send_mail, BadHeaderError

# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            


            # Email the profile with the
            # contact information
            template = get_template('contact/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
                'has_error':False,
            }

            if not validate_email(contact_email):
                messages.add_message(request,messages.ERROR,'Ingrese un email válido')
                context['has_error']=True

            if context['has_error']:
                return render(request, 'contact/contact.html', context, status=400)


            content = template.render(context)

            email = EmailMessage(
                "Mensaje desde SADeVe web",
                content,
                # "sadeve.com.ar" +'',
                # [''],
                # headers = {'Reply-To': contact_email }
                settings.EMAIL_HOST_USER,
                # to=[contact_email]
                to=[settings.EMAIL_HOST_USER,]
            )
            # print(email)
            email.send()

            

        # current_site=get_current_site(request)
        # email_subject='Mensaje desde la web'
        # message=render_to_string('contact/contact_template.txt',
        # {
        #     'user':contact_name,
        #     'domain':current_site.domain,
        #     'contact_email': contact_email,
        #     'form_content': form_content,       
        # }
        # )

        # email_message = EmailMessage(
        #     email_subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     to=[contact_email]
        # )

        # print(message)

        # email_message.send()

        messages.add_message(request,messages.SUCCESS,'Gracias por su contacto. El mensaje fue enviado correctamente')


        # return redirect('contacto')

    return render(request, 'contact/contact.html', {
        # 'form': form_class,
        'form': form_class(request.POST),
    })


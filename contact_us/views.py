from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact_us email from:  {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            recipient = form.cleaned_data.get('email')
            send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            return render(request, 'contact_us/contact_success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact_us/contact_us.html', context)

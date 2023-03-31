from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.conf import settings
from django.core.mail import EmailMessage
import logging

logger = logging.getLogger(__name__)


class MainListView(TemplateView):
    template_name = 'mainapp/index.html'


class ColorListView(TemplateView):
    template_name = 'mainapp/ral_colors.html'


class ServiceListView(TemplateView):
    template_name = 'mainapp/services.html'


class EmailView(View):
    def get(self, request):
        logger.error('ONLY POST REQUEST IS ADMITTED!')
        return redirect("mainapp:index")

    def post(self, request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            subject = request.POST.get('subject')
            file = request.FILES.get('file')

            title = f'САЙТ - новое письмо. {subject}'
            email_body = f'Имя: {name}\nEmail: {email}\nСообщение: {message}\n'
            logger.error('SENDING EMAIL')
            mail = EmailMessage(title, email_body, settings.EMAIL_HOST_USER,
                                ['justitdevelopment@gmail.com'])  # justitdevelopment@gmail.com
            mail.attach(file.name, file.read(), file.content_type)
            mail.send()
        except Exception as e:
            logger.fatal('ERROR:', e)
        else:
            logger.error('EMAIL SENT!')
        return redirect("mainapp:index")

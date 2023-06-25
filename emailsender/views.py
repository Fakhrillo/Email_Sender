from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name, 
            'email': email,
            'subject': subject,
            'message': message,
        }
        
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])

        send_mail(data['subject'], message, data['email'], ['dombit1999@gmail.com'])
        return render(request, 'emailsender/success.html')

    return render(request, 'emailsender/index.html')
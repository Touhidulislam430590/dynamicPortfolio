from django.shortcuts import render
from .models import message

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        messageText = request.POST['message']

        insert = message(name = name, email = email, subject = subject, messageText = messageText)
        insert.save()
    return render(request, 'web/home.html')
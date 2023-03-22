from django.shortcuts import render
from .task import send_feedback_email_task

# Create your views here.

def feedback(request):
    if request.method == 'POST':
        print(request.POST['email'])
        email_address=request.POST['email']
        message=request.POST['msg']
        send_feedback_email_task.delay(email_address,message)
        print("iamin")
        return render(request,'feedback/success.html')

    return render(request,'feedback/feedback.html')

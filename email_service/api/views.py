# from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.mail import send_mail
# from django.conf import settings

# def send_mail_page(request):
#     context = {}

#     if request.method == 'POST':
#         address = request.POST.get('address')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         if address and subject and message:
#             try:
#                 send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
#                 context['result'] = 'Email sent successfully'
#             except Exception as e:
#                 context['result'] = f'Error sending email: {e}'
#         else:
#             context['result'] = 'All fields are required'
    
#     return render(request, "index.html", context)


from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            html_message = f"""
            <html>
                <head>
                    <style>
                        .container {{
                            font-family: Arial, sans-serif;
                            background-color: #f9f9f9;
                            padding: 20px;
                            border-radius: 10px;
                            max-width: 600px;
                            margin: 0 auto;
                            color: #333;
                        }}
                        .header {{
                            text-align: center;
                            padding: 10px 0;
                            background-color: #4CAF50;
                            color: white;
                            border-radius: 8px 8px 0 0;
                        }}
                        .content {{
                            padding: 20px;
                            background-color: white;
                            border-radius: 0 0 8px 8px;
                        }}
                        .footer {{
                            text-align: center;
                            font-size: 12px;
                            color: #aaa;
                            margin-top: 20px;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            <h1>{subject}</h1>
                        </div>
                        <div class="content">
                            <p>{message}</p>
                        </div>
                        <div class="footer">
                            <p>&copy; {settings.EMAIL_HOST_USER}. All rights reserved.</p>
                        </div>
                    </div>
                </body>
            </html>
            """

            try:
                send_mail(
                    subject,
                    message,  # Plain text for fallback
                    settings.EMAIL_HOST_USER,
                    [address],
                    html_message=html_message  # HTML content
                )
                context['result'] = 'Email sent successfully!'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required.'
    

    return render(request, "index2.html", context)

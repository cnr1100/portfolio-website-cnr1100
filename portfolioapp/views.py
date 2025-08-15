from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MessageForm

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)

            send_mail(
                subject = f"New Message from {msg.name}",
                message = f"Email: {msg.email}\n\nMessage:\n{msg.content}",
                from_email = 'developercnr1100@gmail.com',
                recipient_list = ['developercnr1100@gmail.com'],
                fail_silently = False
            )

            reply = EmailMessage(
                subject="Thank you for your Message",
                body=f"""<h2>Hello! {msg.name}</h2>
                <p>Thank you for reaching out. We've received your message and will respond at the earliest convenience.</p>
                <p>If further information is needed, feel free to contact me directly at Email : cnr1100@gmail.com</p>
                <p>Looking forward to your response.</p>
                <p>With Best Regards,</P>
                <p>Chowdary Narayana Rao</p>
                <hr>
                <div style="text-align: center;">
                <p>Chowdary Narayana Rao<br>
                 cnr1100@gmail.com</p>
                </div>""",
                 from_email='developercnr1100@gmail.com',
                 to=[msg.email]
            )
            reply.content_subtype = "html" 
            reply.send(fail_silently=False)


            msg.save()
            return redirect(f"{reverse('contact')}?submitted=true")
        else:
            print(form.errors)
    else:
        form = MessageForm()

    success = request.GET.get('submitted') == 'true'
    return render(request, 'index.html', {
        'form': form,
        'success': success
    })

from django.http import HttpResponse
from django.shortcuts import redirect, render
from sms.forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from sms.models import A2p_Body_Content, A2p_KloudSMS, A2p_Slider, A2pSMS_Feature, Boardcast_Bottom, Boardcast_Menu, Boardcast_Top, Boardcast_content, Contact_Headquarter, Contact_information, Home_Question, Home_SMS_Terminated, Home_Service, Home_body_content, Sms_Bottom_Content, Sms_Choose_U, Sms_Switch_Content, Sms_Switch_Manue, Voice_Otp_Manue, Voice_Question, Voice_otp_Content, VoiceOtp_Body, Wifi_Control_Manue, Wifi_bottom_Manue, Wifi_bottom_content, WifiSoulation_body


# Start home view ...
def home(request):
    homebody = Home_body_content.objects.all()[0:1]
    conntact = Contact_information.objects.all()[0:1]
    headQuater = Contact_Headquarter.objects.all()[0:1]
    homeTerminat = Home_SMS_Terminated.objects.all()[0:1]
    homeQuestion = Home_Question.objects.all()
    homeService = Home_Service.objects.all()

    context = {'homebody': homebody, 'conntact': conntact,
               'homeQuestion': homeQuestion,
               'homeService': homeService,
               'headQuater': headQuater,
               'homeTerminat': homeTerminat
               }
    return render(request, 'base/home.html', context)

# Start A2p view ...
def A2p(request):
    homeService = Home_Service.objects.all()
    conntact = Contact_information.objects.all()[0:1]
    headQuater = Contact_Headquarter.objects.all()[0:1]
    a2pobj = A2p_Body_Content.objects.all()[0:1]
    a2pslider = A2p_Slider.objects.all()
    a2pSms = A2pSMS_Feature.objects.all()
    a2pKloud = A2p_KloudSMS.objects.all()

    context = {'a2pobj':a2pobj, 'a2pslider':a2pslider, 'a2pSms':a2pSms,
               'homeService':homeService, 'conntact':conntact,
               'a2pKloud':a2pKloud,
               'headQuater': headQuater,
               }
    return render(request, 'base/a2p.html', context)

# Start smsSwitch view ...
def smsSwitch(request):
    homeService = Home_Service.objects.all()
    conntact = Contact_information.objects.all()[0:1]
    headQuater = Contact_Headquarter.objects.all()[0:1]
    switch = Sms_Switch_Content.objects.all()[0:1]
    choose = Sms_Choose_U.objects.all()[0:1]
    content = Sms_Bottom_Content.objects.all()
    manue = Sms_Switch_Manue.objects.all()

    context = {'switch': switch,
               'choose': choose,
               'content': content,
               'homeService': homeService,
               'manue': manue,
               'conntact': conntact,
               'headQuater': headQuater,
               }
    return render(request, 'base/sms-switch.html', context)

# Start voiceOtp view ...
def voiceOtp(request):
    homeService = Home_Service.objects.all()
    conntact = Contact_information.objects.all()[0:1]
    headQuater = Contact_Headquarter.objects.all()[0:1]
    question = Voice_Question.objects.all()
    contentOtp = Voice_otp_Content.objects.all()
    voiceManue = Voice_Otp_Manue.objects.all()
    boDy = VoiceOtp_Body.objects.all()

    context = {'question': question,
               'homeService': homeService,
               'contentOtp': contentOtp,
               'voiceManue': voiceManue,
               'boDy': boDy,
               'conntact': conntact,
               'headQuater': headQuater,
               }
    return render(request, 'base/voiceotp.html', context)

# Start wifiSolution view ...
def wifiSolution(request):
    homeService = Home_Service.objects.all()
    conntact = Contact_information.objects.all()[0:1]
    headQuater = Contact_Headquarter.objects.all()[0:1]
    wifyBody = WifiSoulation_body.objects.all()[0:1]
    conTrol = Wifi_Control_Manue.objects.all()
    BoTtom = Wifi_bottom_Manue.objects.all()
    conTent = Wifi_bottom_content.objects.all()[0:1]

    context = {'homeService':homeService,
               'wifyBody':wifyBody,
               'conTrol':conTrol,
               'BoTtom':BoTtom,
               'conTent':conTent,
               'conntact': conntact,
               'headQuater':headQuater,
               }
    return render(request, 'base/wifisolution.html', context)

#start boardCast view ...
def boardCast(request):
    homeService = Home_Service.objects.all()
    conntact = Contact_information.objects.all()[0:1]
    headQuater = Contact_Headquarter.objects.all()[0:1]
    boardcast = Boardcast_Menu.objects.all()
    boardcastop = Boardcast_Top.objects.all()[0:1]
    boardmeddle = Boardcast_content.objects.all()[0:1]
    boardbottom = Boardcast_Bottom.objects.all()

    context  = {'boardcast': boardcast,
                'boardcastop': boardcastop,
                'boardmeddle': boardmeddle,
                'boardbottom': boardbottom,
                'homeService': homeService,
                'conntact': conntact,
                'headQuater': headQuater,
                }
    return render(request, 'base/boardcast.html', context)


#start Contact_info view ...
def ContactInfo(request):
    homeService = Home_Service.objects.all()
    headQuater = Contact_Headquarter.objects.all()[0:1]
    conntact = Contact_information.objects.all()[0:1]
    contactfo = ContactForm()

    if request.method == 'POST':
        contactfo = ContactForm(request.POST)
        if contactfo.is_valid():
            contactfo.save()
            print(messages.success(request, "Contact Messages Successfull."))
            # return redirect('contact')
        else:
            print(contactfo.errors)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():   # Send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['messages']
            if contactfo.is_valid():
                contactfo.save()

                # Send an email
                subject = 'Contact Form Submission From Website'
                message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{body}'
                from_email = 'noreplay@gmail.com'  # Replace with your email
                recipient_list = ['tahsinhossen58@gmail.com']  # Replace with your recipient's email

                send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                
            else:
                print(messages.error(request, "Contact Messages Send Not Success."))
    else:
         form = ContactForm()

    context = {'conntact': conntact, 
               'homeService': homeService,
               'headQuater': headQuater,
               'contactfo': contactfo,
               }
    return render(request, 'base/contact.html', context)



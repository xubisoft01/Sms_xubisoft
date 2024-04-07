from django.db import models
from django.utils import timezone


#start Home Page models ...
class Home_body_content(models.Model):
    top_title1 = models.CharField(null=True, max_length=40)
    top_title2 = models.CharField(null=True, max_length=40)
    help_title = models.CharField(null=True, max_length=40)
    details = models.TextField(null=True)
    picture = models.ImageField(null=True, default="avatar.svg")
    bottom_title = models.CharField(null=True, max_length=50)
    bottom_details = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.top_title1
  
    class Meta:
        verbose_name_plural = "Home Body Content"
    
class Home_Service(models.Model):
    service_title = models.CharField(max_length=60, null=True)
    service_details = models.TextField(null=True)
    service_icone = models.CharField(max_length=60, null=True)
    
    def __str__(self):
        return self.service_title
    
    class Meta:
        verbose_name_plural = "Home Services"

class Home_Question(models.Model):
    question = models.CharField(max_length=150, null=True)
    answer = models.TextField(null=True)
    
    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = "Home Question"
    
class Home_SMS_Terminated(models.Model):
    Terminated_title = models.CharField(max_length=48, null=True)
    Satisfied_Clients = models.CharField(max_length=7, null=True)
    Increased_Traffic = models.CharField(max_length=7, null=True)
    Increased_Revenue = models.CharField(max_length=7, null=True)
    ANNUAL_TURNOVER = models.CharField(max_length=7, null=True)
    
    def __str__(self):
        return self.Satisfied_Clients
    
    class Meta:
        verbose_name_plural = "Home SMS Terminated"

#start Contact_info models ...
class Contact_information(models.Model):
    phone_no = models.CharField(null=True, max_length=20)
    email_address = models.EmailField(null=True, max_length=50)
    address = models.TextField(max_length=200, null=True)
    header_ph_no = models.CharField(null=True, max_length=20)
    header_email = models.EmailField(null=True, max_length=50)
    logo = models.ImageField(null=True, default="avatar.svg")
    
    def __str__(self):
        return self.email_address
    
    class Meta:
        verbose_name_plural = "Contact Information"
    
class Contact_U(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    messages = models.TextField(null=True)
    date_time = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contact Us"
    
class Contact_Headquarter(models.Model):
    title = models.CharField(null=True, max_length=75)
    phone_no = models.CharField(null=True, max_length=20)
    email_address = models.EmailField(null=True, max_length=50)
    branch_address = models.TextField(max_length=200, null=True)
    branch_ph_no = models.CharField(null=True, max_length=20)
    branch_email = models.EmailField(null=True, max_length=50)
    
    def __str__(self):
        return self.phone_no
    class Meta:
        verbose_name_plural = "Contact Headquarter"

#start a2p page models ...
class A2p_Body_Content(models.Model):
    title = models.CharField(max_length=50, null=True)
    details = models.TextField(null=True)
    contact = models.CharField(null=True, max_length=50)
    features = models.CharField(null=True, max_length=50)
    vas_title = models.CharField(null=True, max_length=50)
    work_title = models.CharField(null=True, max_length=50)
    work_bottom = models.CharField(null=True, max_length=50)
    details2 = models.CharField(null=True, max_length=200)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "A2p Body Content"

class A2p_Slider(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(null=True, default="avatar.svg")
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "A2p Slider"
    
class A2pSMS_Feature(models.Model):
    feature_title = models.CharField(max_length=60, null=True)
    feature_details = models.TextField(null=True)
    feature_icone = models.CharField(max_length=60, null=False)
    
    def __str__(self):
        return self.service_title
    class Meta:
        verbose_name_plural = "A2p SMS Feature"

class A2p_KloudSMS(models.Model):
    title = models.CharField(max_length=50, null=True)
    details = models.TextField(null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "A2p Kloud SMS"
    

#start sms-switch models ...
class Sms_Switch_Content(models.Model):
    title = models.CharField(max_length=50, null=True)
    details = models.TextField(null=True)
    picture = models.ImageField(null=True, default="avatar.svg")
    service_title = models.CharField(max_length=50, null=True)
    service_details = models.CharField(null=True, max_length=80)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "SMS Switch Contact"
    
class Sms_Choose_U(models.Model):
    title = models.CharField(max_length=50, null=True)
    point_1 = models.CharField(max_length=200, null=True)
    point_2 = models.CharField(null=True, max_length=150)
    point_3 = models.CharField(max_length=150)
    point_4 = models.CharField(max_length=150, null=False )
    point_5 = models.CharField(max_length=150, null=False)
    picture = models.ImageField(null=True, default="avatar.svg")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "SMS Choose Us"

class Sms_Switch_Manue(models.Model):
    title = models.CharField(max_length=60, null=True)
    details = models.TextField(null=True)
    icone = models.CharField(max_length=60, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "SMS Switch Manue"


class Sms_Bottom_Content(models.Model):
    title = models.CharField(max_length=50, null=True)
    details = models.TextField(null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "SMS Bottom Content"
    

#start Voice OTP Page models ...
class VoiceOtp_Body(models.Model):
    title = models.CharField(max_length=50, null=True)
    details = models.TextField(null=True)
    title2 = models.CharField(max_length=50, null=True)
    details2 = models.CharField(null=True, max_length=320)
    details3 = models.CharField(null=True, max_length=250)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Voice OTP Body"

class Voice_Otp_Manue(models.Model):
    title = models.CharField(max_length=60, null=True)
    details = models.TextField(null=True)
    icone = models.CharField(max_length=60, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Voice OTP Manue"

class Voice_otp_Content(models.Model):
    title = models.CharField(max_length=50, null=True)
    details = models.TextField(null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Voice OTP Content"

class Voice_Question(models.Model):
    question = models.CharField(max_length=150, null=True)
    answer = models.TextField(null=True)
    
    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = "Voice Questions"

# Start wifiSolution Model ...  
class WifiSoulation_body(models.Model):
    top_details = models.TextField(null=True)
    details2 = models.CharField(null=True, max_length=350)
    picture = models.ImageField(null=True, default="avatar.svg")
    mid_title = models.CharField(null=True, max_length=250)
    mid_details = models.CharField(null=True, max_length=350)
    picture2 = models.ImageField(null=True, default="avatar.svg")

    def __str__(self):
        return self.top_details
    
    class Meta:
        verbose_name_plural = "Wifi Soulation Body"
    
class Wifi_Control_Manue(models.Model):
    title = models.CharField(max_length=60, null=True)
    details = models.TextField(null=True)
    icone = models.CharField(max_length=60, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Wifi Control Manue"
    
class Wifi_bottom_Manue(models.Model):
    title = models.CharField(max_length=60, null=True)
    details = models.TextField(null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Wifi Bottom Manue"

class Wifi_bottom_content(models.Model):
    title = models.CharField(max_length=60, null=True)
    details = models.TextField(null=True)
    demo = models.CharField(max_length=60, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Wifi Bottom Content"

#start Boardcast models ...
class Boardcast_Menu(models.Model):
    title = models.CharField(max_length=50, null=True)
    details = models.TextField(null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Boardcast Manue"
    
class Boardcast_Top(models.Model):
    title = models.CharField(max_length=50, null=True)
    details = models.TextField(null=True)
    picture = models.ImageField(null=True, default="avatar.svg")
    site_title = models.CharField(max_length=50, null=True)
    site_details = models.TextField(null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Boardcast Top"

class Boardcast_content(models.Model):
    title = models.CharField(max_length=50, null=True)
    details = models.TextField(null=True)
    picture = models.ImageField(null=True, default="avatar.svg")
    demo = models.CharField(max_length=25, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Boardcast Content"
    
class Boardcast_Bottom(models.Model):
    title = models.CharField(max_length=50, null=True)
    details = models.TextField(null=True)
    picture = models.ImageField(null=True, default="avatar.svg")
    demo = models.CharField(max_length=25, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Boardcast Bottom"
    

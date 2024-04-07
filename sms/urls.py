
from django.urls import path
from sms import views

urlpatterns = [
    path('', views.home, name="home"),
    path('a2p/', views.A2p, name="a2p"),
    path('sms-switch/', views.smsSwitch, name="sms-switch"),
    path('voiceotp/', views.voiceOtp, name="voiceotp"),
    path('wifisolution/', views.wifiSolution, name="wifisolution"),
    path('boardcast/', views.boardCast, name="boardcast"),
    path('contact/', views.ContactInfo, name="contact"),
]

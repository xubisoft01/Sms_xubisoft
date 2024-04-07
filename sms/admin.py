from django.contrib import admin
from django.utils.html import format_html, mark_safe
from sms.models import A2p_Body_Content, A2p_KloudSMS, A2p_Slider, A2pSMS_Feature, Boardcast_Bottom, Boardcast_Menu, Boardcast_Top, Boardcast_content, Contact_Headquarter, Contact_U, Contact_information, Home_Question, Home_SMS_Terminated, Home_Service, Home_body_content, Sms_Bottom_Content, Sms_Choose_U, Sms_Switch_Content, Sms_Switch_Manue, Voice_Otp_Manue, Voice_Question, Voice_otp_Content, VoiceOtp_Body, Wifi_Control_Manue, Wifi_bottom_Manue, Wifi_bottom_content, WifiSoulation_body


#start Home Page Admin ...
class HomeBodyAdmin(admin.ModelAdmin):
    list_display = ('top_title1', 'top_title2', 'help_title', 'details', 'display_picture', 'bottom_title', 'bottom_details')

    def display_picture(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.picture.url)
    display_picture.short_description = 'Picture'

admin.site.register(Home_body_content, HomeBodyAdmin)

class HomeServiceAdmin(admin.ModelAdmin):
    list_filter = ('service_title',)
    list_per_page = 8
    list_display=('id', 'service_title', 'service_details', 'service_icone')
    
admin.site.register(Home_Service, HomeServiceAdmin)

class HomeQuestion_Admin(admin.ModelAdmin):
    list_filter = ('question',)
    list_display=('id', 'question', 'answer')

admin.site.register(Home_Question, HomeQuestion_Admin)

class HomeTerminated_Admin(admin.ModelAdmin):
    list_filter = ('Terminated_title',)
    list_editable= ('Satisfied_Clients',)
    
    list_display=('Terminated_title', 'Satisfied_Clients', 'Increased_Traffic', 'Increased_Revenue', 'ANNUAL_TURNOVER')

admin.site.register(Home_SMS_Terminated, HomeTerminated_Admin)

#start Contact_info Admin ...
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone_no', 'email_address', 'address', 'header_ph_no', 'header_email', 'display_logo')

    def display_logo(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.logo.url)
    display_logo.short_description = 'Logo'

admin.site.register(Contact_information, ContactAdmin)

class ContactAdminForms(admin.ModelAdmin):
    search_fields = ('name', 'email', 'messages')
    list_per_page = 8
    list_display = ('name', 'email', 'formatted_messages','date_time', 'is_read')  # Include 'is_read' in list_display

    # Define a custom admin action to mark messages as read
    actions = ['mark_as_read']

    def formatted_messages(self, obj):
        if obj.is_read:
            # If the message is read, do not apply bold formatting
            return obj.messages
        else:
            # If the message is not read, apply HTML formatting (bold) and mark it as safe
            formatted_message = format_html('<strong>{}</strong>', obj.messages)
            return mark_safe(formatted_message)
    formatted_messages.short_description = "Message"

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

admin.site.register(Contact_U, ContactAdminForms)

class HeadquaterAdmin(admin.ModelAdmin):
    list_display_links = ('phone_no',)
    list_display = ('title', 'phone_no', 'email_address', 'branch_address', 'branch_ph_no', 'branch_email')

admin.site.register(Contact_Headquarter, HeadquaterAdmin)

#start A2p Page Admin  ...
class A2pBodyAdmin(admin.ModelAdmin):
    list_display=('title', 'details', 'contact', 'features', 'vas_title', 'work_title', 'work_bottom', 'details2')

admin.site.register(A2p_Body_Content, A2pBodyAdmin)

class A2pSilderAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 5
    list_display = ('id', 'title', 'display_picture')

    def display_picture(self, obj):
        return format_html('<img src="{}" width="150" height="100" />', obj.picture.url)
    display_picture.short_description = 'Picture'

admin.site.register(A2p_Slider, A2pSilderAdmin)

class A2pSMSAdmin(admin.ModelAdmin):
    list_display=('id', 'feature_title', 'feature_details', 'feature_icone')

admin.site.register(A2pSMS_Feature, A2pSMSAdmin)

class A2pKloudSMSAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display=('id', 'title', 'details')

admin.site.register(A2p_KloudSMS, A2pKloudSMSAdmin)



#start Sms Switch Admin  ...
class SmsSwitchAdmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'display_picture', 'service_title', 'service_details')

    def display_picture(self, obj):
        return format_html('<img src="{}" width="75" height="75" />', obj.picture.url)
    display_picture.short_description = 'Picture'

admin.site.register(Sms_Switch_Content, SmsSwitchAdmin)

class SmsChooseAdmin(admin.ModelAdmin):
    list_display=('title', 'point_1','point_2', 'point_3', 'point_4', 'display_picture')

    def display_picture(self, obj):
        return format_html('<img src="{}" width="75" height="75" />', obj.picture.url)
    display_picture.short_description = 'Picture'

admin.site.register(Sms_Choose_U, SmsChooseAdmin)

class SMSwitchAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_per_page = 8
    list_display=('id', 'title', 'details', 'icone')

admin.site.register(Sms_Switch_Manue, SMSwitchAdmin)

class SmsBottomAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_per_page = 8
    list_display=('id', 'title', 'details')

admin.site.register(Sms_Bottom_Content, SmsBottomAdmin)

#start Voice OTP Admin...
class VoiceBodyAdmin(admin.ModelAdmin):
    list_display=('title', 'details', 'title2', 'details2', 'details3')

admin.site.register(VoiceOtp_Body, VoiceBodyAdmin)

class VoiceOtpAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display=('id', 'title', 'details', 'icone')

admin.site.register(Voice_Otp_Manue, VoiceOtpAdmin)

class VoiceContentAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display=('id', 'title', 'details')

admin.site.register(Voice_otp_Content, VoiceContentAdmin)

class Voice_Question_Admin(admin.ModelAdmin):
    list_filter = ('question',)
    list_per_page = 8
    list_display=('id', 'question', 'answer')

admin.site.register(Voice_Question, Voice_Question_Admin)

#start wifiSolution Admin...
class WifisoluationAdmin(admin.ModelAdmin):
    list_display = ('top_details', 'details2', 'display_image', 'mid_title', 'mid_details', 'display_image2')

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.picture.url)
    display_image.short_description = 'Image'

    def display_image2(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.picture2.url)
    display_image2.short_description = 'Image 2'
    
admin.site.register(WifiSoulation_body, WifisoluationAdmin)

class wifiControlAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_per_page = 7
    list_display=('id', 'title', 'details', 'icone')

admin.site.register(Wifi_Control_Manue, wifiControlAdmin)

class wifiBottomAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display=('id', 'title', 'details')

admin.site.register(Wifi_bottom_Manue, wifiBottomAdmin)

class wificobnAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display=('id', 'title', 'details', 'demo')

admin.site.register(Wifi_bottom_content, wificobnAdmin)

#start Boardcast Admin...
class BoradcastMenuAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display=('id', 'title', 'details')

admin.site.register(Boardcast_Menu, BoradcastMenuAdmin)

class BoradcasTopAdmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'display_picture', 'site_title', 'site_details')

    def display_picture(self, obj):
        return format_html('<img src="{}" width="75" height="75" />', obj.picture.url)
    display_picture.short_description = 'Picture'

admin.site.register(Boardcast_Top, BoradcasTopAdmin)

class BoradcastmeddelAdmin(admin.ModelAdmin):
    list_display = ('title', 'details', 'display_picture', 'demo')

    def display_picture(self, obj):
        return format_html('<img src="{}" width="75" height="75" />', obj.picture.url)
    display_picture.short_description = 'Picture'

admin.site.register(Boardcast_content, BoradcastmeddelAdmin)

class BoradcastBottomAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title', 'details', 'display_picture', 'demo')

    def display_picture(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.picture.url)
    display_picture.short_description = 'Picture'

admin.site.register(Boardcast_Bottom, BoradcastBottomAdmin)

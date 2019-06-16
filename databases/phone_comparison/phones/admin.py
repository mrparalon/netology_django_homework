from django.contrib import admin
from .models import Phone, PhoneApple, PhoneSamsung


class PhoneAdmin(admin.ModelAdmin):
    pass


class PhoneAppleAdmin(admin.ModelAdmin):
    pass


class PhoneSamsungAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phone, PhoneAdmin)
admin.site.register(PhoneApple, PhoneAppleAdmin)
admin.site.register(PhoneSamsung, PhoneSamsungAdmin)

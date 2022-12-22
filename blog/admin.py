from django.contrib import admin
from .models import * 


# Register your models here.
admin.site.register(EventModel)
admin.site.register(Menstruation)
admin.site.register(Ovulation)
admin.site.register(Intercourse)
admin.site.register(Pregnancy)
admin.site.register(Menopause)
admin.site.register(About)
admin.site.register(FAQ)
admin.site.register(Contact)



from django.contrib import admin

from .models import User, Lead, Agent , UserProfile, Category  

# class LeadAdmin(admin.ModelAdmin):
#     fields=(
#         'first_name',
#         'last_name',
#     )

admin.site.register(Category)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Lead)
admin.site.register(Agent)

# Register your models here.

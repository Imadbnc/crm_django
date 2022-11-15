from django.contrib import admin

from .models import User, Lead, Agent , UserProfile, Category, FollowUp

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
admin.site.register(FollowUp)

# Register your models here.

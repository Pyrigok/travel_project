# # -*- coding: utf-8 -*-
# from django.contrib import admin
# from django.contrib.auth import admin as auth_admin
# from django.contrib.auth.models import User

# from .models import UsProfile

# # зв'язує модель UsProfile з формою редагування моделі User в адмінці
# class UsProfileInline(admin.StackedInline): 
# 	model = UsProfile

# class UserAdmin(auth_admin.UserAdmin):
# 	inlines = (UsProfileInline,)

# # заміна існуючої адмін-форми
# admin.site.unregister(UserAdmin)
# admin.site.register(UserAdmin, User)
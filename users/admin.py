from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('email',)
    list_filter = ('email', 'is_active', 'is_staff', 'created_at', 'updated_at')
    ordering = ('-updated_at',)
    list_display = ('email', 'is_active', 'is_staff', 'created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        CustomUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )



# class UserAdminConfig(UserAdmin):
#     model = CustomUser
#     search_fields = ('email', 'user_name')
#     list_filter = ('email', 'user_name', 'is_active', 'is_staff')
#     ordering = ('-start_date',)
#     list_display = ('email', 'user_name',
#                     'is_active', 'is_staff')
#     fieldsets = (
#         (None, {'fields': ('email', 'user_name',)}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#         ('Personal', {'fields': ('about',)}),
#     )
#     formfield_overrides = {
#         CustomUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
#     }
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff')}
#          ),
#     )


admin.site.register(CustomUser, UserAdminConfig)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        if user.is_superuser is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if user.is_staff is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        user.save()
        return user
    
    
    def create_user(self, email, password=None):
        if email is None:
            raise TypeError('Users should have a Email')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    



# class CustomUserManager(BaseUserManager):
    # def create_superuser(self, email, user_name, first_name, password, **other_fields):
    #     other_fields.setdefault('is_staff', True)
    #     other_fields.setdefault('is_superuser', True)
    #     other_fields.setdefault('is_active', True)

    #     if other_fields.get('is_staff') is not True:
    #         raise ValueError(
    #             'Superuser must be assigned to is_staff=True.')
    #     if other_fields.get('is_superuser') is not True:
    #         raise ValueError(
    #             'Superuser must be assigned to is_superuser=True.')
    #     return self.create_user(email, user_name, first_name, password, **other_fields)


    # def create_user(self, email, user_name, first_name, password, **other_fields):
    #     if not email:
    #         raise ValueError(_('You must provide an email address'))

    #     email = self.normalize_email(email)
    #     user = self.model(email=email, user_name=user_name,
    #                       first_name=first_name, **other_fields)
    #     user.set_password(password)
    #     user.save()
    #     return user



AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    # is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        
        
        
# class CustomUser(AbstractBaseUser, PermissionsMixin):
    
#     email = models.EmailField(_('email address'), unique=True)
#     user_name = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=150, blank=True)
#     start_date = models.DateTimeField(default=timezone.now)
#     about = models.TextField(_(
#         'about'), max_length=500, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['user_name', 'first_name']

#     def __str__(self):
#         return self.user_name



































# class CustomAccountManager(BaseUserManager):
    
    
#     def create_superuser(self, email, user_name, password, **other_fields):
#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)


#         if other_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True.')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.')
#         return self.create_user(email, user_name, password, **other_fields)


#     def create_user(self, email, user_name, password, **other_fields):

#         if not email:
#             raise ValueError(_('You must provide an email address'))

#         email = self.normalize_email(email)
#         user = self.model(email=email, user_name=user_name,
#                           **other_fields)
#         user.set_password(password)
#         user.save()
#         return user



# class NewUser(AbstractBaseUser, PermissionsMixin):


#     email = models.EmailField(_('email address'), unique=True)
#     user_name = models.CharField(max_length=100, unique=True)
#     start_date = models.DateTimeField(default=timezone.now)
#     about = models.TextField(_(
#         'about'), max_length=500, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     # objects = CustomAccountManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


#     def __str__(self):
#         return self.user_name
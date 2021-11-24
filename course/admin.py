## @brief The models registered for the admin site

from django.contrib import admin
from .models import Student, Message, Notification, Resources,Membership,ChatMessage

x = Student, Message, Notification, Resources,Membership,ChatMessage
for model in x:
    admin.site.register(model)
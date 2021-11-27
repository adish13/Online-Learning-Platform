from django import forms
from .models import Assignment,Submission,Feedback, StudentBulkUpload
from course.models import Notification, Resources
from django.db import models
from django.contrib.auth.models import User
from TA.models import TeachingAssistant

# This class represents the form to add a notification.
class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = ['content']

# This class represents the form to add an assignment.
class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['name', 'description', 'file', 'weightage', 'deadline']

# This class represents the form to add a resource.
class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resources
        fields = ['title', 'file_resource']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content','marks']

class SendInviteForm(forms.Form):
    email_list = forms.CharField(widget=forms.Textarea)

class StudentBulkUploadForm(forms.ModelForm):
    class Meta:
        model = StudentBulkUpload
        fields = ['csv_file']

class AddTAForm(forms.Form):
    username = forms.CharField(max_length=100)
    can_add_students = forms.BooleanField(required=False)
    can_add_assignments = forms.BooleanField(required=False)
    can_add_resources = forms.BooleanField(required=False)
    can_notify = forms.BooleanField(required=False)
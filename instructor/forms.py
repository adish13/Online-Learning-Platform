from django import forms
from .models import Assignment,Submission,Feedback
from course.models import Notification, Resources

# This class represents the form to add a notification.
class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = ['content']

# This class represents the form to add an assignment.
class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        fields = ['name', 'description', 'file', 'deadline']

# This class represents the form to add a resource.
class ResourceForm(forms.ModelForm):

    class Meta:
        model = Resources
        fields = ['title', 'file_resource']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content','marks']
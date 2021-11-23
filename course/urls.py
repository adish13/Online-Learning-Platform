## @brief urls for the course app.

from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.urls import path

## @brief url patterns for the course app.
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<course_id>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^index/$', views.index, name='index'),
    url(r'^(?P<assignment_id>[0-9]+)/upload_submission/$', views.upload_submission, name='upload_submission'),
    url(r'^(?P<assignment_id>[0-9]+)/view_submissions/$', views.view_submissions, name='view_submissions'),
    url(r'^(?P<submission_id>[0-9]+)/view_feedback/$', views.view_feedback, name='view_feedback'),

    url(r'^(?P<course_id>[0-9]+)/view_assignments/$', views.view_assignments, name='view_assignments'),
    url(r'^(?P<course_id>[0-9]+)/view_resources/$', views.view_resources, name='view_resources'),
    path('send_message/',views.send_message,name='send_message'),
    path('view_messages/',views.view_messages,name='view_messages'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('delete/<message_id>',views.delete_message,name='delete')
]

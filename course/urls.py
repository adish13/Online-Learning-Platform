## @brief urls for the course app.

from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token
from . import cli_views

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
    url(r'^(?P<course_id>[0-9]+)/view_grades/$', views.view_grades, name='view_grades'),
    path('send_message/',views.send_message,name='send_message'),
    path('view_messages/',views.view_messages,name='view_messages'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('delete/<message_id>',views.delete_message,name='delete'),
    url(r'^(?P<course_id>[0-9]+)/(?P<is_it_res>\d)/(?P<id>[0-9]+)/(?P<done>\d)/mark_as_done/$', views.mark_as_done, name='mark_as_done'),
    
    path('join_course',views.join_course,name='join_course'),

    path('delete/<message_id>',views.delete_message,name='delete'),
    path('cli/courses/', cli_views.cli_courses, name='cli_courses'),
    path('cli/pending/', cli_views.cli_pending, name='cli_pending'),
    path('cli/courses_instructor/', cli_views.cli_courses_instructor, name='cli_courses_instructor'),

    path('cli/download_assignments/', cli_views.cli_download_assignments, name='cli_download_assignments'),
    path('cli/download_resources/', cli_views.cli_download_resources, name='cli_download_resources'),
    path('cli/list_tas/',cli_views.cli_list_tas,name='cli_list_tas'),
    path('cli/students/',cli_views.cli_students,name='cli_students')

]

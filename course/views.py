from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from .models import Student, Message, Notification, Resources, ChatMessage
from instructor.models import Assignment, Course, Feedback, Instructor,Submission
from django.shortcuts import render, redirect
from .forms import MessageForm, SubmissionForm, ChatMessageForm
import datetime
import mimetypes
from django.utils import timezone

## @brief view for the index page of the student.
#
# This view is called by /index url.\n
# It returns the student's homepage containing links to all the courses he is enrolled in and all the notifications.
@login_required
def index(request):
    student = Student.objects.get(user = request.user)
    courses = student.course_list.all()
    notifications = Notification.objects.filter(course__in = courses)
    return render(request, 'course/index.html', {'courses': courses, 'notifications': notifications})


# view for the detail page of the course.
# This view is called by <course_id>/detail url.\n
# It returns the course's detail page containing forum and links to all the assignments and resources.
@login_required
def detail(request, course_id):
    user = request.user
    student = Student.objects.get(user=request.user)
    courses = student.course_list.all()
    course = Course.objects.get(id=course_id)
    instructor = course.instructor
    messages = Message.objects.filter(course=course)
    form = MessageForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            message = form.save(commit=False)
            message.course = course
            message.sender = user
            message.time = datetime.datetime.now().strftime('%H:%M, %d/%m/%y') # get the current date,time and convert into string
            message.save()
            try:
                student = Student.objects.get(user=request.user)
                return redirect('course:detail', course_id)

            except:
                return redirect('instructor:instructor_detail', course.id)

    else:
        form = MessageForm()

        context = {
            'course': course,
            'user': user,
            'instructor': instructor,
            'student': student,
            'courses': courses,
            'messages': messages,
            'form': form
        }

        return render(request, 'course/detail.html', context)


# view for the assignments page of a course.
# This view is called by <course_id>/view_assignments url.\n
# It returns the webpage containing all the assignments of the course and links to download them and upload submissions.
@login_required
def view_assignments(request, course_id):
    course = Course.objects.get(id=course_id)
    assignments = Assignment.objects.filter(course=course)
    context = {
        'course' : course,
        'assignments' : assignments,
    }
    return render(request,'course/view_assignments.html',context)


# view for the resources page of a course.
# This view is called by <course_id>/view_resources url.\n
# It returns the webpage containing all the resources of the course and links to download them.
@login_required
def view_resources(request, course_id):
    course = Course.objects.get(id=course_id)
    resources = Resources.objects.filter(course=course)
    context = {
        'course' : course,
        'resources' : resources,
    }
    return render(request,'course/view_resources.html',context)


# view for the assignment's submission page.
# This view is called by <assignment_id>/upload_submission url.\n
# It returns the webpage containing a form to upload submission and redirects to the assignments page again after the form is submitted.
@login_required
def upload_submission(request, assignment_id):
    form = SubmissionForm(request.POST or None, request.FILES or None)
    assignment = Assignment.objects.get(id=assignment_id)
    course_id = assignment.course.id
    course = Course.objects.get(id=course_id)
    if form.is_valid():
        submission = form.save(commit=False)
        submission.user = request.user
        submission.assignment = assignment
        submission.time_submitted = datetime.datetime.now().strftime('%H:%M, %d/%m/%y')
        submission.save()
        return view_assignments(request, course_id)

    return render(request, 'course/upload_submission.html', {'form': form,'course': course})

@login_required
def view_submissions(request,assignment_id):
    assignment = Assignment.objects.get(id=assignment_id)
    submissions = Submission.objects.filter(user=request.user)
    course = assignment.course
    return render(request, 'course/view_submissions.html', {'submissions' : submissions,'course': course})

@login_required
def view_feedback(request,submission_id):
    feedback = Feedback.objects.filter(submission=submission_id)[0]
    submission = Submission.objects.get(id=submission_id)
    course = submission.assignment.course
    print(feedback)
    # content = feedback.content
    # marks = feedback.marks
    return render(request, 'course/view_feedback.html', {'feedback': feedback,'course': course})

@login_required
def send_message(request):
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.published_at = timezone.now()
            message.save()
            return redirect('view_messages')

    else:
        form = ChatMessageForm()
    return render(request, 'course/chat.html',{'form':form})

@login_required
def view_messages(request):
    inbox_messages = ChatMessage.objects.filter(receiver=request.user).order_by('published_at').reverse()[:4]
    sent_messages = ChatMessage.objects.filter(sender=request.user).order_by('published_at').reverse()[:4]
    return render(request, 'course/inbox.html', {'inbox_messages': inbox_messages, 'sent_messages':sent_messages})

@login_required
def dashboard(request):
    user = request.user 
    return render(request,'course/dashboard.html',{'user':user})

@login_required
def delete_message(request,message_id=None):
    message_to_delete=ChatMessage.objects.get(id=message_id)
    message_to_delete.delete()
    return redirect('view_messages')
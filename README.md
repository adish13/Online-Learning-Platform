# BruteForces_float_moodle
We primarily used django and html with styling for this website. For the cli part, we used django-rest framework.

For running the website locally you can simply run 
``` bash init.sh ```
If you want to do it stepwise, run the following commands :

Steps to install virtual environment and get the website running : 

```
python -m venv project-venv
source project-venv/bin/activate
pip install -r requirements.txt 
```
After this :
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
For the command line interface, run the following command after starting the server
```python cli_test.py ```

Our website has the following features :
1. Login and signup page
2. Join as Student, Instructor or TA
3. Forget Password
4. View Profile
5. Notifications
6. Forum
7. Timeline
8. DMs
9. Ability to disable forums
10. Assignments
11. Give feedback to assignments
12. Upload grades using csv files
13. View statistics of each assignment and overall course
14. Progress of the given course
15. Resources
16. Send Email Invitations to students to join courses
17. Invite TAs to join courses
18. Ability to assign different privileges to TAs
19. Deploying to Heroku
20. reset password
21. mark as done option
22. progress bar
23. to do list for instructor
24. notifications are clickable and take you to the corresponding item
25. sending email for updates
26. graphs are also clickable and can be downloaded
27. cli features

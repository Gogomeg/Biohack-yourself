
# Biohack yourself

Biohack yourself is a website built in Django using Python, JavaScript, CSS and HTML. It enables users to create and share health hacks with other users from around the world. It is targetted towards users who enjoy gaining knowledge about optimizing their health and life style. Users have the ability to create health hacks, and their own profile. They can upload images for use on their recipe or on their profile, link their personal youtube accounts and websites, and like and favorite other users recipes.

This is the fourth project for the Code Institute.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, email validation, and Full CRUD functionality for Health Hacks and User Profiles.

## 10 Epics were created which were then further developed into 33 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board here: 

Initial Django setup #1
User Profile #2
User sign in or sign out #3]
User recipes #4]
Recipe management #5]
Recipe searching #6
recipe viewing #7
recipe interaction #8
site owner objectives #9
recipe rating system #28

As a content creator I can choose an unique name for my story, and an unique URL will be generated, as well dates of update and create will be automatically generated and I will be able to add up number of likes for each post as well as status of the post (draft, published so that I can interact with my content.
As a site administrator I can approve or disapprove comments so that I can filter out objectionable comments.
As a site user I can register an account so that I can comment and like posts.
As a site user I can like or unlike a post so that I can interact with the content.
As a site user I can view a paginated list of posts so that I can easily select a post to view.
As a site user I can click on a post so that I can see the full content of it.

As a content creator I can see I have completed all the tasks related to a story to be published so that I can publish it.
Given that I am a registered user who is logged in, and has created a post
When I navigate to the post that I would like to delete
Then I have the option to delete the post
Given that I am a registered user who is logged in, has created a post and I am viewing the post I wish to delete
When I click the delete post button
Then I receive a confirmation window to confirm that I really want to delete the post
Given that I am a registered user who is logged in, has created a post, navigated to that post and clicked on the delete post button
When the confirmation window appears and I confirm the deletion
Then the post is deleted from the system
Given that I am a registered user, or a non registered user
When I navigate to a health hack page that I did not create
Then I do not have the option to delete the health hack
Given that I am a user on the site
When I navigate to the stories page
Then I am presented with a list of the stories available
Given that I am a user on the site
When I navigate to the stories page
And When I click on a story
Then I am presented with the full story details
Given that I am a user of the website
When I navigate to the site
Then I can access a search function to access related posts
As a user or creator of content I can choose a user id that is unique so that I will not be connected to a different user.

As a user, I can create, read, update or delete my own profile, so that login into the site.

### Potential User Stories

Create an account
View my own account
Edit my own account
Delete my account
Change my password
Reset my password if I forget it

As a User, I can view health hacks clearly, so that I can follow them easily.
Clear health hacks layout so its easy to identify which part is which
Easy to read on mobile devices
Easy to print out
Easy to view multiple health hacks at the same time - summary cards
As a User, I can make and receive comments on health hacks, so that I can ask questions, provide answers, or feedback.
Potential User Stories
Be able to ask questions
Be notified if someone comments on my health hack
Control the notifications
Be able to respond to comments
Report inappropriate comments to admin

As a stories user or creator I can log off the platform when I am done using it so that my data is protected against third party usage.

As a site owner I can restrict some features of the site to registered users so that it encourages people to sign up to the site.

##Acceptance Criteria 1
Given that a user is not registered or signed in,
When they view a post,
Then they are unable to save a story

##Acceptance Criteria 2
Given that a user is not registered or signed in,
When they look at the post options
Then they do not have the ability to create a health hack

##Acceptance Criteria 3
Given that a user is not registered or signed in,
When they look at a health hack
Then they are unable to provide a rating or comment

##Acceptance Criteria 4
Given that a user is not registered or signed in,
When they encounter functionality that requires them to be signed in
Then they are presented with a login or register button.

## Technologies

* Python
* Django
* HTML/CSS
* Bootstrap
* Google Cloud Platform
* Cloudinary
* ElephantSQL

## Resource Links used in the video

* https://cdnjs.com/libraries/bootstrap - CDN for bootstrap links
* https://getbootstrap.com/docs/5.2/getting-started/introduction - Bootstrap documentation
* https://uxwing.com/ - UX Wing icons
* https://django-allauth.readthedocs.io/en/latest/installation.html - Django-Allauth
* https://django-crispy-forms.readthedocs.io/en/latest/install.html - Crispy Forms
* https://pypi.org/project/django-reorder/ - Django Reordered
* https://docs.djangoproject.com/en/4.1/topics/class-based-views/mixins/ - Django Mixins
* https://cloudinary.com/ - Cloudinary
* https://django-ckeditor.readthedocs.io/en/latest/ - CKEditor
* https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html - Q Objects
* https://www.w3schools.com/howto/howto_css_modals.asp - CSS Modal

## Credits

All images for recipes were taken from [Unsplash](https://unsplash.com/license)

Recipe information was generated by [Chat GPT-3](https://chat.openai.com/chat)

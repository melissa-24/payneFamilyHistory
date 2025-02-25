from django.db import models
from django.db.models.deletion import CASCADE
from app.validUser import codes

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}

        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] ='Sorry that username has been taken please chose a different one'

        if len(form['password']) < 6:
            errors['password'] = 'Password must be at least 5 characters long'
        
        if form['password'] != form['confirm']:
            errors['password'] = 'Password do not match'

        if form['reg'] not in codes:
            errors['Please the Webmaster to gain access to this site']

        return errors
    
class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    objects = UserManager()

    userCreatedAt = models.DateTimeField(auto_now_add=True)
    userUpdatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username

class Member(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    generation = models.CharField(max_length=255)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName} {self.generation}'
    
class Event(models.Model):
    year = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    day = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    member = models.ForeignKey(Member, related_name="theMember", on_delete=CASCADE)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class EventMembers(models.Model):
    event = models.ForeignKey(Event, related_name="theEvent", on_delete=CASCADE)
    member = models.ForeignKey(Member, related_name="otherMember", on_delete=CASCADE)

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.event.title} {self.member.firstName}'


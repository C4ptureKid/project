from django.db import models

# Create your models here.
class Login(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Usertype = models.CharField(max_length=100)
    
class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Address = models.CharField(max_length=300)
    City = models.CharField(max_length=100)
    Pincode = models.CharField(max_length=100)
    Photo = models.CharField(max_length=100)
    Phone_No = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)

class Complaint(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Username = models.CharField(max_length=500)
    Complaint = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    Replay = models.CharField(max_length=500)

class Review(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Rating = models.CharField(max_length=100)
    Review = models.CharField(max_length=500)
    Date = models.CharField(max_length=100)

class Post(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Post = models.CharField(max_length=3000)
    Date = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)

class Comment(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    POST = models.ForeignKey(Post, on_delete=models.CASCADE)
    Comment = models.CharField(max_length=500)
    Date = models.CharField(max_length=100)

class Chat(models.Model):
    SENDER= models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_id')
    RECEIVER = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_id')
    Message = models.CharField(max_length=1000)
    Date = models.CharField(max_length=100)
    Seen = models.CharField(max_length=100)

class Request(models.Model):
    SENDER= models.ForeignKey(User, on_delete=models.CASCADE, related_name='receivedby_id')
    RECEIVER = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sendedby_id')
    Date = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)


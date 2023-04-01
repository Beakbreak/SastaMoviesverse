from django.db import models

class Movie(models.Model):
  id=models.IntegerField(null=False,primary_key=True)
  mean_rating=models.FloatField()
  number_of_ratings=models.IntegerField()
  title=models.CharField(max_length=255)
  War=models.IntegerField()
  Fantasy=models.IntegerField()
  Adventure=models.IntegerField()
  Horror=models.IntegerField()
  Documentary=models.IntegerField()
  Mystery=models.IntegerField()
  Drama=models.IntegerField()
  Children=models.IntegerField()
  Romance=models.IntegerField()
  IMAX=models.IntegerField()
  Comedy=models.IntegerField()
  Western=models.IntegerField()
  Animation=models.IntegerField()
  No_genre=models.IntegerField()
  Crime=models.IntegerField()
  Musical=models.IntegerField()
  Thriller=models.IntegerField()
  Sci_Fi=models.IntegerField()
  Action=models.IntegerField(null=True)
  Film_Noir=models.IntegerField()
  movieId=models.IntegerField(unique=True)  
    
  def __str__(self):
    return self.title
  

class Rating(models.Model):
  userId=models.IntegerField()
  movieId=models.IntegerField()
  rating=models.FloatField()
   
  def __str__(self):
    return str(self.userId)
    
class Suggestion(models.Model):
  userId=models.IntegerField()
  suggestion_1=models.IntegerField(default=-1)
  suggestion_2=models.IntegerField(default=-1)
  suggestion_3=models.IntegerField(default=-1)
  suggestion_4=models.IntegerField(default=-1)  
  suggestion_5=models.IntegerField(default=-1)
  suggestion_6=models.IntegerField(default=-1)          
  suggestion_7=models.IntegerField(default=-1)
  suggestion_8=models.IntegerField(default=-1)
  suggestion_9=models.IntegerField(default=-1)
  suggestion_10=models.IntegerField(default=-1)
  suggestion_11=models.IntegerField(default=-1)
  suggestion_12=models.IntegerField(default=-1)
  suggestion_13=models.IntegerField(default=-1)
  suggestion_14=models.IntegerField(default=-1)
  suggestion_15=models.IntegerField(default=-1)
  suggestion_16=models.IntegerField(default=-1)
  suggestion_17=models.IntegerField(default=-1)
  suggestion_18=models.IntegerField(default=-1)
  suggestion_19=models.IntegerField(default=-1)
  suggestion_20=models.IntegerField(default=-1)
  suggestion_21=models.IntegerField(default=-1)
  suggestion_22=models.IntegerField(default=-1)
  suggestion_23=models.IntegerField(default=-1)
  suggestion_24=models.IntegerField(default=-1)
  suggestion_25=models.IntegerField(default=-1)
  suggestion_26=models.IntegerField(default=-1)
  suggestion_27=models.IntegerField(default=-1)
  suggestion_28=models.IntegerField(default=-1)
  suggestion_29=models.IntegerField(default=-1)
  suggestion_30=models.IntegerField(default=-1)
  suggestion_31=models.IntegerField(default=-1)
  suggestion_32=models.IntegerField(default=-1)
  suggestion_33=models.IntegerField(default=-1)
  suggestion_34=models.IntegerField(default=-1)
  suggestion_35=models.IntegerField(default=-1)
  suggestion_36=models.IntegerField(default=-1)
  suggestion_37=models.IntegerField(default=-1)
  suggestion_38=models.IntegerField(default=-1)
  suggestion_39=models.IntegerField(default=-1)
  suggestion_40=models.IntegerField(default=-1)

  
  
  def __str__(self):
    return str(self.userId)
  
class userid(models.Model):
  username=models.TextField()
  userId=models.IntegerField()
  
  def __str__(self):
    return str(self.username)
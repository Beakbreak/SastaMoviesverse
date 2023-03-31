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
  movieId=models.IntegerField(models.ForeignKey("collaborative.Movie", to_field='movieId',on_delete=models.CASCADE))
  rating=models.FloatField()
   
  def __str__(self):
    return self.userId
    
class Suggestion(models.Model):
  userId=models.IntegerField()
  suggestion_1=models.IntegerField()
  suggestion_2=models.IntegerField(default=-1)
  suggestion_3=models.IntegerField(default=-1)
  suggestion_4=models.IntegerField()  
  suggestion_5=models.IntegerField()
  suggestion_6=models.IntegerField()          
  suggestion_7=models.IntegerField()
  suggestion_8=models.IntegerField()
  suggestion_9=models.IntegerField()
  suggestion_10=models.IntegerField()
  suggestion_11=models.IntegerField()
  suggestion_12=models.IntegerField()
  suggestion_13=models.IntegerField()
  suggestion_14=models.IntegerField()
  suggestion_15=models.IntegerField()
  
  
  def __str__(self):
    return str(self.userId) 
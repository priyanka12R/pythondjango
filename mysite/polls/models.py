from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Question(models.Model):
	def __str__(self):return self.question_text
	#this str special function will return question_text on Choice.Objects.all
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date_published')
# Create your models here.

class Choice(models.Model):
	def __str__(self):return self.choice_text
	#this str special function will return choice_text on Choice.Objects.all
	question=models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)

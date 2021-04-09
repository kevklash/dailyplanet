from django.db import models


class Journalist(models.Model):
	jouralist_name = models.CharField(max_length=100)

	def __str__(self):
		return self.jouralist_name


class Article(models.Model):
	date = models.DateField()
	headline = models.CharField(max_length=200)
	content = models.TextField()
	jouralist_name = models.ForeignKey(Journalist, on_delete=models.CASCADE)

	def __str__(self):
		return self.headline

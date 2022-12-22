from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 


# Create your models here.
class EventModel(models.Model):
	start_date = models.DateField()
	end_date = models.DateField(blank=True, null=True)
	notes = models.TextField(blank=True)

	def __str__(self):
		return f'{self.start_date} - {self.end_date}'


class Menstruation(EventModel):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	flow = models.CharField(max_length=20, choices=[
		("light", "Light"), 
		("medium", "Medium"),
		("heavy", "Heavy")])
	pain_level = models.CharField(max_length=20, choices=[
		("none", "None"),
		("mild", "Mild"),
		("moderate", "Moderate"),
		("severe", "Severe")])
	mood_changes = models.TextField(blank=True)
	cramps = models.CharField(max_length=20, choices=[
		("none", "None"),
		("mild", "Mild"),
		("moderate", "Moderate"),
		("severe", "Severe")])
	bloating = models.CharField(max_length=20, choices=[
		("none", "None"), 
		("mild", "Mild"),
		("moderate", "Moderate"),
		("severe", "Severe")])
	headaches = models.CharField(max_length=20, choices=[
		("none", "None"), 
		("mild", "Mild"),
		("moderate", "Moderate"), 
		("severe", "Severe")])
	medication = models.CharField(max_length=50, choices=[
		("none", "None"), 
		("NSAIDs", "NSAIDs"), 
		("hormonal contraceptives", "Hormonal Contraceptives"), 
		("other", "Other")])

	def __str__(self):
		return str(self.author)

	def get_absolute_url(self):
		return reverse('menstruation_detail', args=[self.pk])


class Pregnancy(EventModel):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	baby_count = models.PositiveSmallIntegerField()
	trimesters = models.PositiveSmallIntegerField()
	weight_gain = models.DecimalField(max_digits=5, decimal_places=2)
	doctor_visits = models.TextField(blank=True)
	fetal_movement = models.CharField(max_length=20, choices=[
		("none", "None"), 
		("mild", "Mild"), 
		("moderate", "Moderate"), 
		("strong", "Strong")])
	nutrition = models.CharField(max_length=50, choices=[
		("good", "Good"), 
		("fair", "Fair"), 
		("poor", "Poor")])
	medical_appointments = models.TextField(blank=True)

	def __str__(self):
		return str(self.author)

	def get_absolute_url(self):
		return reverse('pregnancy_detail', args=[self.pk])


class Menopause(EventModel):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	symptoms = models.TextField(blank=True)
	hormonal_changes = models.TextField(blank=True)
	lifestyle_changes = models.TextField(blank=True)

	def __str__(self):
		return str(self.author)

	def get_absolute_url(self):
		return reverse('menopause_detail', args=[self.pk])


class Ovulation(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField()
	fertility_window = models.CharField(max_length=20, choices=[
		("1 day before", "1 Day Before"),
		("2 days before", "2 Days Before"),
		("3 days before", "3 Days Before"),
		("day of", "Day of"),
		("1 day after", "1 Day After"),
		("2 days after", "2 Days After"),
		("3 days after", "3 Days After")])
	ovulation_method = models.CharField(max_length=50, choices=[
		("basal body temperature", "Basal Body Temperature"), 
		("ovulation predictor kit", "Ovulation Predictor Kit")])

	def __str__(self):
		return str(self.author)

	def get_absolute_url(self):
		return reverse('ovulation_detail', args=[self.pk])


class Intercourse(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField()
	method_of_birth_control = models.CharField(max_length=50, choices=[
		("condom", "Condom"), 
		("birth control pill","Birth Control Pill"), 
		("IUD", "IUD")])
	pregnancy_risk = models.CharField(max_length=20, choices=[
		("low", "Low"), 
		("medium", "Medium"), 
		("high", "High")])
	partner = models.CharField(max_length=50)
	relationship_status = models.CharField(max_length=20, choices=[
		("single", "Single"), 
		("dating", "Dating"), 
		("engaged", "Engaged"),
		("married", "Married")])
	lubrication = models.CharField(max_length=50, choices=[
		("none", "None"),
		("water-based","Water-Based"),
		("oil-based", "Oil-Based"), 
		("silicone-based", "Silicone-Based")])

	def __str__(self):
		return str(self.author)

	def get_absolute_url(self):
		return reverse('intercourse_detail', args=[self.pk])


class About(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(null=True, blank=True)

	class Meta:
		ordering = ['title',]
		verbose_name = 'About'
		verbose_name_plural = 'Abouts'

	def __str__(self):
		return str(self.title) 


class FAQ(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField(null=True, blank=True)

	class Meta:
		ordering = ['title',]
		verbose_name = 'FAQ'
		verbose_name_plural = 'FAQs'

	def __str__(self):
		return self.title 

class Contact(models.Model):
	address = models.CharField(max_length=100, null=True, blank=True)
	email = models.EmailField(null=True, blank=True)
	whatsapp = models.CharField(max_length=500, null=True, blank=True)
	facebook = models.CharField(max_length=500, null=True, blank=True)
	telegram = models.CharField(max_length=500, null=True, blank=True)
	instagram = models.CharField(max_length=500, null=True, blank=True)

	class Meta:
		verbose_name='Contact'
		verbose_name_plural = 'Contacts'

	def __str__(self):
		return f'{self.address} - {self.email}'




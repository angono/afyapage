from django import forms
from .models import *

# Menstruation
# Ovulation
# Intercourse
# Pregnancy
# Menopause

class PregnancyForm(forms.ModelForm):
	class Meta:
		model = Pregnancy
		fields = [
			'start_date',
			'end_date',
			'notes',
			'baby_count',
			'trimesters',
			'weight_gain',
			'doctor_visits',
			'fetal_movement',
			'nutrition',
			'medical_appointments'
		]


class MenopauseForm(forms.ModelForm):
	class Meta:
		model = Menopause
		fields = [
			'start_date',
			'end_date',
			'symptoms',
			'hormonal_changes',
			'lifestyle_changes'
		]


class IntercourseForm(forms.ModelForm):
	class Meta:
		model = Intercourse
		fields = [
			'date',
			'method_of_birth_control',
			'pregnancy_risk',
			'partner',
			'relationship_status',
			'lubrication'
		]


class OvulationForm(forms.ModelForm):
	class Meta:
		model = Ovulation
		fields = [
			'date',
			'fertility_window',
			'ovulation_method',
		]


class MenstruationForm(forms.ModelForm):
	class Meta:
		model = Menstruation
		fields = [
			'start_date',
			'end_date',
			'notes',
			'flow',
			'pain_level',
			'mood_changes',
			'cramps',
			'bloating',
			'headaches',
			'medication'
		]




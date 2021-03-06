from django.db import models

# Create your models here.

class CVentry(models.Model):
	# constants for the category simple choice
	JOB = 1
	EDUCATION = 2
	SKILL = 3
	CAT_CHOICES = (
		(JOB, 'Job'),
		(EDUCATION, 'Education'),
		(SKILL, 'Skill'),
	)


	# fields
	category = models.IntegerField(choices = CAT_CHOICES, default = JOB) # job, education, skill, 
	name = models.CharField(max_length = 50)

	#
	class Meta:
		abstract = True



class Skill(CVentry):
	# constants for level simple choice
	BASIC = 20
	GOOD = 50
	FLUENT = 70
	GODLIKE = 100
	LEVEL_CHOICES = (
		(BASIC,'Basic'),
		(GOOD,'Good'),
		(FLUENT,'Fluent'),
		(GODLIKE,'Godlike'),
	)

	# constants for subcategory simple choice
	LANGUAGE = 'LANG'
	TECHNICAL = 'TECH'

	SUBCAT_CHOICES = (
		(LANGUAGE,'Language'),
		(TECHNICAL,'Technical (?)')
	)

	def __init__(self, *args, **kwargs):
		self._meta.get_field('category').default = CVentry.SKILL
		super(Skill,self).__init__(*args,**kwargs)

	# fields
	subcategory = models.CharField(max_length = 4, choices = SUBCAT_CHOICES)
	level = models.IntegerField(choices = LEVEL_CHOICES, default = FLUENT, blank=True)

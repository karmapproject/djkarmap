

# PROVINCE_CHOICES = tuple(province)
# COUNTY_CHOICES = tuple(county)
# REGION_CHOICES = tuple(province)

GENDER_CHOICES = (
				('',''),
				('M','مرد'),
				('F', 'زن'),
			)

EDUCATION_CHOICES = (
				('',''),
				('HS','زیر دیپلم'),
				('BD', 'دیپلم'),
				('LS','لیسانس'),
				("MD", "فوق لیسانس"),
				('MBA', 'ام.بی.آ'),
				('PhD', 'دکترا'),						
			)

EMPLOYER_TYPE_CHOICES = (
			('University', 'University'), 
			('High School', 'High School'),
			('Middle School', 'Middle School'), 
			('Primary School', 'Primary School'),
			('Kindergarten', 'Kindergarten'),
			('Youth Language Center', 'Youth Language Center'),
			('Adult Language Center', 'Adult Language Center'),			
		)

POSITION_TYPE_CHOICES = (
			('Teacher', 'Teacher'),
			('Manager', 'Manager'),
			('Principal', 'Principal'),
			('Partner', 'Partner'), 									
		)

DESIRED_MONTHLY_SALARY_CHOICES = (
			('1000', '1000+'), 
			('2000', '2000+'), 
			('3000', '3000+'),								 
		)
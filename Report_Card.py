
#Midterm question 
def gpa(grades):
	running_sum = 0
	for grade in grades:
		running_sum = running_sum + grade
	return float(running_sum) / len(grades)


class_grades = []
class_names = []
number_classes = int(raw_input('How many classes did you take?  '))

for courses in range(number_classes):
	name = raw_input('What was the name of this class?  ')
	grade = int(raw_input('What was your grade?  '))
	class_names.append(name)
	class_grades.append(grade)
	
print 
print 'REPORT CARD:'
print 
for class_number in range (number_classes):
	print class_names[class_number], ' - ', class_grades[class_number]
	
print
print 'Overall GPA - ', gpa(class_grades)

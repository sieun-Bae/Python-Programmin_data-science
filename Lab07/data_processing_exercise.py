class Student:
	def __init__(self, name, hours, qpoints):
		self.name = name
		self.hours = float(hours)
		self.qpoints = float(qpoints)

	def getName(self):
		return self.name

	def getHours(self):
		return self.hours

	def getQPoints(self):
		return self.qpoints

	def gpa(self):
		return self.qpoints/self.hours

def makeStudents(infoStr):
	name, hours, qpoints = infoStr.split('\t')
	return Student(name, hours, qpoints)

def main():
	filename = input('Enter name of the grade file')

	with open(filename,'r') as infile:
		best = makeStudents(infile.readline())

		for line in infile:
			s = makeStudents(line)

			if s.gpa() > best.gpa():
				best = s

	print("The best student is: ", best.getName())
	print("Hours: ", best.getHours())
	print("GPA: ", best.gpa())

	if __name__ == "__main__":
		main()
main()
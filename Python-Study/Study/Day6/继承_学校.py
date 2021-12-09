class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []
        self.staffs = []

    def enroll(self,stu_obj):
        print("为学员%s办理入学注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        self.staffs.append(staff_obj)
        print("雇用新员工%s" % staff_obj.name)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher, self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ---- info of Teacher %s ----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        ''' % (self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching course [%s]" % (self.name,self.course))






class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,classroom):
        super(Student, self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.classroom = classroom

    def tell(self):
        print('''
        ---- info of Student %s ----
        Name:%s
        Age:%s
        Sex:%s
        Stu_ID:%s
        Classroom:%s
        ''' % (self.name,self.name,self.age,self.sex,self.stu_id,self.classroom))

    def study(self):
        print("%s is studying in classroom [%s]" % self.name,self.classroom)

    def pay_tuition(self,amount):
        print("%s has paid tuition for %s RMB" %(self.name,amount))


school = School("天津大学建筑学院","天津市南开区卫津路92号")

t1 = Teacher("Xinnan Zhang",40,"Male",20000,"Architectural Design")
t2 = Teacher("Yuhang Kong",60,"Male",50000,"Architectural Theory")

s1 = Student("Qiaozhi LI",26,"Male",3012206013,20120101)
s2 = Student("Anran Yu",25,"Female",3012206027,20120101)

t1.tell()
s1.tell()
school.enroll(s2)
school.enroll(s1)
school.hire(t2)

print(school.students)
print(school.staffs)
school.staffs[0].teach()

for stu in school.students:
    stu.pay_tuition(5000)
class student:
    marks = 10
    @classmethod
    def modify(cls, name):
        print(name,"score is",cls.marks)

student.modify("vidhi")
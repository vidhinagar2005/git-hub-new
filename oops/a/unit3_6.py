class office:
    count = 0
    def __init__(self):
        office.count +=1

    @staticmethod
    def employe():
        print("Employr number = ",office.count)

off = office()
off1 = office()
office.employe()
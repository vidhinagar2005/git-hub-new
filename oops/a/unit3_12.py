class bank(object):
    cash = 1000
    # @classmethod
    def access(cs):
        print(cs.cash)

class amdavad(bank):
    cash = 2000
    def access(cs):
        print(cs.cash)

class vadodra(bank):
    cash = 3000
    def access(cs):
        print(cs.cash)

a = amdavad()
a.access()
v = vadodra()
v.access()



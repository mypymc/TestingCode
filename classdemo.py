class Staff:
    def __init__ (self, pPosition, pName, pPay):
        self.position = pPosition
        self.name = pName
        self.pay = pPay
        print('Creating Staff Object')

    def __str__ (self):
        return "Position=%s, Name=%s, Pay=%d"%(self.position, self.name, self.pay)

    def calculatePay(self):
        prompt='\n Enter number of hrs worked for %s:'%(self.name)
        hours = input(prompt)
        prompt = '\n Enter the hourly rate for %s:'%(self.name)
        hourlyRate=input(prompt)
        self.pay = 'Pay for %s = %d'%(self.name,int(hours)*int(hourlyRate))
        return self.pay

    def __add__(self,other):
        return self.pay + other.pay



class MgmtStaff(Staff):
    def __init__(self,pName,pPay,pAllowance,pBonus):
        super(MgmtStaff,self).__init__('Manager',pName,pPay)
        self.allowance=pAllowance
        self.bonus=pBonus

    def calculatePay(self):
        basicPay=super().calculatePay()
        self.pay=basicPay+self.allowance
        return self.pay

    def calculatePerfBonus(self):
        prompt='Enter performance grade for %s: '%(self.name)
        grade=input(prompt)
        if(grade=='A'):
            self.bonus=10000
        else:
            self.bonus=0
        return self.bonus

class BasicStaff(Staff):
    def __init__(self,pName,pPay):
        super(BasicStaff,self).__init__('Basic',pName,pPay)
        

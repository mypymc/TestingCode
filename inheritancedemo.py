import classdemo

peter=classdemo.BasicStaff('Peter',0)
john=classdemo.MgmtStaff('John',0,10000,0)

print(peter)
print(john)

print('Peter\'s pay = ', peter.calculatePay())

print('John\'s pay= ', john.calculatePay())

print('John\'s performance bonus= ', john.calculatePerfBonus())

totalPay= john+peter
print('\n Total pay for both staff=', totalPay)

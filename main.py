from operations import add_Employee, view_Employee,delete_Employee,update_Employee

print("1.add emp")
print("2.view emp")
print("3.upadate emp")
print("4.delete emp")
print("5.exit")

choose = int(input ("enter option here :--"))

if choose == 1:
    add_Employee()

elif choose==2 :
    view_Employee() 

elif choose==3:
    update_Employee()      

elif choose==4:
    delete_Employee()

elif choose==5:
    print("Exit program Thank You...")    

else:
    print("Try again..")    
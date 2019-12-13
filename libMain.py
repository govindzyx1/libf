from libFun import *
yes="Y"
while yes=="Y":
    m=showOption()
    if m==1:
        libMember()
    elif m==2:
        addBook()
    elif m==3:
        bookTaken()
    elif m==4:
        bookSubmit()
    elif m==5:
        showLib()
    else:
        showMem()
        

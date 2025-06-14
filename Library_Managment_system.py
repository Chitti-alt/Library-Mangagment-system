import random as r

import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",passwd="Cj@29122005",database="batch1",charset="utf8")

cur=con.cursor()
def choices(cid):
    print('Your Choices : ')
    print('1. To add a Book')
    print('2. To see list of Books')
    print('3. To classify book by author')
    print('4. To classify books by its genre')
    print('5. To borrow a book')
    print('6  To return Book')
    print('7. To delete you library account')
    print('8. To exit Library')
    mo=int(input('Enter your choice: '))
    if mo==1:
        isbn=int(input('Enter ISBN of Book:'))
        ok=input('Enter the book you want to input:')
        mot=input('Enter the author of book you want to input:')
        genre=input('Enter genre of the book you want to input:')
        price=int(input('enter price of book:'))
        cur.execute('insert into library3(isbn,bookname,genre,author,price,issue_status) values({},"{}","{}","{}",{},"{}")'.format(isbn,ok,mot,genre,price,'notissued'))
        con.commit()
        print('Thank you for adding',ok,'book')
        return True
    if mo==2:
        cur.execute('select*from library3')
        nope=cur.fetchall()
        for mk in nope:
            print(mk)
        return True
    if mo==3:
        mon=input('What author do you want to classify with:')
        cur.execute("select * from library3 where (genre='{}') ".format(mon))
        lok=cur.fetchall()
        if lok==False:
            print('No such genre exists')
        for ml in lok:
            print(ml)
        return True
    if mo==4:
        don=input('What genre do want to classify the books with:')
        cur.execute("select * from library3 where (author='{}')".format(don))
        dope=cur.fetchall()
        if dope==False:
            print('No such author exists here')
        for i in dope:
            print(i)
        return True
    if mo==5:
        xy=input('Book u want:')
        cur.execute('update library3 set issue_status="issued" where bookname="{}"'.format(xy))
        con.commit()
        cur.execute('update library3 set issuerid="{}" where bookname="{}"'.format(cid,xy))
        con.commit()
        print(xy,'Book issued successfully by',mlo[0])
        return True
    if mo==6:
        lmn=input('Book to return:')
        cur.execute('update library3 set issue_status="notissued" where bookname="{}"'.format(lmn))
        cur.execute('update library3 set issuerid=NULL where bookname="{}"'.format(lmn))
        con.commit()
        print(lmn,'Book returned successsfully')
        return True
    if mo==7:
        delacc=input('Are you sure about deleting you account(y/n)')
        if delacc=='y' or delacc=='Y':
            cur.execute('delete  from customer_details where c_id="{}"'.format(cid))
            print('Account deleted successfully')
            con.commit()
            return False
        else:
            return True
    if mo==8:
        return False
        

def create_account():
    print()
    id1=[]
    name=input('Enter Your Full Name : ').title()
    contact=input('Enter Your Phone Number : ')
    username=input('Enter Username : ')
    passwd=input('Enter Password : ')
    cur.execute('select c_id from customer_details')
    dat=cur.fetchall()
    for i in dat:
        id1.append(i[0])
    while True:
        x=r.randint(10,99)
        c_id=str(x)
        if c_id in id1:
            continue
        else:
            break
    
    str1="insert into customer_details values('{}','{}','{}','{}','{}')".format(c_id,name,contact,username,passwd)
    cur.execute(str1)
    con.commit()
    print('++++++++++++++++++++ACCOUNT CREATED SUCCESSFULLY++++++++++++++++++++')
    return name
 
def login():
    count=0
    tr=0
    cur.execute('select * from customer_details')
    dat=cur.fetchall()
    while True:
        tr+=1
        if tr<4:
            username=input('Enter Your Username : ').lower()
            for i in dat:
                count+=1
                if username in i:
                        while username in i:
                            passwd=input('Enter Password : ')
                            if passwd in i:
                                print('ACCESS GRANTED')
                                str1="select name,c_id from customer_details where username='{}'".format(username)
                                cur.execute(str1)
                                data=cur.fetchall()
                                nme=data[0][0]
                                id1=data[0][1]
                                return nme , id1
                            else:
                                print('PASSWORD INCORRECT')
                                print('ENTER CORRECT PASSWORD')
                                print()
                else:
                     if count==len(dat):
                          print('ACCOUNT NOT FOUND')
                          print('Enter Valid Username')
                          print()
                          count=0
        else:
            print('You Have Tried Many Times')
            print('Account Not Found')
            print('Create New Account')
            break

        

        

print('Welcome to the library')
print('Do You Have an account in this library')
idask=input('ENTER Y for yes and N for no:')
if idask=='N' or idask=='n':
    print('Then is is required to create an account')
    print('to use our servives')
    create_account()
    mol=login()
    cdi=mol[0]
    while True:
        joke=choices(cdi)
        if joke==False:
            break
    print('Thank you for visiting the library')
elif idask=='Y' or idask=='y':
    print('Enter the login details')
    mlo=login()
    
    cid=mlo[0]
    while True:
        mal=choices(cid)
        if mal==False:
            break
    print('Thank you for visiting the library')


# Mini Project
# Platform for Social Media Start-Ups

from os import system , name
import mysql.connector

def clear():
    if name == 'nt':
        _ = system('cls')

def welcome_screen():
    print("\t\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("\t\n *                        W E L C O M E    T O                             * ")
    print("\t\n *        I S A A N A  :  F O R  T H E  S T R O N G  W I L L E D           * ")
    print("\t\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")

def seller_register():
    print("\n =======================================================================")
    s_uid = input("\n\t     User ID : ")
    s_name = input("\t     Name : ")
    s_email  = input("\t     Email ID : ")
    s_pno = int(input("\t     Phone Number : "))
    s_dob = input("\t     Date of Birth : ")
    s_passwd = input("\t     Password : ")
    s_address = input("\t     Address :  ")
    s_social_media = input("\t     Social Media Base : ")
    print("\n =======================================================================")
    print("\n\n Y O U R    A C C O U N T    H A S    B E E N    R E G I S T E R E D")
    cursor.execute('''INSERT INTO SELLER
    VALUES('{}','{}','{}',{},'{}','{}','{}','{}');'''.format(s_uid, s_name, s_email, s_pno, s_dob, s_passwd, s_address, s_social_media))
    mydb.commit()

def customer_register():
    print("\n =======================================================================")
    c_uid = input("\n\t     User ID : ")
    c_name = input("\t     Name : ")
    c_email = input("\t     Email ID : ")
    c_pno = int(input("\t     Phone Number : "))
    c_dob = input("\t     Date of Birth : ")
    c_passwd = input("\t     Password : ")
    c_address = input("\t Address : ")
    print("\n =======================================================================")
    print("\n\n Y O U R    A C C O U N T    H A S    B E E N    R E G I S T E R E D")
    cursor.execute('''INSERT INTO CUSTOMER
    VALUES('{}','{}','{}',{},'{}','{}','{}');'''.format(c_uid, c_name, c_email, c_pno, c_dob, c_passwd, c_address))
    mydb.commit()

def seller_login():
    global s_uid
    global s_passwd
    print("\n\n * * * * * * * * * * * * * * * * * * * * * * * * * ")
    s_uid = input("\n\t\t     User ID: " )
    s_passwd = input("\t\t     Password: ")  
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * ")
    cursor.execute("SELECT USERID, PASSWD FROM SELLER")
    check = cursor.fetchall()
    for i in check:
        if i[0] == s_uid and i[1] == s_passwd:
            break
        elif i[0] == s_uid and i[1] != s_passwd:
            print("Wrong Password")
            seller_login()
        else:
            continue    

def customer_login():
    global c_uid
    global c_passwd
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * ")
    c_uid = input("\n\t    User ID: ")
    c_passwd = input("\t    Password: ")
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * ")
    cursor.execute("SELECT C_UID, C_PASSWD FROM CUSTOMER")
    check = cursor.fetchall()
    for i in check:
        if i[0] == c_uid and i[1] == c_passwd:
            break
        elif i[0] == c_uid and i[1] != c_passwd:
            print("Wrong Password")
            customer_login()
        else:
            continue
    
def product():
    print("\n =======================================================================")
    p_name = input("\n\t    Product Name : ")
    p_price = int(input("\t    Price : ")) 
    p_quan = int(input("\t    Quantity : "))
    p_desc = input("\t    Description : ")
    p_id = input("\t    ID : ")
    print("\n =======================================================================")
    print("\n\n     Y O U R    P R O D U C T    H A S    B E E N    A D D E D        ")
    cursor.execute('''INSERT INTO PRODUCT
    VALUES('{}',{},{},'{}','{}');'''.format(p_name, p_price, p_quan, p_desc, p_id))
    mydb.commit()
    
def customer_credit_debit():
    print("\n ================================================================")
    c_no = int(input("\n\t    Card Number : "))
    c_name = input("\t    Name : ")
    c_cvv = int(input("\t    CVV : "))
    c_validthru = input("\t    Expiry Date : ")
    print("\n ================================================================")
    cursor.execute('''INSERT INTO C_CREDIT_DEBIT
    VALUES({},'{}',{},'{}');'''.format(c_no, c_name, c_cvv, c_validthru))
    mydb.commit()

def seller_net_banking():
    print("\n =======================================================================")
    print("\n\t  Enter Your Bank Details...")
    s_bname = input("\t    Bank Name : ")
    s_bbranch = input("\t    Branch Name : ")
    s_baccname = input("\t    Account Holder Name : ")
    s_baccno = input("\t    Account Number : ")
    s_ifsc = input("\t    IFSC Code : ")
    print("\n =======================================================================")
    cursor.execute('''INSERT INTO S_ACCOUNT
    VALUES('{}','{}','{}',{},'{}');'''.format(s_bname, s_bbranch, s_baccname, s_baccno, s_ifsc))
    mydb.commit()

def product_display():
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("\n *                             P R O D U C T S    D E T A I L S                                * ")
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    cursor.execute('''SELECT * FROM PRODUCT
    WHERE P_QUAN != 0;''')
    prods = cursor.fetchall()
    for i in prods:
        print("\n\n\t ID:" , i[4] , "\t NAME :" , i[0] , "\t PRICE : Rs" , i[1] , "\n\t DESCRIPTION :" , i[3])
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")

def seller_product_display():
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("\n *                             P R O D U C T S    D E T A I L S                                * ")
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    cursor.execute('''SELECT * FROM PRODUCT
    WHERE P_QUAN != 0;''')
    prods = cursor.fetchall()
    for i in prods:
        print("\n\n ID:" , i[4] , "\t NAME :" , i[0] , "\t PRICE : Rs" , i[1] , "\t Quantity : ", i[2] , "\n DESCRIPTION :" , i[3])
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")

def product_change():
    print("\n =======================================================================")
    p_id = input("\n\tID of the product you want to change : ")
    print("\tWhat do you want to change ?")
    print("\t1. To change the product name \n\t 2. To change the product description \n\t 3. To change the product quantity \n\t 4. To change the product price")
    n = int(input())
    if n == 1:
        print("\n\n\t Changing the product name.....")
        new_name = input("\n\t Enter the new name : ")
        print("\n Y O U R    P R O D U C T    N A M E    H A S   B E E N    C H A N G E D ")
        cursor.execute('''UPDATE PRODUCT
        SET P_NAME = '{}'
        WHERE P_ID = '{}';'''.format(new_name, p_id))
        mydb.commit()
    elif n == 2:
        print("\n\n\t Changing the product description....")
        new_desc = input("\n\t Enter new description : ")
        print("\n Y O U R    P R O D U C T    D E S C R I P T I O N   H A S   B E E N    C H A N G E D ")
        cursor.execute('''UPDATE PRODUCT
        SET P_DESC = '{}'
        WHERE P_ID = '{}';'''.format(new_desc, p_id))
        mydb.commit()          
    elif n == 3:
        print("\n\n\t Changing the product quantity...")
        new_quan = int(input("\n\t Enter new quantity : "))
        print("\n Y O U R    P R O D U C T    Q U A N T I T Y    H A S   B E E N    C H A N G E D ")
        cursor.execute('''UPDATE PRODUCT
        SET P_QUAN = {}
        WHERE P_ID = '{}';'''.format(new_quan, p_id))
        mydb.commit()
    elif n == 4:
        print("\n\n\t Changing the product price....")
        new_price = int(input("\n\t Enter new price : "))
        print("\n Y O U R    P R O D U C T    P R I C E    H A S   B E E N    C H A N G E D ")
        cursor.execute('''UPDATE PRODUCT
        SET P_PRICE = {}
        WHERE P_ID = '{}';'''.format(new_price, p_id))
        mydb.commit()
    else:
        print("Wrong Input!")
    print("\n =======================================================================")

def product_delete():
    print("\n =======================================================================")
    p_id = input("\n\t ID of the product you want to delete: ")
    print("\n     Y O U R    P R O D U C T    H A S    B E E N    D E L E T E D      ")
    print("\n =======================================================================")
    cursor.execute('''DELETE FROM PRODUCT
    WHERE P_ID = '{}';'''.format(p_id))
    mydb.commit()

def order():
    prod_number = 0
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("\n           P L A C E    A N     O R D E R          ")
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * ")
    test = True
    while test:
        id = input("Enter Product ID you want to add in the basket : ")
        qty = int(input("Enter Quantity : "))
        cursor.execute('''INSERT INTO BASKET (P_ID, P_NAME, P_PRICE)
        SELECT P_ID, P_NAME, P_PRICE FROM PRODUCT
        WHERE PRODUCT.P_ID = '{}';'''.format(id))
        mydb.commit()
        cursor.execute('''UPDATE BASKET
        SET P_QUAN = {}
        WHERE P_ID = '{}';'''.format(qty, id))
        mydb.commit()
        a = int(input("Want to enter more items in the basket? ( 1 = yes , 0 = no ): "))
        if a == 1:
            test = True
        else:
            test = False 
        prod_number+=1
    print("\n Y O U R    O R D E R   H A S    B E E N    P L A C E D ! ")
      
def basket_display():
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("\n *                           P R O D U C T S    D E T A I L S                                  *")
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    cursor.execute('''SELECT * FROM BASKET
    WHERE P_QUAN != 0;''')
    prods = cursor.fetchall()
    for i in prods:
        print("\n\t ID : " , i[0], "\tName:" , i[1] , "\tPrice:" , i[2] , "\tQuantity:" , i[3])
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

def basket():
    basket_display()
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("\n *                                     B A S K E T                                             * ")
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")   
    print("\n\t 1. To change the Quantity of Product \n\t 2. To Delete the product \n\t 3. To go to Checkout \n\t")
    n = int(input("\n\n Enter your choice : "))
    if n == 1 :
        p_id = input("\n\t Enter the Product ID : ")
        print("\t Changing the Quantity of Product.....")
        new_qnty = input("\t Enter the new Quantity : ")
        cursor.execute('''UPDATE BASKET
        SET P_QUAN = {}
        WHERE P_ID = '{}';'''.format(new_qnty, p_id))
        mydb.commit()
        cursor.execute('''UPDATE PRODUCT
        SET P_QUAN = P_QUAN - {}
        WHERE P_ID = '{}';'''.format(new_qnty, p_id))
        mydb.commit()
        basket()
    elif n == 2:
        p_id = int(input("\t Enter the Product ID : "))
        print("\t Deleting the product....")
        cursor.execute('''DELETE FROM BASKET
        WHERE P_ID = '{}';'''.format(p_id))
        mydb.commit()
        basket()     
    elif n == 3:        
        return
    else:
        print("\n\t W R O N G    I N P U T ! ")

def money():
    cursor.execute('''SELECT SUM(P_PRICE*P_QUAN) FROM BASKET;''')
    val = cursor.fetchall()
    tot = int(val[0][0])
    print(tot)
    return tot

def receipt():
    tot = money()
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("\n *                           R E C E I P T                           * ")
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    cursor.execute("SELECT * FROM BASKET;")
    prods = cursor.fetchall()
    for i in prods:
        print("\n\tName:", i[1] , "\tPrice:" , i[2] , "\tQuantity:" , i[3])
    print("\n\n\t\tYour Total Amount : " , tot )
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    
def delivery_address():
    print("\n =======================================================================")
    print("\n\t Enter your Delivery Address Details : ")
    flat_no = int(input("\t Flat Number : "))
    bldg_name = input("\t Building Name : ")
    strt_name = input("\t Street : ")
    area = input("\t Area : ")
    city = input("\t City : ")
    state = input("\t State : ")
    landmark = input("\t Landmark : ")
    print("\n =======================================================================")

def payment():
    print("\n =======================================================================")
    print("\n\t 1. Cash On Delivery \n\t 2. Online Payment ")
    a = int(input("\n\t Choose n Payment Option : "))
    if a == 1 :
        clear()
        delivery_address()
        clear()
        receipt()
        print("\n Your Order Has Been Placed. It will get delivered by a week! ")
        print(" \n\n    T H A N K    Y O U    F O R   S H O P P I N G   W I T H    U S   !")
    if a == 2 :
        clear()
        print("\n 1. Credit Card \n 2. Debit Card. ")
        c = int(input("\n\n Choose your Card : "))
        customer_credit_debit()
        clear()
        delivery_address()
        clear()
        receipt()
        print("\n Your Order Has Been Placed. It will get delivered by a week! ")
        print(" \n\n    T H A N K    Y O U    F O R   S H O P P I N G   W I T H    U S   !")
    print("\n =======================================================================")
    cursor.execute('''DELETE FROM BASKET;''')
    mydb.commit()

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "kavya", database = "PP_MiniProject")
cursor = mydb.cursor()

def __main__():
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("\n *                    1. Customer                          * ")
    print("\n *                    2.  Seller                           * ")
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    a = int(input("\n\n\t Enter Your Option : "))
    if a == 1 :
        clear()
        print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("\n *                    1. Login                             * ")
        print("\n *                    2. Register                          * ")
        print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        b = int(input("\n\n\t Enter Your Option : "))
        if b == 1 :
            clear()
            customer_login()
            clear()
            welcome_screen()
            print("\n")
            product_display()
            print("\n")
            order()
            clear()
            basket()
            clear()
            receipt()
            payment()
        elif b == 2 :
            clear()
            customer_register()
            clear()
            welcome_screen()
            print("\n")
            product_display()
            print("\n")
            order()
            clear()
            basket()
            clear()
            receipt()
            payment()
        else:
            clear()
            print("\n\n\t   W R O N G    I N P U T ")
    elif a == 2 :
        clear()
        print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        print("\n *                    1. Login                             * ")
        print("\n *                    2. Register                          * ")
        print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
        c = int(input("\n\n    Enter Your Option : "))
        if c == 1:
            clear()
            seller_login()
            clear()
            welcome_screen()
            while(True):
                print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
                print("\n *                1. Add Product                           * ")
                print("\n *                2. Change Product Details                * ")
                print("\n *                3. Delete Product                        * ")
                print("\n *                4. Display Product List                  * ")
                print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
                d = int(input("\n\n\t Enter Your Option : "))
                if d == 1 :
                    clear()
                    product()
                    ch = int(input("Would you like to continue? (1:Yes ; 0:No) : "))
                    if ch == 1:
                        continue
                    else:
                        break
                elif d == 2 :
                    clear()
                    product_change()
                    ch = int(input("Would you like to continue? (1:Yes ; 0:No) : "))
                    if ch == 1:
                        continue
                    else:
                        break
                elif d == 3 :
                    clear()
                    product_delete()
                    ch = int(input("Would you like to continue? (1:Yes ; 0:No) : "))
                    if ch == 1:
                        continue
                    else:
                        break
                elif d == 4 :
                    clear()
                    product_display()
                    ch = int(input("Would you like to continue? (1:Yes ; 0:No) : "))
                    if ch == 1:
                        continue
                    else:
                        break
                else:
                    print("\n\n\t  W R O N G    I N P U T ")
                    ch = int(input("Would you like to continue? (1:Yes ; 0:No) : "))
                    if ch == 1:
                        continue
                    else:
                        break
        elif c == 2 :
            clear()
            seller_register()
            seller_net_banking()
            clear()
            welcome_screen()
            while(True):
                print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
                print("\n *                 1. Add Product                          * ")
                print("\n *                 2. Change Product Details               * ")
                print("\n *                 3. Delete Product                       * ")
                print("\n *                 4. Display Product List                 * ")
                print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
                d = int(input("\n\n\t Enter Your Option : "))
                if d == 1 :
                    clear()
                    product()
                    ch = int(input("Would you like to continue? (1:Yes ; 0:No) : "))
                    if ch == 1:
                        continue
                    else:
                        break
                elif d == 2 :
                    clear()
                    product_change()
                    ch = int(input("Would you like to continue? (1:Yes ; 0:No) : "))
                    if ch == 1:
                        continue
                    else:
                        break
                elif d == 3 :
                    clear()
                    product_delete()
                    ch = int(input("Would you like to continue? (1:Yes ; 0:No) : "))
                    if ch == 1:
                        continue
                    else:
                        break
                elif d == 4 :
                    clear()
                    seller_product_display()
                    ch = int(input("Would you like to continue? (1:Yes ; 0:No) : "))
                    if ch == 1:
                        continue
                    else:
                        break
                else:
                    print("\n\n\t  W R O N G    I N P U T ")
                    ch = int(input("Would you like to continue? (1:Yes ; 0:No) : "))
                    if ch == 1:
                        continue
                    else:
                        break
    else:
        print("\n\n\t W R O N G   I N P U T ")

__main__()
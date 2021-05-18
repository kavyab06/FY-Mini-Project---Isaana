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

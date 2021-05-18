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

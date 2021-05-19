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
    
def product_display():
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    print("\n *                             P R O D U C T S    D E T A I L S                                * ")
    print("\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
    cursor.execute('''SELECT * FROM PRODUCT
    WHERE P_QUAN != 0;''')
    prods = cursor.fetchall()
    for i in prods:
        print("\n\n\tID:" , i[4] , "\tNAME :" , i[0] , "\tPRICE : Rs" , i[1] , "\n\tDESCRIPTION :" , i[3])
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

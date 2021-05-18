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

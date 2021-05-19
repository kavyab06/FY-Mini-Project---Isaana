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

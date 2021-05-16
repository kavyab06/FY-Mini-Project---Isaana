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

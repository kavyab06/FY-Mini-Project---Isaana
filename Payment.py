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

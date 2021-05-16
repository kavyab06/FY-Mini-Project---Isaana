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

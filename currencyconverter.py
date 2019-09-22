from forex_python.converter import *
from forex_python.bitcoin import *
from decimal import *


#Calling necessary functions
r = CurrencyRates()
c = CurrencyCodes()
b = BtcConverter()

print("Welcome to the Currency Coverter \nHere you can find: \n1) Currency Conversion(CCR) \n2) Currency Exchange Rate(CXR) \n3) Bitcoin Conversion(BCR) \n4) BitCoin Exchange Rate(BXR)")

#Gathering what the user wants
action = input("Lets begin by what you would like to do today: ")
action = action.upper()

#Class for currency conversion
class CCR:
    def __init__(self, first_curr, sec_curr, amount):
        self.con_amt = r.convert(first_curr, sec_curr, amount)
    def printamount(self):
        print(amount," in ",sec_curr," is = ", c.get_symbol(sec_curr), self.con_amt)

#Class for currency exchange
class CXR:
    def __init__(self, first_curr, sec_curr):
        self.cxr_rate = r.get_rate(first_curr, sec_curr)
    def printexrate(self):
        print("The exchange rate between ",first_curr," and ", sec_curr," is = ",self.cxr_rate)
        
#Class for BitCoin Conversion        
class BCR:
    def __init__(self, amount, curr):
        self.btc_amt = b.convert_to_btc(amount, curr)
    def printbcramt(self):
        print ("You have ",b.get_symbol(),self.btc_amt)

#Class for BitCoin exchange
class BXR:
    def __init__(self, curr):
        self.btc_ex = b.get_latest_price(curr)
    def printbtcer(self):
        print ("The exchange rate between ",curr," and ",b.get_symbol()," is = ",self.btc_ex)



#Currency Converstion
if (action == "CCR"):
    first_curr = input("Enter the currency to convert from in its currency code:")
    sec_curr = input("Enter the currency to convert to in its currency code:")
    amount = input("Enter amount to convert:")
    c1 = CCR(first_curr, sec_curr, Decimal(amount))
    c1.printamount()
#Currency Exchange
elif (action == "CXR"):
    first_curr = input("Enter the base currency code:")
    sec_curr = input("Enter the exchange its currency code:")
    c2 = CXR(first_curr, sec_curr)
    c2.printexrate()
#BitCoin Conversion
elif (action == "BCR"):
    curr = input("Enter currency code to be converted into BTC: ")
    amount = input("Enter the amount to convert: ")
    c3 = BCR(amount, curr)
    c3.printbcramt()
#BitCoin Exchange
elif (action == "BXR"):
    curr = input("Enter currency code you want find the exchange rate for: ")
    c4 = BXR(curr)
    c4.printbtcer()
else:
    print("Please assign a proper choice")
    
        
        
        
    

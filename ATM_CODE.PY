def lenguage():
    print("wecome to the ICICI ","\U0001f600")
    user=int(input("choice language \n1.ENGLISH \n2.HINDI ="))
    if user==1:
        return ("enlish")
    else:
        return ("hindi")
def pin_code():
    if lenguage==2:
        i=0
        while i<3:
            pin=int(input("enter your four digit pin number"))
            if pin==1234:
                print("your pin is correct")
                break
            else:
                print("your pin is incorrect try again!")
            i+=1
    else:
        i=0
        while i<3:
            pin=int(input("अपना चार नंबर का पिन दर्ज करें"))
            if pin==1234:
                print("आपका पिन सही है ")
                break
            else:
                print("फिर से अपना पिन डालें!")
            i+=1
        
def options():
    if lenguage ==1:
        balance=20000
        print('please press 1 for your balance')
        print('please press 2 for your withdrawl')
        print('please press 3 for your pay in')
        print('please press 4 for your return card')
        option=int(input('what would you like to choose='))
        if option==1:
            print('your balance is $',balance)
        elif option==2:
            withdrawl=float(input('how much would you like to withdraw amount?'))
            if withdrawl in [100,200,300,400,600,800,1000]:
                balance=balance -withdrawl
                print('your balance is now $ ',balance)
        elif option==3:
            pay_in=float(input('how much would you like to pay in ?:'))
            balance = balance +pay_in
            print('your balance is now $',balance)
        elif option==4:
            print('please wait while card is returned ....')
            print('thank you for banking with ICICI ')
    else:
        balance=20000
        print('कृपया अपने पैसे की जांच के लिए 1 दबाएं')
        print('कृपया अपने पैसे निकालने के लिए 2 दबाएं')
        print('कृपया अपने भुगतान के लिए 3 दबाएं')
        print('कृपया अपने रिटर्न कार्ड के लिए 4 दबाएं')
        option=int(input('आप क्या चुनना चाहेंगे ='))
        if option==1:
            print('आपका शेष $ है',balance)
        elif option==2:
            withdrawl=float(input('आप कितनी राशि निकालना चाहेंगे?'))
            balance=balance -withdrawl
            print('आपका शेष अब $ है ',balance)
        elif option==3:
            pay_in=float(input('आप कितना भुगतान करना चाहेंगे?:'))
            balance = balance +pay_in
            print('आपका शेष अब $ है',balance)
        elif option==4:
            print('कृपया प्रतीक्षा करें जबकि कार्ड वापस आ गया है ....')
            print('ICICI बैंक की तरफ से धन्यवाद कृपया दोबारा विजिट करें')
lenguage()
pin_code()
options()
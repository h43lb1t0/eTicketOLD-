from source.ticket import main
from source.links import URL_BALL, URL_Party
from source.qrCoder import qrCode
from source.pdf import pdf

#imports all required files into main.py so that they can be executed from there.#

#Creates a function to query which event the tickets are for.#
#It also checks whether the user has made a valid entry. If not, the user will be informed.#
def eventt():
    event = input('Are the tickets for the ball (b) or the afterparty (a)? Enter the according letter: ')
    if event == 'a':
        return event
    if event == 'b':
        return event
    else:
        print('Please enter only the relevant letter.')
        eventt()
        
event = eventt() #The input of the user from the function 'eventt' is stored in the variable 'event#

#The user is asked for all details necessary to book the tickets.#

AMOUNT = int(input('Number of tickets to be ordered: '))
print("")
ENTRY_URL = input('Event URL: ')
print("")
EVENTNR = input('Event No.: ')
print("")
EMAIL = input('email address: ')
print("")
main(ENTRY_URL,EVENTNR,AMOUNT,EMAIL)
print("")
print('The wiki instructions should now be followed')
try:
    input("Press enter to continue")
except SyntaxError:
    pass
#Creates a function that calls the function to create the qr-codes. The function only needs one input from the user.#
def PartyQR(URL_Party):
    URL = URL_Party
    evt = 'source/qr/qr_party/Party_' #defines the location where the qr-code is stored.#
    qrCode(URL,evt)
#Creates a function that calls the function to create the qr-codes. The function only needs one input from the user.#
def BallQR(URL_BALL):
    URL = URL_BALL
    evt = 'source/qr/qr_ball/ball_' #defines the location where the qr-code is stored.#
    qrCode(URL,evt) 
#automatic query if the user has selected that the tickets are for the afterparty#
if event == 'a':
    if AMOUNT == len(URL_Party): #check that the list of links to create the qr-codes matches the number of tickets requested.#
        print('List complete')
        PartyQR(URL_Party)
    else: #asks the user to 'call over' the list if it does not match the desired quantity#
        print('The number of links does not match the amount ordered.')
        try:
            input("When the list is corrected press Enter")
        except SyntaxError:
            pass
        PartyQR(URL_Party)
#automatic query if the user has selected that the tickets are for the Abiball#
if event == 'b':
    if AMOUNT == len(URL_BALL): #check that the list of links to create the qr-codes matches the number of tickets requested.#
        print('List complete')
        BallQR(URL_BALL)
    else: #asks the user to 'call over' the list if it does not match the desired quantity#
        print('The number of links does not match the amount ordered.')
        try:
            input("When the list is corrected press Enter")
        except SyntaxError:
            pass
        BallQR(URL_BALL)
print('')

#Creates a function that calls the function to create the afterparty tickets. The function allows you to create the tickets with the given coordinates or to use user created tickets with only two inputs.#

def vorlage_Afterparty(AMOUNT,cords):
    cords = cords
    input_file = 'source/vorlagen/Afterparty_ticket.pdf' #defines where the template for the ticket can be found#
    output_dic = 'source/Tickets/afterparty_tickets/Afterparty_' #defines where the finished tickets should be stored.#
    qr_dic = 'source/qr/qr_party/Party_qr_' #defines where the qr-codes can be found.#
    pdf(AMOUNT,cords,input_file,output_dic,qr_dic) #calls the function to create the tickets.#

#Creates a function that calls the function to create the Abiball Tickets. The function allows you to create the tickets with the given coordinates or to use the user created tickets with only two inputs.# 

def vorlage_Ball(AMOUNT,cords):
    cords = cords
    input_file = 'source/vorlagen/Abiball_ticket.pdf'
    output_dic = 'source/Tickets/ball_tickets/Ball_'
    qr_dic = 'source/qr/qr_ball/ball_qr_'
    pdf(AMOUNT,cords,input_file,output_dic,qr_dic)

pdf_method = int(input('use fix cords (1) or use your own cords (2): '))

def usr_cords():
    x1= input('X1 Wert')
    x2= input('X2 Wert')
    x3= input('X3 Wert')
    x4= input('X4 Wert')
    cords = (int(x1),int(x2),int(x3),int(x4))
    return cords


if pdf_method == 1:
    if event == 'b':
        cords = (900,20,550,120)
        vorlage_Ball(AMOUNT,cords)

    elif event == 'a':
        cords = (450,20,550,120)
        vorlage_Afterparty(AMOUNT,cords)

elif pdf_method == 2:
        if event == 'b':
            cords = usr_cords()
            #vorlage_Ball(AMOUNT,cords)

        elif event == 'a':
            cords = usr_cords()
            vorlage_Afterparty(AMOUNT,cords)


    






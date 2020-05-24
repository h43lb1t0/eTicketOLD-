from source.ticket import main
from source.links import URL_BALL, URL_Party
from source.qrCoder import qrCode
from source.pdf import pdf

#####################################################################################################
def eventt():
    event = input('Are the tickets for the ball (b) or the afterparty (a)? Enter the according letter: ')
    if event == 'a':
        return event
    if event == 'b':
        return event
    else:
        print('Please enter only the relevant letter.')
        eventt()
        
event = eventt()
AMOUNT = int(input('Number of tickets to be ordered: '))
print("")
ENTRY_URL = input('Event URL: ')
print("")
EVENTNR = input('Event No.: ')
print("")
EMAIL = input('email address: ')
print("")
print("")
#main(ENTRY_URL,EVENTNR,AMOUNT,EMAIL)
print("")
print('The wiki instructions should now be followed')
try:
    input("Press enter to continue")
except SyntaxError:
    pass
#####################################################################################################
def PartyQR(URL_Party):
    URL = URL_Party
    evt = 'source/qr/qr_party/Party_'
    qrCode(URL,evt)
#####################################################################################################
def BallQR(URL_BALL):
    URL = URL_BALL
    evt = 'source/qr/qr_ball/ball_'
    qrCode(URL,evt) 
#####################################################################################################
if event == 'a':
    if AMOUNT == len(URL_Party):
        print('List complete')
        PartyQR(URL_Party)
    else:
        print('The number of links does not match the amount ordered.')
        try:
            input("When the list is corrected press Enter")
        except SyntaxError:
            pass
        PartyQR(URL_Party)
#####################################################################################################
if event == 'b':
    if AMOUNT == len(URL_BALL):
        print('List complete')
        BallQR(URL_BALL)
    else:
        print('The number of links does not match the amount ordered.')
        try:
            input("When the list is corrected press Enter")
        except SyntaxError:
            pass
        BallQR(URL_BALL)
#####################################################################################################
print('')

def vorlage_Afterparty(AMOUNT,cords):
    cords = cords
    input_file = 'source/vorlagen/Afterparty_ticket.pdf'
    output_dic = 'source/Tickets/afterparty_tickets/Afterparty_'
    qr_dic = 'source/qr/qr_party/Party_qr_'
    pdf(AMOUNT,cords,input_file,output_dic,qr_dic)

def vorlage_Ball(AMOUNT,cords):
    cords = cords
    input_file = 'source/vorlagen/Abiball_ticket.pdf'
    output_dic = 'source/Tickets/ball_tickets/Ball_'
    qr_dic = 'source/qr/qr_ball/ball_qr_'
    pdf(AMOUNT,cords,input_file,output_dic,qr_dic)

pdf_method = int(input('use fix cords (1) or use your own cords (2): '))

if pdf_method == 1:
    if event == 'b':
        cords = 900,20,550,120
        vorlage_Ball(AMOUNT,cords)

    if event == 'a':
        cords = 450,20,550,120
        vorlage_Afterparty(AMOUNT,cords)

elif pdf_method == 2:
        h
    






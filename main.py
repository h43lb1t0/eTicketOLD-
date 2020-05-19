from ticket import main
from links import URL_BALL, URL_Party
from qrCoder import qrCode
from pdf import pdf

#####################################################################################################

def eventt():
    event = input('Die Tickets sind für den Ball (b) oder die Afterparty (a)? Den entsprechenden Buchstaben eingaben: ')
    if event == 'a':
        return event
    if event == 'b':
        return event
    else:
        print('Bitte nur den Buchstaben eingeben.')
        eventt()
        
event = eventt()
AMOUNT = int(input('Anzahl der Tickets: '))
print("")
ENTRY_URL = input('Event URL: ')
print("")
EVENTNR = input('Event Nr.: ')
print("")
EMAIL = input('Email adresse: ')
print("")
print("")
main(ENTRY_URL,EVENTNR,AMOUNT,EMAIL)
print("")
print('Den Anweisungen aus dem Wiki nun folgen')
try:
    input("Press enter to continue")
except SyntaxError:
    pass
#####################################################################################################
def PartyQR(URL_Party):
    URL = URL_Party
    evt = 'qr/qr_party/Party_'
    qrCode(URL,evt)
#####################################################################################################
def BallQR(URL_BALL):
    URL = URL_BALL
    evt = 'qr/qr_ball/ball_'
    qrCode(URL,evt) 
#####################################################################################################
if event == 'a':
    if AMOUNT == len(URL_Party):
        print('Liste vollständig')
        PartyQR(URL_Party)
    else:
        print('Die Anzahl der Links stimmt nicht mit dern bestellten Menge überein.')
        try:
            input("Wenn die Liste korigiert ist drücke Enter")
        except SyntaxError:
            pass
        PartyQR(URL_Party)
#####################################################################################################
if event == 'b':
    if AMOUNT == len(URL_BALL):
        print('Liste vollständig')
        BallQR(URL_BALL)
    else:
        print('Die Anzahl der Links stimmt nicht mit dern bestellten Menge überein.')
        try:
            input("Wenn die Liste korigiert ist drücke Enter")
        except SyntaxError:
            pass
        BallQR(URL_BALL)
#####################################################################################################
print('')

def vorlage_Afterparty(AMOUNT,cords):
    cords = cords
    input_file = 'vorlagen/Afterparty_ticket.pdf'
    output_dic = 'Tickets/afterparty_tickets/Afterparty_'
    qr_dic = 'qr/qr_party/Party_qr_'
    pdf(AMOUNT,cords,input_file,output_dic,qr_dic)

def vorlage_Ball(AMOUNT,cords):
    cords = cords
    input_file = 'vorlagen/Abiball_ticket.pdf'
    output_dic = 'Tickets/ball_tickets/Ball_'
    qr_dic = 'qr/qr_ball/ball_qr_'
    pdf(AMOUNT,cords,input_file,output_dic,qr_dic)
    
if event == 'b':
    cords = 450,20,550,120
    vorlage_Ball(AMOUNT,cords)
if event == 'a':
    cords = 450,20,550,120
    vorlage_Afterparty(AMOUNT,cords)





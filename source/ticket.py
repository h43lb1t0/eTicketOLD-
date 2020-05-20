#Script by Andreas Schröder and Tom haelbich to automate booking of tickets over the
# eveeno.com ticket provider.

import requests
import json
import time
import random

ORDER_URL='https://eveeno.com/public/bookingAX.php'


def order_ticket(ENTRY_URL,EVENTNR,EMAIL):
    # Create a new session, like the browser does when visiting a website.
    session = requests.Session()

    # We do not care about the response, but by this request we get the
    # PHPSESSID cookie into the session (internal storage, like the browser
    # does)
    print('Request entry page')
    response = session.get(ENTRY_URL)
    print('Got response with code', response.status_code)

    # take the same data as posted by the browser.
    data = {
        'email': EMAIL,
        'lang': 'de',
        'format': '',
        'eventnr': EVENTNR,
        'orderid': '',
        'tktlist': '{"0":0}',
        'tkt_status': 'booking',
        'order_price': '0',
        'guestlist': '',
        'message': '',
        'promo_code': '',
        'promo_unit': '',
        'promo_value': '0',
        'task': 'step1',
        'test_code':'',
    }

    # Send some headers with the post request. Did not check if they are really
    # required.
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://eveeno.com',
        'Referer': ENTRY_URL,
    }

    print('Posting ticket request.')
    response = session.post(
        ORDER_URL,
        data=data,
        headers=headers)
    print('Got response with code', response.status_code)

    # write response to debug.txt, just for debugging
    with open('debug.txt', 'w') as fhdl:
        fhdl.write(response.text)

    # the response is in json format, we can decode and check for the status.
    response_data = json.loads(response.text)

    print("Your order id is {orderid} with status '{status}'.".format(**response_data))

    return response_data['status'] == 'confirmed'


def main(ENTRY_URL,EVENTNR,AMOUNT,EMAIL):
    for x in range(AMOUNT):
        success = order_ticket(ENTRY_URL,EVENTNR,EMAIL)
        if success:
            print('Ticket ordered successfully.')
            print('                                                                                                                  ')

        else:
            print('Failed to order ticket :-(.')
        ran = random.randrange(5,10)
        print('delay:', ran)
        time.sleep(ran)


if __name__ == '__main__':
    main(AMOUNT)

import fitz


def pdf(AMOUNT,cords,input_file,output_dic,qr_dic):
    
    image_rectangle = fitz.Rect(cords)
    i = 0
    for x in range(AMOUNT):
        file_handle = fitz.open(input_file)
        first_page = file_handle[0]
        i = i+1
        output_file = output_dic + str(i) + ".pdf"
        barcode_file = qr_dic + str(i) + ".png"
        first_page.insertImage(image_rectangle, barcode_file)
        file_handle.save(output_file)
        print('Ticket Nr.' + str(i))
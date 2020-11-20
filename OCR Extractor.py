import tkinter
import requests
import PIL
import urllib
from PIL import Image, ImageTk
from tkinter import filedialog
from io import BytesIO

root = tkinter.Tk()

root.title('OCR Extractor')
root.geometry('600x270')
root.resizable(0, 0)
root.iconbitmap('icon.ico')
root.config(bg='#A0A6DE')


def getfile():
    #file = filedialog.askopenfile(initialdir='/', mode='rb')
    #content = file.read()
    #data = base64.b64encode(content)
    # print(data)

    global response

    URL = label.get()
    URL = URL + '.png'
    print(URL)
    api = 'a07656b96688957'
    # https://gyazo.com/159c01251162f026b434d57fc1cccb6a
    string = {'apikey': api, 'url': URL,
              'language': 'eng', 'isOverlayRequired': False}

    response = requests.post(
        'https://api.ocr.space/parse/image',  data=string)
    print(response)

    response = response.json()
    'print(response)''
    '''{"ParsedResults":[{"TextOverlay":{"Lines":[],"HasOverlay":false,"Message":"Text overlay is not provided as it is not requested"},
    "TextOrientation":"0","FileParseExitCode":1,"ParsedText":"the message","ErrorMessage":"","ErrorDetails":""}],
    "OCRExitCode":1,"IsErroredOnProcessing":false,"ProcessingTimeInMilliseconds":"406","SearchablePDFURL":"Searchable PDF not generated as it was not requested."}'''

    dat = str(response['ParsedResults'][0]['ParsedText'])
    sub = ['\r', '\n', '\r\n', '\n\r']
    for s in sub:
        dat = dat.replace(s, " ")

    te.insert('1.0', dat)


but1 = tkinter.Button(root, text='Get Text', command=getfile, width=20)
but1.grid(row=0, column=0, padx=5, pady=5, sticky='w')
LAB = tkinter.Label(root, text='Enter image URL :', bg='#A0A6DE')
LAB.grid(row=0, column=0, padx=170, pady=5, sticky='w')
label = tkinter.Entry(root, width=53,)
label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
te = tkinter.Text(root, height=13, width=73)
te.grid(row=1, column=0, columnspan=1, padx=5, pady=10, sticky='n')
#pic = tkinter.Label(root, text='texting', height=20, width=20)
#pic.grid(row=1, column=0, padx=5, pady=5)


# run the windowns main loop
root.mainloop()

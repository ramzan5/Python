import pyttsx3
import PyPDF2
book = open('purpose.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
page = pdfReader.getPage(0)
text = page.extractText()
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()


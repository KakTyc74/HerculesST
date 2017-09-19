from PyPDF2 import PdfFileReader

f = open('ST.pdf', 'rb')
reader = PdfFileReader(f)
contents = reader.getPage(0).extractText()
#.split('\n')

for string in contents:
    string.split()

print (contents)
#f.close()

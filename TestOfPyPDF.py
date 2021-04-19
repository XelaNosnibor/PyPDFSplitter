'''
PSEUDOCODE
    Navigate to location of PDF
    Select PDF
    for pages in pdf page:
        Split PDF per page
        save with incremented number
'''

from PyPDF2 import PdfFileWriter, PdfFileReader

#import pdf
inputpdf = PdfFileReader(open("/home/xelar/Documents/MumPhotos/BROTHER/HOME_001293.pdf" , "rb"))

num_pages = inputpdf.numPages

#loop through all pages
for i in range(num_pages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))

with open(f"document-page{i+1}.pdf", 'wb') as outputStream:
    output.write(outputStream)

#Print confirmation of successful
print("Your PDF has been split")
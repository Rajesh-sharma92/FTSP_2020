# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:09:04 2020

@author: Rajesh
"""


"""
Extract text from PDF In python for NLP
"""


# step 1 - !pip install PyPDF2


# Now import the PyPDF2
import PyPDF2 as pdf


# file
file = open(r'E:\Projects\Extract Text From PDF File\NLP.pdf','rb')   # open our pdf for extracting the data




# pdf_reader
pdf_reader = pdf.PdfFileReader(file)
# image = open('cafe.PNG','rb')



pdf_reader.getIsEncrypted()  # False

pdf_reader.getNumPages()  # It will return number of pages in pdf # 3


page1 = pdf_reader.getPage(0)
page1.extractText()


page2 = pdf_reader.getPage(1)
page2.extractText()


# Append Write or Merge PDf

pdf_writer = pdf.PdfFileWriter()


pdf_writer.addPage(page1)
pdf_writer.addPage(page2)


output = open('E:\Projects\Extract Text From PDF File\Pages.pdf','wb')    

pdf_writer.write(output)

output.close()




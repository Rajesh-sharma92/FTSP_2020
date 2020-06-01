# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:39:51 2020

@author: Rajesh
"""


"""
Extract text from PDF In python for NLP
"""


# step 1 - !pip install PyPDF2

# Now import the PyPDF2

import PyPDF2 as pdf

file = open('D:\PF.pdf','rb')



pdf_reader = pdf.PdfFileReader(file)

pdf_reader.getIsEncrypted() # False

pdf_reader.getNumPages() # 1 # It will return number of pages in pdf # 3

page1 = pdf_reader.getPage(0) 

page1.extractText()




# Append Write or Merge PDf
pdf_writer = pdf.PdfFileWriter()

pdf_writer.addPage(page1)

output = open('D:\PF_New.pdf','wb')

pdf_writer.write(output)

output.close()





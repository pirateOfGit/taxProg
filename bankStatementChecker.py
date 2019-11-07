#! /usr/bin/python3

# PURPOSE: Application used to check that the total obtained from 
# 	   the incoives program is correct by checking how much was 
#	   paid into the bank account from Deliveroo/Uber etc

# USAGE: 

import os, PyPDF2, re

# Get a list of all files in directory

path = "/home/snake_charmer/scripts/bankStatements/"

pdfName = os.listdir(path)

counter = 0

for pdf in pdfName:
	print(pdf)
	# Open PDF nad extract contents
	pdfObj = open(path + pdf, 'rb') # Need to change for the for loop
	pdfReader = PyPDF2.PdfFileReader(pdfObj)
	pageObj = pdfReader.getPage(0)
	pdfText = pageObj.extractText()
	numberOfPages = pdfReader.numPages
	#print(pdfText)

	# Create regex for fee payments
	rooPaymentRegex = re.compile(r'[0-9]{2}[a-zA-Z]{3}BankcreditRoofoodsLimited[0-9]+\.[0-9]+')
	refinedRooPaymentRegex = re.compile(r'[0-9]+\.[0-9]+')
	dateRegex = re.compile(r'[0-9]{2}[a-zA-Z]{3}')

	# Search the pdf text for regex
	mo = rooPaymentRegex.findall(pdfText)
	#print(mo)

	# Extract only the numbers
	refinedRooResult = refinedRooPaymentRegex.findall(str(mo))

	# Extract the date
	dateRegexResult = dateRegex.findall(str(mo))

print('\n\n*****\n\n' + str(mo))
print('\n' + str(dateRegexResult) + ': ' + str(refinedRooResult) + '\n')
print('There are ' + str(numberOfPages) + ' pages in this document')

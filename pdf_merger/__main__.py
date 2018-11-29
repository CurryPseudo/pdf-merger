import argparse
import pdfrw
import os
parser = argparse.ArgumentParser(description="Merge some pdfs")
parser.add_argument('input_pdf_dir')
parser.add_argument('output_pdf_path', default='output.pdf')
args = parser.parse_args()
fileList = []
for file in os.listdir(args.pdf_dir):
    if ".pdf" in file:
        fileList.append(file)
defaultOrder = []
for i in range(0, len(fileList)):
    defaultOrder.append(str(i))
    print("{0}: {1}".format(i, fileList[i]))

print("\nInput the right order[default:{0}]:".format(''.join(defaultOrder)))
inputOrder = input()
if inputOrder != "":
    defaultOrder.clear()
    for c in inputOrder:
        defaultOrder.append(c)
orderList = []
for c in defaultOrder:
    orderList.append(int(c))

outPdf = pdfrw.PdfWriter()
for o in orderList:
    outPdf.addpages(pdfrw.PdfReader(args.pdf_dir + '/' + fileList[o]).pages)

outPdf.write(args.output_pdf_path)

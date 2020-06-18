import PyPDF2 as pdf
import get_file_content as ok
import os
FILE_PATH = 'N:\\PythonBiggerProjects\\PdfCombiner\\FilesToConvert\\'
output_pdf = pdf.PdfFileWriter()

def get_pdf_reader(oppened_file):
    op = open(FILE_PATH+oppened_file,'rb')
    return pdf.PdfFileReader(op,strict=False)


file_list = os.listdir(path=FILE_PATH)
file_streams = {file:get_pdf_reader(file) for file in file_list}

for name,stream in file_streams.items():
    ok.get_file_content(output_pdf,stream)
with open(FILE_PATH+"result.pdf",'wb') as result:
    output_pdf.write(result)

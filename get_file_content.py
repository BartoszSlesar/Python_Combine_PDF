def get_file_content(output,input):
    r = input.getNumPages()
    for page in range(r):
        output.addPage(input.getPage(page))

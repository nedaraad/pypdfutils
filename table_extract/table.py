import tabula


finp = input("Enter your pdf file name: ")
fout = input("Enter your output file name: ")

# extract table from pdf file to csv file
tabula.convert_into(finp, fout, pages="1")

import tabula


file = "input.pdf"
# extract table from pdf file to csv file
tabula.convert_into(file, "output.csv", pages="all")

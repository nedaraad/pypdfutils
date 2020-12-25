import tabula

file = "7-series-product-selection-guide.pdf"
table = tabula.read_pdf(file, pages = 1)
print(table[0])


#tabula.convert_into("7-series-product-selection-guide.pdf", "tablecal.ods", all = True)
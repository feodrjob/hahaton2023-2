import xlsxwriter
from main import array
def writer(parametr):
    book = xlsxwriter.Workbook(r"C:\Users\Фёдор\OneDrive\Рабочий стол\names.xlsx")
    page = book.add_worksheet("товар")

    row = 0
    colum = 0
    page.set_column("A:A", 20)
    page.set_column("B:B", 20)



    for item in parametr():
        page.write(row,colum, item[0])
        page.write(row, colum+1, item[1])

        row+=1

    book.close()
writer(array)


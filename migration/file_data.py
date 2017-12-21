import xlrd

excel_sheet = xlrd.open_workbook('./data/file_data.xlsx').sheet_by_index(0)

file_data = dict()

for row_index in range(1,excel_sheet.nrows):
    link, save_loc, file_name = excel_sheet.row_values(row_index)
    save_loc = save_loc.split("\\")[-2]
    try:
        file_data[save_loc]
    except:
        file_data[save_loc] = []
    file_data[save_loc].append({'link':link,'file_name':file_name})
import xlrd

FILE_WORKSHEET = './data/g_drive_files4.xlsx'

excel_sheet = xlrd.open_workbook(FILE_WORKSHEET).sheet_by_index(0)

file_data = dict()

for row_index in range(1,excel_sheet.nrows):
    link, save_loc, file_name = excel_sheet.row_values(row_index)
    save_loc = save_loc.split("\\")[-2]
    if('/' in save_loc):
        save_loc.replace("/","-")
    try:
        file_data[save_loc]
    except:
        file_data[save_loc] = []
    file_data[save_loc].append({'link':link,'file_name':file_name})
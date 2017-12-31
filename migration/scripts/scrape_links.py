import scrapy
from xlsxwriter import Workbook
from scrapy.http import HtmlResponse
from pprint import pprint

workbook = Workbook('data/g_drive_files.xlsx')
worksheet = workbook.add_worksheet()
HEADERS = (
    "LINK",
    "SAVE AS PATH",
    "SAVE AS FILENAME"
)

CA_ROOT_URL = "https://sanjac.compliance-assist.com/accreditation/"
G_ROOT_URI = "G:\\SACSCOC 2019 Regression\\"

for i,header in enumerate(HEADERS):
    worksheet.write(0,i,header)

row = 0

f = open('data/doc_directory.htm','rb')
response = HtmlResponse(url='http://example.com/index', body=f.read())

folders = response.xpath('//li[descendant::img[contains(@src,"folder")]]')

for folder in folders:
    folder_name = folder.xpath('./div/span[contains(@class,"rtIn")]/text()').extract()[0]
    folder_name = G_ROOT_URI + folder_name + '\\'
    documents = folder.xpath('.//a[contains(@class,"rtIn")]')
    for document in documents:
        row += 1
        doc_link = CA_ROOT_URL + document.xpath('./@href').extract()[0]
        doc_name = document.xpath('./text()').extract()[0]
        if('.pdf' not in doc_name):
            doc_name += '.pdf'
        worksheet.write(row,0,doc_link)
        worksheet.write(row,1,folder_name)
        worksheet.write(row,2,doc_name)
        
f.close()
workbook.close()



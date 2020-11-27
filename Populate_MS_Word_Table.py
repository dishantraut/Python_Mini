from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

template = "Ms_Word_Table_Populate_Demo.docx"

document = MailMerge(template)
print(document.get_merge_fields())


sales_history = [{
    'prod_desc': 'Red Shoes',
    'price': '$10.00',
    'quantity': '2500',
    'total_purch': '$25,000.00'
}, {
    'prod_desc': 'Green Shirt',
    'price': '$20.00',
    'quantity': '10000',
    'total_purch': '$200,000.00'
}, {
    'prod_desc': 'Purple belt',
    'price': '$5.00',
    'quantity': '5000',
    'total_purch': '$25,000.00'
}]

document.merge_rows('prod_desc', sales_history)
document.write('test-output-table.docx')
print('DONE')

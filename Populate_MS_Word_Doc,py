# https://pbpython.com/python-word-template.html

# conda install -U lxml 
# pip install -U docx-mailmerge

from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

template = "demo.docx"

document = MailMerge(template)
print(document.get_merge_fields())

document.merge(date = '10/01/1997',
                to_name = 'Dishant R. Raut',
                sub = 'Submission of Annual Returns in Form XXV under Gujarat Contract Labour (Regulation and Abolition Rules)',
                comp_name = 'Onion King',
                comp_add = 'Unit No. 1-7 on Gr. & First Floor, Shreeji One, Near. Gurudwara, Indira Gandhi Road, Jamnagar, Gujarat - 361001',
                Add_l1 = 'Diamond Market, 2nd floor,',
                Add_l2 = 'near Amber Cinema,',
                loc = 'Jamnagar',
                pincode = '361001')
document.write(f'MM_{comp_name}.docx')

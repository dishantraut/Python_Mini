# https://www.geeksforgeeks.org/working-zip-files-python/?ref=rp

from zipfile import ZipFile 
  
# specifying the zip file name 
file_name = r"C:\Users\kmc445\Desktop\KARMA MANAGEMENT-20201030T142011Z-001.zip"
  
# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip: 
    # printing all the contents of the zip file 
    zip.printdir() 
  
    # extracting all the files 
    print('Extracting all the files now...') 
    zip.extractall() 
    print('Done!') 

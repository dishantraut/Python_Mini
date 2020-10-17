# Generate QRCode for any URL
import pyqrcode
import png
from pyqrcode import QRCode

qrs = "https://www.linkedin.com/in/dishant-raut-595972178/"
url =  pyqrcode.create(qrs)
url.png("yoo.png",scale = 8) 

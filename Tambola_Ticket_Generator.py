""" MODULES REQUIRED """
from email.mime.multipart import MIMEMultipart 
from jinja2 import Environment, BaseLoader
from email.mime.image import MIMEImage
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from IPython.core.display import HTML
from IPython.display import display
from pandas.plotting import table
import matplotlib.pyplot as plt
import dataframe_image as dfi
from tabulate import tabulate
from email import encoders 
import pandas as pd
import numpy as np
import smtplib 
import random
import glob
import sys
import os



def GT():
    """ GENEREATE TICKETS MADE BY DDR """
    
    FC = random.sample(range(1,10),3)
    SND = random.sample(range(10,20),3)
    TC = random.sample(range(20,30),3)
    FOC = random.sample(range(30,40),3)
    FIC = random.sample(range(40,50),3)
    SC = random.sample(range(50,60),3)
    SEC = random.sample(range(60,70),3)
    EC = random.sample(range(70,80),3)
    NC = random.sample(range(80,91),3)
    
    FC.sort()
    SND.sort()
    TC.sort()
    FOC.sort()
    FIC.sort()
    SC.sort()
    SEC.sort()
    EC.sort()
    NC.sort()

    # print(FC,SC,TC,FOC,FIC,SC,SEC,EC,NC)
    data = pd.DataFrame({'one':FC,'two':SND,'third':TC,'four':FOC,'five':FIC,'six':SC,'seven':SEC,'eight':EC,'nine':NC})

    ba = random.sample(range(0,9),4)
    for o in ba:
        data.loc[0][o] = 0 


    ab = random.sample(range(0,9),4)
    for n in ab:
        data.loc[1][n] = 0 

    xy = random.sample(range(0,9),4)
    for m in xy:
        data.loc[2][m] = 0 

    for i in data.columns.values:
        data[i].replace(0, 'X',inplace=True)


    UD = data
    df_dict = dict.fromkeys(UD.columns, '')                   
    YOO = UD.rename(columns = df_dict)                        # Rename Columns Index Blank
    UD.index = [' ', ' ', ' ']                                # Rename Rows Index Blank
    df_dict = dict.fromkeys(UD.columns, '')                   
    FD = UD.rename(columns = df_dict)
    return FD

GT()
F='Dishant'
L='Raut'
dfi.export(GT(),str(F)+'_'+str(L)+".png",fontsize=50)

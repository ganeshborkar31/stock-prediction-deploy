from datetime import datetime
import pandas as pd
import numpy as np
from keras.models import load_model
import matplotlib.pyplot as plt

import streamlit as st  #streamlit-1.33.0
from streamlit_option_menu import option_menu

from pandas_datareader import data as pdr
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

###  pakages 
from packeges import tech
from packeges import about
from packeges import fundament
from packeges import account
from packeges import home
from packeges import disclaimer


st.set_page_config(
    page_title="Stock Price Predictor",
    page_icon="📈 ",
)

# nse=pd.read_csv('/home/ganesh/Projects/BE_Project/NSE.csv')
# symbols=np.array(nse["Symbol"])

# symbol = st.sidebar.selectbox('Select dataset for prediction', symbols)

# st.title("Predictive Analysys for "+ symbol)
# symbol = symbol+'.NS'



#stock = st.text_input("Enter the Stock ID", "TCS.NS") 

### -- Authentication library --

from pathlib import Path
import streamlit_authenticator as stauth
import pickle

    
# @st.cache
def run():
    # app = st.sidebar(
    with st.sidebar:        
        app = option_menu(
            menu_title='Menu ',
            options=['Home','about','Disclaimer'], #removed Account from optioins( icon ->'person-circle')
            icons=['house-fill','info-circle-fill',	'warning','⚠️'],
            menu_icon='chat-text-fill',
            default_index=1,
            
    #         styles={
    #             "container": {"padding": "5!important","background-color":'black'},
    # "icon": {"color": "white", "font-size": "23px"}, 
    # "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
    # "nav-link-selected": {"background-color": "#02ab21"},}
            
            )
        
        
    if app == "Home":
        try:
            home.home_def()
        except Exception as e:
            st.write(e) 
            
    if app == "about":
        try:
            about.aboutus() 
        except Exception as e:
            st.write(e)
        
        
    # if app == 'Account':
    #     account.acc()
        
    if app == 'Disclaimer':
        disclaimer.display_disclaimer()
    
    
    
run() 

































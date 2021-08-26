import numpy as np
import pickle
import pandas as pd
import streamlit as st
import sklearn   
import math

from PIL import Image

pickle_in=open("bank_class.pkl","rb")
log_reg =pickle.load(pickle_in)

def predict_default(Interest_Rate_orig_time,interest_rate_time,balance_time,gdp_time,LTV_time):
    prediction=log_reg.predict([[Interest_Rate_orig_time,interest_rate_time,balance_time,gdp_time,LTV_time]])
    print(prediction)
    return prediction

def main():
    st.title("BANK LOAN APPROVAL IDENTIFICATION APP")
    html_temp="""
     <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align: center;"> This WEB APP is created to help banks
    whether the customer payoff or default </h2>
    </div>
    """
  
    st.markdown(html_temp,unsafe_allow_html=True)

    Interest_Rate_orig_time=st.number_input("Interest_Rate_orig_time",format="%.2f")
    
    if (Interest_Rate_orig_time<2.0):
       Interest_Rate_orig_time=0.323361
    elif float(Interest_Rate_orig_time>=2.0 and Interest_Rate_orig_time<5.0):
         Interest_Rate_orig_time=-0.804885
    elif float(Interest_Rate_orig_time>=5.0 and Interest_Rate_orig_time<6.0):
         Interest_Rate_orig_time=-0.325760
    elif float(Interest_Rate_orig_time>=6.0 and Interest_Rate_orig_time<7.0):
         Interest_Rate_orig_time=-0.013290
    else: Interest_Rate_orig_time=0.232141
    
    interest_rate_time=st.number_input("interest_rate_time",format="%.2f")
    
    if float(interest_rate_time<3.0):
       interest_rate_time=-1.660522
    elif float(interest_rate_time>=3.0 and interest_rate_time<7.0):
         interest_rate_time=0.1975500
    else:interest_rate_time=0.51900
    
    balance_time=st.number_input("balance_time",format="%.2f")
    
    if float(balance_time<60000.0):
       balance_time=-0.933103
    elif float(balance_time>=60000.0 and balance_time<120000.0):
          balance_time=-0.290920
    elif float(balance_time>=120000.0 and balance_time<180000.0):
         balance_time=0.118070
    else: balance_time=0.283062
    
    gdp_time=st.number_input("gdp_time",format="%.2f")
    
    if float(gdp_time<0.0):
       gdp_time=4.684266
    elif float(gdp_time>=0.0 and gdp_time<2.0):
         gdp_time=3.679645
    else: gdp_time=-1.016383
    
    LTV_time=st.number_input("LTV_time",format="%.2f")
    
    if float(LTV_time<85.0):
       LTV_time=-1.388241
    elif float(LTV_time>=85.0 and LTV_time<100.0):
         LTV_time=-0.253946
    elif float(LTV_time>=100.0 and LTV_time<110.0):
        LTV_time=1.465731
    else: LTV_time=3.309052
    
    result=""
    if st.button("Predict default"):
        result=predict_default(float(Interest_Rate_orig_time),float(interest_rate_time),float(balance_time),float(gdp_time),float(LTV_time))
    st.success("The CUSTOMER will default if score is 1 and will not default if score is 0. The score of current customer =      {}".format(result))
                     
if __name__=='__main__':
        main()
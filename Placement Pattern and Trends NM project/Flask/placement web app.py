# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:58:38 2023

@author: Anuiskha RE
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/Anuiskha RE/Downloads/placement project/trained_model.sav', 'rb'))


# creating a function for prediction

def placement_prediction(input_data):
    
 #Prediction on new data
 

 # changing the input_data to numpy array
 input_data_as_numpy_array = np.asarray(input_data)

 input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

 prediction = loaded_model.predict(input_data_reshaped)
 print(prediction)

 if(prediction[0] == 0):
     return'Placed'
 else:
     return'Not Placed'
 
    
 
def main():
        
      # giving a title
      st.title('Placement Patterns and Trends Web App')
      
      
      # getting the input data from the user
     
      
      Gender = st.text_input('Numbeer of Gender')
      SSC = st.text_input(' secondary ssc_p')
      Ssc = st.text_input(' secondary of ssc_b')
      HSC = st.text_input('higher study of hsc_p')
      Hsc = st.text_input(' higher study of hsc_b')
      DEGREE = st.text_input(' course of degree_p')
      Degree = st.text_input(' course of degree_b')
      Work = st.text_input('Number of work')
      Test = st.text_input('Numbeer of etest')
      Specialisation = st.text_input('Numbeer of specialisation')
      MBA = st.text_input('Numbeer of mba_p')
      
      # code for prediction 
      Placement = ' '
      
      # creating a button for prediction
      
      if st.button('Placement Result'):
          Placement = PREDICTION([Gender, SSC, Ssc, HSC, Hsc, DEGREE, Degree, Work, Test, Specialisation, MBA])
          
      st.success(Placed)
      
      
      
      if__name__ == '__main__'
      main()
      
     
      
      
      
      
      
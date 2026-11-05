

import numpy as np
import pickle
import streamlit as st


 #loading the saved model
loaded_model = pickle.load(open('C:/Users/ASHWINI - AISHWARYA/Desktop/ML-projects/trained_model.sav','rb'))


 #creating a function for prediction
 
def diabeties_prediction(input_data):
     
     
     #changing the input_data to numpy array
     input_data_as_numpy_array = np.asarray(input_data)
     
     #reshape the array as we are predicting for one instance
     input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
     
     prediction = loaded_model.predict(input_data_reshaped)
     print(prediction)
     
     if(prediction[0] == 0):
         return 'the person is not diabetic'
     else:
         return 'the person is diabetic'
    
    
    
def main():
        
        
        #giving a title
        st.title('Diabetes prediction Web app')
        
        
        #getting the input data from the user
        
        
        Pregnancies=st.text_input('Number of pregnancies ')
        Glucose=st.text_input('Glucose level')
        BloodPressure=st.text_input('Blood pressure value')
        SkinThickness=st.text_input('Skin thockness')
        Insulin=st.text_input('Insulin level')
        BMI=st.text_input('BMI value')
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
        Age=st.text_input('Age of the person')
         
        
        #code for prediction
        diagnosis=''
        
        #creating a button for prediction
        
        if st.button('Diabetes Test Result'):
            diagnosis = diabeties_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
            
            
        st.success(diagnosis)
            
            
            
            
            
if __name__ == '__main__':
        main()
     
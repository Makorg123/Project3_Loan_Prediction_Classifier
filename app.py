import streamlit as st
from PIL import Image
import pickle

# Loading the trained model

model = pickle.load(open('regmodel.pkl', 'rb'))

st.header(':blue[Bank Loan] Prediction Using Machine Learning')
st.write('Please enter the required details and click on the predict button to check if you are eligible for a loan or not')
st.divider()
col1, col2, col3, col4 = st.columns(4)
with col1:
   # for gender
   gen_display = ('Female','Male')
   gen_options = list(range(len(gen_display)))
   gen = st.selectbox("Gender",gen_options,format_func=lambda x: gen_display[x])

   # for marital status
   mar_display = ('Married','Single')
   mar_options = list(range(len(mar_display)))
   mar = st.selectbox("Marital Status",mar_options,format_func=lambda x: mar_display[x])

   # No of dependents
   dep_display = ('No','One','Two','More than Two')
   dep_options = list(range(len(dep_display)))
   dep = st.selectbox("No of Dependents",dep_options,format_func=lambda x: dep_display[x])

with col2:
   # for education
   edu_display = ('Graduate','Not Graduate')
   edu_options = list(range(len(edu_display)))
   edu = st.selectbox("Education",edu_options,format_func=lambda x: edu_display[x])

   # for emp status
   emp_display = ('Job','Business')
   emp_options = list(range(len(emp_display)))
   emp = st.selectbox('Employment Status',emp_options,format_func=lambda x: emp_display[x])

   # For Property Status
   prop_display = ('Rural','Semi-Urban','Urban')
   prop_options = list(range(len(prop_display)))
   prop = st.selectbox('Property Area',prop_options,format_func=lambda x: prop_display[x])

with col3:
   # for credit Score
   cred_display = ('Between 300 to 500','Above 500')
   cred_options = list(range(len(cred_display)))
   cred = st.selectbox('Credit Score',cred_options,format_func=lambda x: cred_display[x])

   # Applicant Monthly Income
   mon_income = st.number_input("Applicant's Monthly Income($)",value=0)

   # Co-Applicant Monthly Income
   co_mon_income = st.number_input("Co-Applicant's Monthly Income($)",value=0)

with col4:
   # Loan Amount
   loan_amt = st.number_input("Loan Amount($)",value=0)

   # loarn duration
   dur_display = ['2 Month', '6 Month', '8 Month', '1 Year', '16 Month']
   dur_options = range(len(dur_display))
   dur = st.selectbox('Loan Duration',dur_options,format_func=lambda x: dur_display[x])

if st.button('Predict'):
   duration = 0
   if dur == 0:
      duration = 60
   if dur == 1:
      duration = 180
   if dur == 2:
      duration = 240
   if dur == 3:
      duration = 360
   if dur == 4:
      duration = 480
   result = model.predict([[gen,mar,dep,edu,emp,prop,cred,mon_income,co_mon_income,loan_amt,dur]])
   if result == 1:
      st.success('Congratulations! You are eligible for the loan')
   else:
      st.error('Sorry! You are not eligible for the loan')
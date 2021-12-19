import pandas as pd
import streamlit as st
import numpy as np

st.title("Center for Medicare and Medicaid Services (CMS) HOSPITAL DATASETS IN THE UNITED STATES")
st.text ("The datasets are data from hospitals in the United States from CMS for diagnsis, patient experience, total charges and payments.  First I will load the datasets then make a comparison between SUNY/Stony Brook University Hospitals with Bronx Lebanon Hospital, Montefiore Medical Center and St. Barnabas")

df = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv")
df1 = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv")

st.dataframe(df)
st.dataframe(df1)
st.dataframe(df2)



st.subheader ('Outpatient Ambulatory Payment Classification(APC) in Stony Brook University Hospital')
dataframe_pivot = df2.pivot_table(index= ['state','city'], values = ['average_total_payments'], aggfunc = ['mean'])

st.text("Comparison of Diagnosis Related Groups (DRGs) at Stony Brook Hospital and Montefiore Medical Center")
st.text(VISUALIZATION)

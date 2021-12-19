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


st.text("Comparison of Stony Brook Hospital and Bronx Lebanon Hospital, Montefiore Medical Center and St. Barnabas Hospital")
st.code(Results.pivot(index ='provider_name', columns = 'apc', values = 'average_total_payments'))

st.text ("Comparison of Diagnosis Related Groups (DRGs) at Stony Brook Hospital and Montefiore Medical Center")

st.code(OResults.pivot(index = 'hospital_name', columns = 'drg_definition', values = 'average_covered_charges'))

st.text(VISUALIZATION)

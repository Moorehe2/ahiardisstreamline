import pandas as pd
import streamlit as st
import numpy as np

st.title("Center for Medicare and Medicaid Services (CMS) HOSPITAL DATASETS IN THE UNITED STATES")
st.markdown("The datasets are data from CMS for diagnosis, patient experience, discharges, readmission, imaging, procedures, total charges and payments. I will load the datasets and show visualization.")

df = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv")
df1 = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv")
df2 = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv")

st.write(df, 25,25)
st.write(df1, 25,25)
st.write(df2, 25,25)

st.markdown("Display Ambulatory Payment Classification")

apc_data = df2["apc"].value_counts()

st.bar_chart(apc_data)

st.markdown("Display Diagnosis Related Groups")

drgs_data = df1["drg_definition"].value_counts()


st.bar_chart(drgs_data)
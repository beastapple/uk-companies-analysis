import streamlit as st
import pandas as pd

st.markdown(""" # Companies Data Dashboard  
There's nothing here yet! This application will allow for filtering and analysis of company information exported from the [Companies House Advanced Search function](https://find-and-update.company-information.service.gov.uk/advanced-search).         
""")

st.divider()
# @st.cache_data

# Step 1: Import the CSV spreadsheet data.

# Creates a column list to validate the CSV upload against.
companies_house_headers = pd.DataFrame(columns=['company_name', 'company_number', 'company_status', 'company_type', 'company_subtype', 'dissolution_date', 'incorporation_date', 'removed_date', 'registered_date', 'nature_of_business', 'registered_office_address'])

# Sidebar upload.
raw_companies_data = st.sidebar.file_uploader("Upload CSV from Companies House to generate a data dashboard.", type=['csv'])

# Validates the CSV upload is the right format/from Companies House.
if raw_companies_data:
    unvalidated_csv = pd.read_csv(raw_companies_data)
#    st.write(unvalidated_csv.columns.values)
    if unvalidated_csv.columns.values.all() == companies_house_headers.columns.values.all():
        raw_companies_data = unvalidated_csv
#        st.write("CSV accepted.")
    else:
        st.write(f"Unexpected columns. Expected {companies_house_headers}")

# For testing.
st.write(f"The dataset is {len(raw_companies_data)} rows long.")
st.write(raw_companies_data.columns.values)
st.write(raw_companies_data.head(5))

# Dashboard
total_companies = len(raw_companies_data['company_number'])
total_active = raw_companies_data['company_status'].value_counts().get('Active', 0)
total_private = raw_companies_data['company_type'].value_counts().get('Private limited company', 0)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Companies:")
    st.subheader(f"{total_companies:,}")
with middle_column:
    st.subheader("Total Active Companies:")
    st.subheader(f"{total_active:,}")
with right_column:
    st.subheader("Total Private Limited Companies")
    st.subheader(f"{total_private:,}")

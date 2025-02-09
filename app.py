import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.markdown(""" # Companies Data Dashboard  
This application will allow for filtering and analysis of company information exported from the [Companies House Advanced Search function](https://find-and-update.company-information.service.gov.uk/advanced-search).         
""")

st.divider()
# @st.cache_data

# Step 1: Import the CSV spreadsheet data, whether one or multiple files, and combine into one document while removing duplicates.

# Sidebar upload.
raw_companies_data = st.sidebar.file_uploader("Upload CSV(s) from Companies House to generate a data dashboard.", type=['csv'], accept_multiple_files=True)
upload_done = st.sidebar.button("Process Files") # Need to style better as looks "inactive"

# Combines all of the uploaded files into one file by deduplicating based on unique company number.

all_files = pd.DataFrame({})

def deduplicate_data(df, dedupe_column):
    if dedupe_column in df.columns.values:
        deduped.sort_values(by=[dedupe_column], ascending=[True])
        deduped.drop_duplicates(subset=dedupe_column, keep='first', inplace=True)
        st.write("List deduplicated by company number.")
    else:
        st.write("Please upload files and click the 'Process files' button when done.")
    return deduped

if upload_done:
#    st.write(f"Processing the following files: {raw_companies_data}") # Need to figure out how to get it to just say the name and not the full shebang of info.
    all_files = pd.concat(pd.read_csv(csv_file) for csv_file in raw_companies_data)

deduped = all_files.copy()
deduped = deduplicate_data(all_files, 'company_number') # Would be cool to add this as a "selector" so the user can choose which column to dedupe on, rather than hard coded.

# For testing
# st.write(deduped.head(5))
# st.write(f"The dataset is {len(deduped)} rows long.")
# st.write(deduped.columns.values)

# Step 2. Validate the CSV upload is the right format/from Companies House.

# Creates a column list to validate the CSV upload against.
companies_house_headers = pd.DataFrame(columns=['company_name', 'company_number', 'company_status', 'company_type', 'company_subtype', 'dissolution_date', 'incorporation_date', 'removed_date', 'registered_date', 'nature_of_business', 'registered_office_address'])

def validate_csv():
    unvalidated_csv = deduped
#    st.write(unvalidated_csv.columns.values)
    if unvalidated_csv.columns.values.all() == companies_house_headers.columns.values.all():
        st.write("CSV validated.")
    else:
        st.write(f"Unexpected columns. Expected {companies_house_headers}")

# Step 3. Wrangles the SIC codes (nature_of_business column) for analysis.

def explode_sic(): # https://www.geeksforgeeks.org/how-to-split-explode-pandas-dataframe-string-entry-to-separate-rows/
    # Explode the SICs column so that companies with multiple SICs are accounted properly.
    sics_exploded = deduped.copy()
    sics_exploded = sics_exploded['nature_of_business'].str.split().explode() # Returns as a series, not a dataframe
    sics_counted = sics_exploded.groupby(sics_exploded).count() # https://stackoverflow.com/questions/33483670/how-to-group-a-series-by-values-in-pandas
    sics_counted = sics_counted.sort_values(ascending=False)
    st.write(sics_counted)
    fig_sics = px.pie(
        sics_exploded.head(30), 
        values='nature_of_business', 
        names='nature_of_business',
        title='Top 30 SIC codes',
        hole=0.3,
        )
    st.plotly_chart(fig_sics)



# Step 3. Generates a dashboard.

def dashboard():
    total_companies = len(deduped['company_number'])
    total_active = deduped['company_status'].value_counts().get('Active', 0)
    total_private = deduped['company_type'].value_counts().get('Private limited company', 0)

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
    return st.write(deduped)

# Main 
if len(deduped) > 1:
    validate_csv()
    dashboard()
    explode_sic()


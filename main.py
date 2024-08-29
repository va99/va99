import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample mock data for facilities
facilities_data = {
    'Facility Name': ['City Hospital', 'Green Clinic', 'Sunrise Health Center', 'Prime Care Hospital'],
    'Location': ['Mumbai', 'Delhi', 'Bangalore', 'Pune'],
    'Insurance': ['Cashless, Reimbursement', 'Cashless, BNPL', 'Reimbursement, BNPL', 'Cashless, Reimbursement, BNPL']
}

# Sample mock data for best sellers
best_sellers_data = {
    'Service/Product': ['Consultation', 'Peace+ Capsule', 'Lab Tests', 'Vaccination'],
    'Sales': [250, 150, 100, 200]
}

# Convert to DataFrame
facilities_df = pd.DataFrame(facilities_data)
best_sellers_df = pd.DataFrame(best_sellers_data)

# Streamlit UI
st.title('MedLeads - Doctor Admin Dashboard')

# Search Facility
st.header('Search Facility')
facility_name = st.text_input('Enter Facility Name:')
location = st.text_input('Enter Location:')
insurance = st.selectbox('Select Insurance Method:', ['', 'Cashless', 'Reimbursement', 'BNPL'])

# Filter Data
filtered_df = facilities_df[
    (facilities_df['Facility Name'].str.contains(facility_name, case=False, na=False)) &
    (facilities_df['Location'].str.contains(location, case=False, na=False)) &
    (facilities_df['Insurance'].str.contains(insurance, case=False, na=False))
]

# Display Facility Results
st.subheader('Facility Results')
st.dataframe(filtered_df)

# Refer Patient
if st.button('Refer'):
    st.success(f'Patient referred to {facility_name}!')

# Data Visualization - Best Seller Trends
st.header('Best Sellers - Trends')
st.bar_chart(best_sellers_df.set_index('Service/Product'))

# Additional Visualization (Pie Chart)
st.subheader('Best Sellers Distribution')
fig, ax = plt.subplots()
ax.pie(best_sellers_df['Sales'], labels=best_sellers_df['Service/Product'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)
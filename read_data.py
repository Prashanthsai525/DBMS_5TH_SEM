import pandas as pd
import streamlit as st
import plotly.express as px
from databas import view_crime_data


def read():
    result = view_crime_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['crime_id','crime_type','crime_place','crime_date','criminal_id','criminal_name','past_crimes','jail_name','fir_id','fir_statement','fir_writer','date_of_fir'])
    with st.expander("View all crimes"):
        st.dataframe(df)
    


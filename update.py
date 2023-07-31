import datetime

import pandas as pd
import streamlit as st
from databas import view_crime,view_only_crime_ids, get_details, edit_details


def update():
    result = view_crime()
    df = pd.DataFrame(result, columns=["crime_id", "crime_type", "crime_place", "crime_date"])
    with st.expander("Current CRIMES"):
        st.dataframe(df)
    list_of_crimes = [i[0] for i in view_only_crime_ids()]
    selected_crime = st.selectbox("crime to Edit", list_of_crimes)
    selected_result = get_details(selected_crime)
    # st.write(selected_result)
    if selected_result:
        crime_id = selected_result[0][0]
        crime_type = selected_result[0][1]
        crime_place = selected_result[0][2]
        crime_date = selected_result[0][3]


        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_crime_id = st.text_input("ID:", crime_id)
            new_crime_type = st.text_input("Type:", crime_type)
        with col2:
            new_crime_place = st.text_input("PLACE:",crime_place)
            new_crime_date=st.date_input("DATE",crime_date)
        

        if st.button("Update crime info"):
            edit_details(new_crime_id, new_crime_type, new_crime_place,new_crime_date,crime_id,crime_type,crime_place,crime_date)
            st.success("Successfully updated")

       
        with st.expander("Updated data"):
            result2 = view_crime()
            df2 = pd.DataFrame(result2, columns=['crime_id', 'crime_type', 'crime_place', 'crime_date',])
            st.dataframe(df2)



import pandas as pd
import streamlit as st
from databas import view_only_crime_ids,delete_data,view_fir


def delete():
    result = view_fir()
    df = pd.DataFrame(result, columns=["crime_id", "fir_id", "fir_statement", "fir_writer","date_of_fir"])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_crimes = [i[0] for i in view_only_crime_ids()]
    selected_crime = st.selectbox("crime to Delete", list_of_crimes)
    st.warning("Do you want to delete ::{}".format(selected_crime))
    if st.button("Delete crime"):
        delete_data(selected_crime)
        st.success("crime has been deleted successfully")
    
    with st.expander("Updated data"):
        new_result = view_fir()
        df2 = pd.DataFrame(new_result, columns=["crime_id", "fir_id", "fir_statement", "fir_writer","date_of_fir"])
        st.dataframe(df2)
	
	
	

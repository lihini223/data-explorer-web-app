import streamlit as st
import pandas as pd

from tab_df.logics import Dataset
from tab_num.logics import NumericColumn

def display_tab_num_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_num_content (function): Function that will instantiate tab_num.logics.NumericColumn class, save it into Streamlit session state and call its tab_num.logics.NumericColumn.find_num_cols() method in order to find all numeric columns.
    Then it will display a Streamlit select box with the list of numeric columns found.
    Once the user select a numeric column from the select box, it will call the tab_num.logics.NumericColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_num.logics.NumericColumn.get_summary() as a Streamlit Table
    - the graph from tab_num.logics.NumericColumn.histogram using Streamlit.altair_chart()
    - the results of tab_num.logics.NumericColumn.frequent using Streamlit.write
 
    --------------------
    Parameters
    --------------------
    -> file_path (str): File path to uploaded CSV file (optional)
    -> df (pd.DataFrame): Loaded dataframe (optional)

    --------------------
    Returns
    --------------------
    -> None

    """


    # If file_path is not None, instantiate Dataset class and save it into Streamlit session state
    if df is not None:
        df = st.session_state.dataset
    else:
        dataset = Dataset(file_path)
        df = dataset.set_df()


    # Instantiate NumericColumn class
    numeric_column = NumericColumn(file_path=file_path, df=df)

    # Save numeric_column into Streamlit session state
    st.session_state["numeric_column"] = numeric_column

    # Find numeric columns
    numeric_column.find_num_cols()

    # Display select box with numeric columns
    with st.expander("Select a numeric column"):
        st.session_state["selected_num_col"] = st.selectbox("Select a numeric column", numeric_column.num_cols)
    
    # If a numeric column is selected, compute information and display it
    if st.session_state["selected_num_col"] is not None:
        # Set data
        numeric_column.set_data()
        # Display summary
        with st.expander("ℹ️ - Summary", expanded=True):
            st.table(numeric_column.get_summary())
        # Display histogram
        with st.expander("ℹ️ - Histogram", expanded=True):
            st.altair_chart(numeric_column.histogram(), use_container_width=True)
        # Display frequent
        with st.expander("ℹ️ - Frequent", expanded=True): st.write(numeric_column.frequent())
    
    


import streamlit as st

from tab_date.logics import DateColumn

def display_tab_date_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_date_content (function): Function that will instantiate tab_date.logics.DateColumn class, save it into Streamlit session state and call its tab_date.logics.DateColumn.find_date_cols() method in order to find all datetime columns.
    Then it will display a Streamlit select box with the list of datetime columns found.
    Once the user select a datetime column from the select box, it will call the tab_date.logics.DateColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_date.logics.DateColumn.get_summary() as a Streamlit Table
    - the graph from tab_date.logics.DateColumn.histogram using Streamlit.altair_chart()
    - the results of tab_date.logics.DateColumn.frequent using Streamlit.write
 
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
    # Instantiate DateColumn class
    date_column = DateColumn(file_path=file_path, df=df)

    # Find datetime columns
    date_column.find_date_cols()

    # Display select box with datetime columns
    st.subheader("Select a datetime column")
    selected_date_col = st.selectbox("", date_column.date_cols)

    # If a datetime column is selected, compute information to be displayed
    if selected_date_col is not None:
        date_column.set_data(selected_date_col)

        # Display summary
        with st.expander("ℹ️ - Summary", expanded=True):
            st.table(date_column.get_summary())

        # Display histogram
        with st.expander("ℹ️ - Histogram", expanded=True):
            st.altair_chart(date_column.histogram(), use_container_width=True)

        # Display frequent
        with st.expander("ℹ️ - Frequent", expanded=True):
            st.write(date_column.frequent())
    
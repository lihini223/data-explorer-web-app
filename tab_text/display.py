import streamlit as st

from tab_text.logics import TextColumn

def display_tab_text_content(file_path=None, df=None):
    """
    --------------------
    Description
    --------------------
    -> display_tab_text_content (function): Function that will instantiate tab_text.logics.TextColumn class, save it into Streamlit session state and call its tab_text.logics.TextColumn.find_text_cols() method in order to find all text columns.
    Then it will display a Streamlit select box with the list of text columns found.
    Once the user select a text column from the select box, it will call the tab_text.logics.TextColumn.set_data() method in order to compute all the information to be displayed.
    Then it will display a Streamlit Expander container with the following contents:
    - the results of tab_text.logics.TextColumn.get_summary() as a Streamlit Table
    - the graph from tab_text.logics.TextColumn.histogram using Streamlit.altair_chart()
    - the results of tab_text.logics.TextColumn.frequent using Streamlit.write
 
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
    # Instantiate TextColumn class
    text_column = TextColumn(file_path=file_path, df=df)

    # Save TextColumn class into Streamlit session state
    st.session_state.text_column = text_column

    # Find text columns
    st.session_state.text_column.find_text_cols()

    # Display select box with text columns
    st.session_state.selected_text_col = st.selectbox("Select a text column", st.session_state.text_column.text_cols)

    # If a text column is selected, compute information to be displayed
    if st.session_state.selected_text_col is not None:
        st.session_state.text_column.set_data(selected_text_col=st.session_state.selected_text_col)

        # Display results in an expander container
        with st.expander("ℹ️ - Text Column Summary", expanded=True):
            st.write(st.session_state.text_column.get_summary())
            st.altair_chart(st.session_state.text_column.histogram)
            st.write(st.session_state.text_column.frequent)


    

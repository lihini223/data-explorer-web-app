# Development of Data Explorer Web App

## DSP Group 10

Members:

- Lihini Dematan Pitiyage - Student ID: 25024175
- Wanzhen Chen - Student ID: 25016179
- Tran Minh Toan Hoang - Student ID: 12625897
- Phuong Anh Pham - Student ID: 24682282


## Description
This is an interactive web application in Python using Streamlit which helps users to explore their datasets and perform some fundamental exploratory data analysis. The web application only allows users to import CSV files with the maximum of 200MB and will be using Python 3.9.18, Pandas 2.0.3, Streamlit 1.13.0.
This web application consists of two sections:

1. Menu for uploading a CSV file
2. Container with 4 tabs:
- tab_df: Overall information of the dataset and interactive exploration of its content
- tab_num: Selection of a numeric column and display data analysis results
- tab_text: Selection of a text column and display data analysis results
- tab_date: Selection of a datetime column and display data analysis results

### Challenges
Firstly, we created the conda environment named dsp_at3 on a computer which is running Windows OS and export it to txt file called requirement.txt. However, when trying to create the environment using the requirement.txt file on MacOS, and the computers would get errors. Hence, the reason is there are build strings attached to the modules in the requirements.txt file and we resolved it by using the following command: conda env export --no-builds > environment.yml.

Secondly, there is another problem when installed the streamlit module version 1.13 in conda environment but the current version of conda did not have the streamlit 1.13; therefore, we needed to upgrade the conda and then update all the modules in the conda environment dsp_at3. Then, downgrade the pandas, altair and streamlit modules one by one to get the streamlit 1.13.

Next, we got an error message as below:
* 		AttributeError: 'NoneType' object has no attribute 'df' Traceback: File "C:\Anaconda3\envs\dsp_at3\lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 562, in _run_script exec(code, module.dict) File "C:\Users\Lihini Nisansala\OneDrive - UTS\UTS\Data Science and Innovation\Year 01\Data Science Practice\Assignments\Assignment-03\app\streamlit_app.py", line 59, in display_tab_num_content(df=st.session_state.dataset.df)
This error message indicates that st.session_state.dataset.df is None. This means that st.session_state.dataset is None or st.session_state.dataset doesn't have an attribute df. To fix this, we checked whether the st.session_state.dataset and st.session_state.dataset.df are not None before calling display_tab_num_content(df=st.session_state.dataset.df). The code below shows how we resolve this issue:
If hasattr(st.session_state, ‘dataset’) and st.session_state.dataset is not None and hasattr(st.session_state.dataset, ‘df’) and st.session_state.dataset.df is not None:
        display_tab_num_content(df=st.session_state.dataset.df)
else:
st.error(‘Dataset is not loaded or df attribute is not set.’)
This code checks if st.session_state has an attribute dataset, if st.session_state.dataset is not None, if st.session_state.dataset has an attribute df, and if st.session_state.dataset.df is not None. If all these conditions are true, it calls display_tab_num_content(df=st.session_state.dataset.df). Otherwise, it displays an error message.

### Future works and recommendations
While the key objectives have been achieved, there are rooms for further development which may improve both usability and user interface of the web application, as well as enhance user satisfaction. For wider data science projects, web applications should explore the capabilities of data visualization such as interactive charts and graphs with customized visualization options such as chart colors, or chart types. Plotly library is recommended to integrate for interactive charts. Moreover, since the current maximum file size is limited to 200MB, it may be better if the tool in the future projects can support non-technical users to handle larger datasets. In larger projects, advanced statistical analysis tools should be integrated to help users extract more insights from the dataset, including descriptive statistics, machine learning models, and correlations.

## How to Setup
Step 1:  Make sure conda is installed on your computer. 
https://www.anaconda.com/download
Step 2: Go to https://github.com/lihini223/data-explorer-web-app.git and download the git repository.
Step 3: Use the requirements.yaml file to create the conda environment using the following command.
conda env create -f requirements.yaml

## How to Run the Program
Step 1:  Activate the conda environment.
            Conda activate dsp_at3
Step 2: navigate to the app folder
            cd app
Step 3:Run the streamlit application using the following command in the terminal
            Run streamlit run streamlit_app.py

## Project Structure
- README.md: A file contains overview of the project includes project description, guide to setup and run the project, project structure, citations, etc.
- requirements.txt: A list of all packages required to run the project.
- streamlit_app.py: Entry of the application which calls functions.
- sample.csv: sample CSV file which is used to run the web application.
- tab_df
  - display.py: Display overall information of columns and rows in the dataset.
  - logics.py: Define the Dataset class that makes changes following user selections.
- tab_num
  - display.py: Display overall information and histogram of numeric columns in the dataset.
  - logics.py: Define the NumericColumn class that manages and provides various statistical information about numeric columns in a dataset.
- tab_text
  - display.py: Display overall information and histogram of object columns in the dataset.
 - logics.py: Define the TextColumn class that manages and provides various statistical information about object columns in a dataset.
- tab_date
  - display.py: Display overall information and histogram of datetime columns in the dataset.
  - logics.py: Define the DateTime class that manages provides various statistical information about datetime columns in a dataset.

## Citations
- UTS Online (2022, February 11). What is data processing? https://studyonline.uts.edu.au/blog/what-data-processing
- Smith, K. A., & Smith, K. A. (2004). Teamwork and project management (2nd ed.). McGraw Hill Higher Education.
- Read the docs from Streamlit: https://docs.streamlit.io/



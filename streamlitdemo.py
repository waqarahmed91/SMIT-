import pandas as pd 
import streamlit as st


# student must submit marks of three subject and we need to tabulate and calculate the percentage and grade 
st.set_page_config('std_form', layout = 'centered')
st.title('Student information form')
st.write('Dear student, please write your name and marks')
with st.form ('Marksheet_correction_fomr'):
    name =  st.text_input('Student Name', value='')
    python = st.number_input('Enter your Pyhton marks(out of 100)', min_value=0, max_value =100)
    C = st.number_input('Enter your C marks(out of 100)', min_value=0, max_value =100)
    R = st.number_input('Enter your R marks(out of 100)', min_value=0, max_value =100)
    submit= st.form_submit_button('Submit')


# helper function 

def std_percentage (marks):

    return round((sum(marks)/ len(marks)),2)


def std_grade(pct):

    if pct >= 80:
        return "A"  
    elif pct >= 60:
        return "B"
    elif pct >= 50:
        return "C"
    elif pct >= 40:
        return "D"
    else:
        return 'F'

if submit: 
    marks = [python, C, R]
    pct = std_percentage(marks)
    grade = std_grade(pct)
    st.subheader(name)
    st.write(f'your percentage is {pct}')
    st.write(f'your grade is {grade}')

df= pd.DataFrame({'Subject': ['pyhton','C','R'],
                    'marks':[python, C, R]})

st.table(df)
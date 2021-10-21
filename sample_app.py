import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Question 1
st.title("Homework 4 app")

#Question 2
st.markdown("[Nhi Truong](https://github.com/nhiphanthuctruong)")

#Question 3 

uploaded_file = st.file_uploader(label = "Upload a CSV file, please", type = "CSV")

#Question 4: Make a pandas DataFrame from the file. 

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)


    
#Question 5: Using applymap and a lambda function, replace all string entries consisting of a single blank space " " in the DataFrame with NumPy’s not-a-number. 
    df = df.applymap(lambda x: np.nan if x == " " else x)
    
#Question 6: Using list comprehension, make a list containing the names of all the columns of the DataFrame which can be made numeric.
    
    def can_be_numeric(c):
        try:
            pd.to_numeric(df[c])
            return True
        except:
            return False
    
    #Now, let's make a list of all the columns that can be made numeric
    good_cols = [c for c in df.columns if can_be_numeric(c)]


#Question 7
#Replace columns in df that can be made numeric with their numeric values
    df[good_cols] = df[good_cols].apply(pd.to_numeric, axis = 0)

#Question 8
#Select x-axis and y-axis from st.selectbox
    x_axis = st.selectbox("Choose an x-value",good_cols)
    y_axis = st.selectbox("Choose a y-value", good_cols)
    
# Question 9 Use the range slider version of st.slider to allow the user to select the rows they want plotted. 
  # Have the minimum be 0 and the maximum be the number of rows in the file
    l = len(df)
    st.write(f"The maximun number of is {l}")
    value = st.slider("Select the range of row you would like to plot",0,l)

# Question 10
    st.write(f"Plotting [{x_axis},{y_axis}] for the row {value}")
    
# Question 11 Use st.altair_chart to display the chart with the chosen 𝑥-axis, 𝑦-axis, and rows.
    g = alt.Chart(df[:value]).mark_circle().encode(
        x = x_axis,
        y = y_axis,
        )
    st.altair_chart(g)
    
# Question 12: Include at least one extra element in the app, beyond what is specified above. Your choice.
    st.write(df.loc[:value,[x_axis]])
    st.write(df.loc[:value,[y_axis]])
# bonus points
    

    
    #st.write(st.__version__)
    #st.write(pd.__version__)
    #st.write(np.__version__)
    #st.write(alt.__version__)
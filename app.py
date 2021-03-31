import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import altair
import seaborn as sns
import plotly.express as px



col1, col2, col3 = st.beta_columns(3)


plot_types = ("histogram", "bar", "boxplot", "scatter", "line")

# TODO change for reproducibilty and use caching
np.random.seed(34)
df = pd.DataFrame(np.random.randn(100, 2), columns=["Var1", "Var2"])

st.title("Data Viz Gallery")
st.subheader(
    "A gallery of data viz with Python code for common libraries and common chart types"
)

# sidebar
chart_type = st.sidebar.selectbox("Chart type", plot_types)

"Showing:", chart_type


# plot
with col1:
    st.header("Scatterplot")
    "Matplotlib"
    with st.echo():
        fig, ax = plt.subplots()
        ax.scatter(x=df["Var1"], y=df["Var2"])
        st.pyplot(fig)

    st.write("Seaborn")
    with st.echo():
        sns.scatterplot(data=df, x="Var1", y="Var2")
        st.pyplot(fig)

    with st.echo():
        fig = px.scatter(df, x="Var1", y="Var2", title=f"Plotly Express {chart_type}")
        st.plotly_chart(fig)

with col2:
    st.header("Histogram")

    "Matplotlib"
    with st.echo():
        fig, ax = plt.subplots()
        ax.hist(df["Var1"])
        st.pyplot(fig)

    with st.echo():
        fig = px.histogram(df, "Var1", title=f"Plotly Express {chart_type}")
        st.plotly_chart(fig)

with col3:
    st.header("Bar chart")
    "Matplotlib"
    with st.echo():
        fig, ax = plt.subplots()
        ax.scatter(x=df["Var1"], y=df["Var2"])
        st.pyplot(fig)

    st.write("Seaborn")
    with st.echo():
        sns.scatterplot(data=df, x="Var1", y="Var2")
        st.pyplot(fig)

    with st.echo():
        fig = px.scatter(df, x="Var1", y="Var2", title=f"Plotly Express {chart_type}")
        st.plotly_chart(fig)


# the data
show_data = st.checkbox("See the raw data?")
if show_data:
    df

st.text(
    """Python has many data visualization libraries. This gallery is not exhaustive. 
If you would like to add code for another library, please submit a pull request."""
)

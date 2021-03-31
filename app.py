import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import altair
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")

plot_types = ("histogram", "bar", "boxplot", "scatter", "line")

# TODO change for reproducibilty and use caching
np.random.seed(34)
df = pd.DataFrame(np.random.randn(100, 2), columns=["Var1", "Var2"])

# sidebar
chart_type = st.sidebar.selectbox("Chart type", plot_types)

with st.beta_container():
    # plot
    st.header(f"Showing:  {chart_type}")

col1, col2, col3 = st.beta_columns(3)

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
        fig = px.scatter(df, x="Var1", y="Var2")
        st.plotly_chart(fig, use_container_width=True)

with col2:
    st.header("Histogram")

    "Matplotlib"
    with st.echo():
        fig, ax = plt.subplots()
        ax.hist(df["Var1"])
        st.pyplot(fig)

    "Seaborn"
    with st.echo():
        sns.histplot(data=df, x="Var1")
        st.pyplot(fig)

    "Plotly Express"
    with st.echo():
        fig = px.histogram(df, "Var1")
        st.plotly_chart(fig, use_container_width=True)

with col3:
    st.header("Bar chart")
    "Matplotlib"
    with st.echo():
        fig, ax = plt.subplots()
        ax.bar(x=df["Var1"], height=df["Var2"])
        st.pyplot(fig)

    "Seaborn"
    with st.echo():
        sns.barplot(data=df, x="Var1", y="Var2")
        st.pyplot(fig)

    "Plotly Express"
    
    with st.echo():
        fig = px.bar(df, "Var1", "Var2")
        st.plotly_chart(fig, use_container_width=True)

with st.beta_container():
    show_data = st.checkbox("See the raw data?")
    if show_data:
        df

    st.text(
        """Python has many data visualization libraries. This gallery is not exhaustive. 
    If you would like to add code for another library, please submit a pull request."""
    )

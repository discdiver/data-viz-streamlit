import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import altair
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")

plot_types = ("Histogram", "Bar", "Boxplot", "Scatter", "Line")

# TODO change for reproducibilty and use caching
np.random.seed(34)
df = pd.DataFrame(np.random.randn(100, 2), columns=["Var1", "Var2"])

# sidebar to get user type
chart_type = st.selectbox("Choose your chart type", plot_types)

with st.beta_container():
    # plot
    st.header(f"Showing:  {chart_type}")

col1, col2 = st.beta_columns(2)


def return_matplotlib_plot(plot_type: str):
    """ return matplotlib plots """

    fig, ax = plt.subplots()
    if chart_type == "Scatter":
        ax.scatter(x=df["Var1"], y=df["Var2"])
    elif chart_type == "Histogram":
        ax.hist(df["Var1"])
    elif chart_type == "Bar":
        ax.bar(x=df["Var1"], height=df["Var2"])
    return fig


def return_sns_plot(plot_type: str):
    """ return seaborn plots """

    fig, ax = plt.subplots()
    if chart_type == "Scatter":
        sns.scatterplot(data=df, x="Var1", y="Var2")
    elif chart_type == "Histogram":
        sns.histplot(data=df, x="Var1")
    elif chart_type == "Bar":
        sns.barplot(data=df, x="Var1", y="Var2")
    return fig


def return_plotly_plot(plot_type: str):
    """ return plotly plots """

    if chart_type == "Scatter":
        fig = px.scatter(df, x="Var1", y="Var2")
    elif chart_type == "Histogram":
        fig = px.histogram(df, "Var1")
    elif chart_type == "Bar":
        fig = px.bar(df, "Var1", "Var2")
    return fig


with col1:

    "Matplotlib"
    with st.echo():
        plot = return_matplotlib_plot(chart_type)
        st.pyplot(plot)

    "Seaborn"
    with st.echo():
        plot = return_sns_plot(chart_type)
        st.pyplot(plot)

    "Plotly Express"
    with st.echo():
        plot = return_plotly_plot(chart_type)
        st.plotly_chart(plot, use_container_width=True)


with st.beta_container():
    show_data = st.checkbox("See the raw data?")
    if show_data:
        df

    st.text(
        """Python has many data visualization libraries. This gallery is not exhaustive. 
    If you would like to add code for another library, please submit a pull request."""
    )

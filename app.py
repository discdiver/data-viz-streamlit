import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt


st.set_page_config(layout="wide")

plot_types = ("Histogram", "Bar", "Boxplot", "Scatter", "Line")
libs = ("Matplotlib", "Seaborn", "Plotly Express", "Altair")

# get data
@st.cache
def load_penguins():
    return sns.load_dataset("penguins")


df = load_penguins()

# start of output
with st.beta_container():
    st.title("Python Data Visualization Tour")
    st.header("Popular Plots in Popular Libraries")

# User choose user type
chart_type = st.selectbox("Choose your chart type", plot_types)

with st.beta_container():
    st.subheader(f"Showing:  {chart_type}")
    st.write("")

three_cols = st.checkbox("2 columns?")
if three_cols:
    col1, col2 = st.beta_columns(2)

# functions for creating plots and showing code
def return_matplotlib_plot(plot_type: str):
    """ return matplotlib plots """

    fig, ax = plt.subplots()
    if chart_type == "Scatter":
        with st.echo():
            ax.scatter(x=df["bill_depth_mm"], y=df["bill_length_mm"])
    elif chart_type == "Histogram":
        with st.echo():
            ax.hist(df["bill_depth_mm"])
    elif chart_type == "Bar":
        with st.echo():
            ax.bar(x=df["bill_depth_mm"], height=df["bill_length_mm"])
    elif chart_type == "Boxplot":
        with st.echo():
            ax.boxplot(x=df["bill_depth_mm"])
    elif chart_type == "Line":
        with st.echo():
            ax.plot(df["bill_depth_mm"], df["bill_length_mm"])
    return fig


def return_sns_plot(plot_type: str):
    """ return seaborn plots """

    fig, ax = plt.subplots()
    if chart_type == "Scatter":
        with st.echo():
            sns.scatterplot(data=df, x="bill_depth_mm", y="bill_length_mm")
    elif chart_type == "Histogram":
        with st.echo():
            sns.histplot(data=df, x="bill_depth_mm")
    elif chart_type == "Bar":
        with st.echo():
            sns.barplot(data=df, x="bill_depth_mm", y="bill_length_mm")
    elif chart_type == "Boxplot":
        with st.echo():
            sns.boxplot(data=df, x="bill_depth_mm")
    elif chart_type == "Line":
        with st.echo():
            sns.lineplot(data=df, x="bill_depth_mm", y="bill_length_mm")
    return fig


def return_plotly_plot(plot_type: str):
    """ return plotly plots """

    if chart_type == "Scatter":
        with st.echo():
            fig = px.scatter(df, x="bill_depth_mm", y="bill_length_mm")
    elif chart_type == "Histogram":
        with st.echo():
            fig = px.histogram(df, "bill_depth_mm")
    elif chart_type == "Bar":
        with st.echo():
            fig = px.bar(df, "bill_depth_mm", "bill_length_mm")
    elif chart_type == "Boxplot":
        with st.echo():
            fig = px.box(df, "bill_depth_mm")
    elif chart_type == "Line":
        with st.echo():
            fig = px.line(df, "bill_depth_mm", "bill_length_mm")
    return fig


def return_altair_plot(plot_type: str):
    """ return altair plots """

    if chart_type == "Scatter":
        with st.echo():
            fig = (
                alt.Chart(df)
                .mark_point()
                .encode(x="bill_depth_mm", y="bill_length_mm")
                .interactive()
            )
    elif chart_type == "Histogram":
        with st.echo():
            fig = (
                alt.Chart(df)
                .mark_bar()
                .encode(alt.X("bill_depth_mm", bin=True), y="count()")
                .interactive()
            )
    elif chart_type == "Bar":
        with st.echo():
            fig = (
                alt.Chart(df)
                .mark_bar()
                .encode(x="bill_depth_mm", y="bill_length_mm")
                .interactive()
            )
    elif chart_type == "Boxplot":
        with st.echo():
            fig = (
                alt.Chart(df)
                .mark_boxplot()
                .encode(x="bill_depth_mm:O", y="bill_length_mm:Q")
            )
    elif chart_type == "Line":
        with st.echo():
            fig = (
                alt.Chart(df)
                .mark_line()
                .encode(x="bill_depth_mm", y="bill_length_mm")
                .interactive()
            )
    return fig


# create plots
def show_plot(kind: str):
    st.write(kind)
    if kind == "Matplotlib":
        plot = return_matplotlib_plot(chart_type)
        st.pyplot(plot)
    elif kind == "Seaborn":
        plot = return_sns_plot(chart_type)
        st.pyplot(plot)
    elif kind == "Plotly Express":
        plot = return_plotly_plot(chart_type)
        st.plotly_chart(plot, use_container_width=True)
    elif kind == "Altair":
        plot = return_altair_plot(chart_type)
        st.altair_chart(plot, use_container_width=True)


# put plots in layout
if three_cols:
    with col1:
        show_plot(kind="Matplotlib")
    with col2:
        show_plot(kind="Seaborn")
    with col1:
        show_plot(kind="Plotly Express")
    with col2:
        show_plot(kind="Altair")
else:
    with st.beta_container():
        for lib in libs:
            show_plot(kind=lib)

# display data
with st.beta_container():
    show_data = st.checkbox("See the raw data?")

    if show_data:
        df

    # help out
    st.write(
        """Python has many data visualization libraries. 
        This gallery is not exhaustive. 
        If you would like to add code for another library, please check out 
        the code on GitHub and submit a pull request."""
    )

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt


st.set_page_config(layout="wide")

plot_types = ("Histogram", "Bar", "Boxplot", "Scatter", "Line")

@st.cache
def load_penguins():
    return sns.load_dataset("penguins")


df = load_penguins()


# sidebar to get user type
chart_type = st.selectbox("Choose your chart type", plot_types)

with st.beta_container():
    # plot
    st.header(f"Showing:  {chart_type}")


three_cols = st.checkbox("3 columns?")
if three_cols:
    col1, col2, col3 = st.beta_columns(3)
else:
    col1 = st.beta_columns(1)


def return_matplotlib_plot(plot_type: str):
    """ return matplotlib plots """

    fig, ax = plt.subplots()
    if chart_type == "Scatter":
        ax.scatter(x=df["bill_depth_mm"], y=df["bill_length_mm"])
    elif chart_type == "Histogram":
        ax.hist(df["bill_depth_mm"])
    elif chart_type == "Bar":
        ax.bar(x=df["bill_depth_mm"], height=df["bill_length_mm"])
    elif chart_type == "Boxplot":
        ax.boxplot(x=df["bill_depth_mm"])
    elif chart_type == "Line":
        ax.plot(df["bill_depth_mm"], df["bill_length_mm"])
    return fig


def return_sns_plot(plot_type: str):
    """ return seaborn plots """

    fig, ax = plt.subplots()
    if chart_type == "Scatter":
        sns.scatterplot(data=df, x="bill_depth_mm", y="bill_length_mm")
    elif chart_type == "Histogram":
        sns.histplot(data=df, x="bill_depth_mm")
    elif chart_type == "Bar":
        sns.barplot(data=df, x="bill_depth_mm", y="bill_length_mm")
    elif chart_type == "Boxplot":
        sns.boxplot(data=df, x="bill_depth_mm")
    elif chart_type == "Line":
        sns.lineplot(data=df, x="bill_depth_mm", y="bill_length_mm")
    return fig


@st.cache  # only one that doesn't give a warning if cache it
def return_plotly_plot(plot_type: str):
    """ return plotly plots """

    if chart_type == "Scatter":
        fig = px.scatter(df, x="bill_depth_mm", y="bill_length_mm")
    elif chart_type == "Histogram":
        fig = px.histogram(df, "bill_depth_mm")
    elif chart_type == "Bar":
        fig = px.bar(df, "bill_depth_mm", "bill_length_mm")
    elif chart_type == "Boxplot":
        fig = px.box(df, "bill_depth_mm")
    elif chart_type == "Line":
        fig = px.line(df, "bill_depth_mm", "bill_length_mm")
    return fig


def return_altair_plot(plot_type: str):
    """ return altair plots """

    if chart_type == "Scatter":
        fig = alt.Chart(df).mark_bar().encode(x="bill_depth_mm", y="bill_length_mm")
    elif chart_type == "Histogram":
        fig = alt.Chart(df).mark_bar().encode(x="bill_depth_mm", y="bill_length_mm")
    elif chart_type == "Bar":
        fig = alt.Chart(df).mark_bar().encode(x="bill_depth_mm", y="bill_length_mm")
    elif chart_type == "Boxplot":
        fig = alt.Chart(df).mark_bar().encode(x="bill_depth_mm", y="bill_length_mm")
    elif chart_type == "Line":
        fig = alt.Chart(df).mark_bar().encode(x="bill_depth_mm", y="bill_length_mm")
    return fig


# functions to output data


def show_plt():
    st.write("Matplotlib")
    with st.echo():
        plot = return_matplotlib_plot(chart_type)
        st.pyplot(plot)


def show_seaborn():
    st.write("Seaborn")
    with st.echo():
        plot = return_sns_plot(chart_type)
        st.pyplot(plot)


def show_plotly():
    st.write("Plotly Express")
    with st.echo():
        plot = return_plotly_plot(chart_type)
        st.plotly_chart(plot, use_container_width=True)


def show_altair():
    st.write("Altair")
    with st.echo():
        plot = return_altair_plot(chart_type)
        st.altair_chart(plot, use_container_width=True)


# output
if three_cols:
    with col1:
        show_plt()
else:
    show_plt()

if three_cols:
    with col2:
        show_seaborn()
else:
    show_seaborn()

if three_cols:
    with col3:
        show_plotly()
else:
    show_plotly()

if three_cols:
    with col1:
        show_altair()
else:
    show_altair()


with st.beta_container():
    show_data = st.checkbox("See the raw data?")

    if show_data:
        df

    st.text(
        """Python has many data visualization libraries. This gallery is not exhaustive. 
    If you would like to add code for another library, please submit a pull request."""
    )

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt
from bokeh.plotting import figure
from make_plots import (
    matplotlib_plot,
    sns_plot,
    pd_plot,
    plotly_plot,
    altair_plot,
    bokeh_plot,
)


# can only set this once, first thing to set
st.set_page_config(layout="wide")

plot_types = (
    "Scatter",
    "Histogram",
    "Bar",
    "Line",
    "3D Scatter",
)  # maybe add 'Boxplot' after fixes
libs = (
    "Matplotlib",
    "Seaborn",
    "Plotly Express",
    "Altair",
    "Pandas Matplotlib",
    "Bokeh",
)

# get data
# @st.cache(allow_output_mutation=True) # maybe source of resource limit issue
def load_penguins():
    return sns.load_dataset("penguins")


pens_df = load_penguins()
df = pens_df.copy()
df.index = pd.date_range(start="1/1/18", periods=len(df), freq="D")


with st.beta_container():
    st.title("Python Data Visualization Tour")
    st.header("Popular plots in popular plotting libraries")
    st.write("""See the code and plots for five libraries at once.""")


# User choose type
chart_type = st.selectbox("Choose your chart type", plot_types)

with st.beta_container():
    st.subheader(f"Showing:  {chart_type}")
    st.write("")

two_cols = st.checkbox("2 columns?", True)
if two_cols:
    col1, col2 = st.beta_columns(2)


# create plots
def show_plot(kind: str):
    st.write(kind)
    if kind == "Matplotlib":
        plot = matplotlib_plot(chart_type, df)
        st.pyplot(plot)
    elif kind == "Seaborn":
        plot = sns_plot(chart_type, df)
        st.pyplot(plot)
    elif kind == "Plotly Express":
        plot = plotly_plot(chart_type, df)
        st.plotly_chart(plot, use_container_width=True)
    elif kind == "Altair":
        plot = altair_plot(chart_type, df)
        st.altair_chart(plot, use_container_width=True)
    elif kind == "Pandas Matplotlib":
        plot = pd_plot(chart_type, df)
        st.pyplot(plot)
    elif kind == "Bokeh":
        plot = bokeh_plot(chart_type, df)
        st.bokeh_chart(plot, use_container_width=True)


# output plots
if two_cols:
    with col1:
        show_plot(kind="Matplotlib")
    with col2:
        show_plot(kind="Seaborn")
    with col1:
        show_plot(kind="Plotly Express")
    with col2:
        show_plot(kind="Altair")
    with col1:
        show_plot(kind="Pandas Matplotlib")
    with col2:
        show_plot(kind="Bokeh")
else:
    with st.beta_container():
        for lib in libs:
            show_plot(kind=lib)

# display data
with st.beta_container():
    show_data = st.checkbox("See the raw data?")

    if show_data:
        df

    # notes
    st.subheader("Notes")
    st.write(
        """
        - This app uses [Streamlit](https://streamlit.io/) and the [Palmer Penguins](https://allisonhorst.github.io/palmerpenguins/) dataset.      
        - To see the full code check out the [GitHub repo](https://github.com/discdiver/data-viz-streamlit).
        - Plots are interactive where that's the default or easy to add.
        - Plots that use MatPlotlib under the hood have fig and ax objects defined before the code shown.
        - Lineplots should have sequence data, so I created a date index with a sequence of dates for them. 
        - Where an axis label shows by default, I left it at is. Generally where it was missing, I added it.
        - There are multiple ways to make some of these plots.
        - You can choose to see two columns, but with a narrow screen this will switch to one column automatically.
        - Python has many data visualization libraries. This gallery is not exhaustive. If you would like to add code for another library, please submit a [pull request](https://github.com/discdiver/data-viz-streamlit).
        - For a larger tour of more plots, check out the [Python Graph Gallery](https://www.python-graph-gallery.com/density-plot/) and [Python Plotting for Exploratory Data Analysis](https://pythonplot.com/).
        - The interactive Plotly Express 3D Scatterplot is cool to play with. Check it out! 😎
        
        Made by [Jeff Hale](https://www.linkedin.com/in/-jeffhale/). 
        
        Subscribe to my [Data Awesome newsletter](https://dataawesome.com) for the latest tools, tips, and resources.
        """
    )

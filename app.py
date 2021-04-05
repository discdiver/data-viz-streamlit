import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt

# can only set this once, first thing to set
st.set_page_config(layout="wide")

plot_types = (
    "Scatter",
    "Histogram",
    "Bar",
    "Line",
    "3D Scatter",
)  # add 'Boxplot' after fixes
libs = ("Matplotlib", "Seaborn", "Plotly Express", "Altair", "Pandas Matplotlib")

# get data
@st.cache(allow_output_mutation=True)
def load_penguins():
    return sns.load_dataset("penguins")


pens_df = load_penguins()
df = pens_df.copy()
df.index = pd.date_range(start="1/1/18", periods=len(df), freq="D")


with st.beta_container():
    st.title("Python Data Visualization Tour")
    st.header("Popular plots in popular plotting libraries")
    st.write("""See the code and plots for five libraries at once.""")


# User choose user type
chart_type = st.selectbox("Choose your chart type", plot_types)

with st.beta_container():
    st.subheader(f"Showing:  {chart_type}")
    st.write("")

three_cols = st.checkbox("2 columns?")
if three_cols:
    col1, col2 = st.beta_columns(2)


def return_matplotlib_plot(plot_type: str):
    """ return matplotlib plots """

    fig, ax = plt.subplots()
    if chart_type == "Scatter":
        with st.echo():
            df["color"] = df["species"].replace(
                {"Adelie": 1, "Chinstrap": 2, "Gentoo": 3}
            )
            ax.scatter(x=df["bill_depth_mm"], y=df["bill_length_mm"], c=df["color"])
            plt.title("Bill Depth by Bill Length")
            plt.xlabel("Bill Depth (mm)")
            plt.ylabel("Bill Length (mm)")
    elif chart_type == "Histogram":
        with st.echo():
            plt.title("Count of Bill Depth Observations")
            ax.hist(df["bill_depth_mm"])
            plt.xlabel("Bill Depth (mm)")
            plt.ylabel("Count")
    elif chart_type == "Bar":
        with st.echo():
            ax.bar(x=df["species"], height=df["bill_depth_mm"])
            plt.title("Mean Bill Depth by Species")
            plt.xlabel("Species")
            plt.ylabel("Mean Bill Depth (mm)")
    elif chart_type == "Boxplot":
        "Bug, can't plot matplotlib boxplot."
        # with st.echo():
        #     bp = ax.boxplot(x=df[["bill_depth_mm", 'bill_length_mm']], showfliers=True, sym='k.',
        #     positions=[1, 2],
        #     patch_artist=True)
        #     for flier in bp['fliers']:    # outliers
        #         flier.set_markersize(9)
        #         flier.set_marker('v')
        #     for box in bp['boxes']:     # box bodys
        #         box.set_facecolor('green')
        #         box.set_edgecolor('black')
        #         box.set_linewidth(2)
        #     for whisker in bp['whiskers']:   # whisker line
        #         whisker.set_linewidth(5)
        #     for cap in bp['caps']:     # cap line
        #         cap.set_color('red')
        #         cap.set_linewidth(10)
        #     for median in bp['medians']:   # median line
        #         median.set_linewidth(15)
        #     # for flier in bp['fliers']:
        #     #     flier.set(marker='o', color='#e7298a', alpha=0.5)
        #     # bp
        #     # bp['boxes'][0]

        #     # bp
        #     fig
        #     st.pyplot(fig)
    elif chart_type == "Line":
        with st.echo():
            ax.plot(df.index, df["bill_length_mm"])
            plt.title("Bill Length Over Time")
            plt.ylabel("Bill Length (mm)")
    elif chart_type == "3D Scatter":
        ax = fig.add_subplot(projection="3d")
        with st.echo():
            df["color"] = df["species"].replace(
                {"Adelie": 1, "Chinstrap": 2, "Gentoo": 3}
            )
            ax.scatter3D(
                xs=df["bill_depth_mm"],
                ys=df["bill_length_mm"],
                zs=df["body_mass_g"],
                c=df["color"],
            )
            ax.set_xlabel("bill_depth_mm")
            ax.set_ylabel("bill_length_mm")
            ax.set_zlabel("body_mass_g")
            plt.title("3D Scatterplot")
    return fig


def return_sns_plot(plot_type: str):
    """ return seaborn plots """

    fig, ax = plt.subplots()
    if chart_type == "Scatter":
        with st.echo():
            sns.scatterplot(
                data=df,
                x="bill_depth_mm",
                y="bill_length_mm",
                hue="species",
            )
            plt.title("Bill Depth by Bill Length")
    elif chart_type == "Histogram":
        with st.echo():
            sns.histplot(data=df, x="bill_depth_mm")
            plt.title("Count of Bill Depth Observations")
    elif chart_type == "Bar":
        with st.echo():
            sns.barplot(data=df, x="species", y="bill_depth_mm")
            plt.title("Mean Bill Depth by Species")
    elif chart_type == "Boxplot":
        with st.echo():
            sns.boxplot(data=df)
            plt.title("Bill Depth Observations")
    elif chart_type == "Line":
        with st.echo():
            sns.lineplot(data=df, x=df.index, y="bill_length_mm")
            plt.title("Bill Length Over Time")
    elif chart_type == "3D Scatter":
        st.write("Seaborn doesn't do 3D ☹️. Here's 2D.")
        sns.scatterplot(data=df, x="bill_depth_mm", y="bill_length_mm", hue="island")
        plt.title("Just a 2D Scatterplot")
    return fig


def return_plotly_plot(plot_type: str):
    """ return plotly plots """

    if chart_type == "Scatter":
        with st.echo():
            fig = px.scatter(
                data_frame=df,
                x="bill_depth_mm",
                y="bill_length_mm",
                color="species",
                title="Bill Depth by Bill Length",
            )
    elif chart_type == "Histogram":
        with st.echo():
            fig = px.histogram(
                data_frame=df,
                x="bill_depth_mm",
                title="Count of Bill Depth Observations",
            )
    elif chart_type == "Bar":
        with st.echo():
            fig = px.bar(
                data_frame=df.groupby(["species"]).mean().reset_index(),
                x="species",
                y="bill_depth_mm",
                title="Mean Bill Depth by Species",
            )
            # by default shows stacked bar chart (sum) with individual hover values
    elif chart_type == "Boxplot":
        with st.echo():
            fig = px.box(data_frame=df, x="species", y="bill_depth_mm")
    elif chart_type == "Line":
        with st.echo():
            fig = px.line(
                data_frame=df,
                x=df.index,
                y="bill_length_mm",
                title="Bill Length Over Time",
            )
    elif chart_type == "3D Scatter":
        with st.echo():
            fig = px.scatter_3d(
                data_frame=df,
                x="bill_depth_mm",
                y="bill_length_mm",
                z="body_mass_g",
                color="species",
                title="Interactive 3D Scatterplot!",
            )

    return fig


def return_altair_plot(plot_type: str):
    """ return altair plots """

    if chart_type == "Scatter":
        with st.echo():
            fig = (
                alt.Chart(
                    df,
                    title="Bill Depth by Bill Length",
                )
                .mark_point()
                .encode(x="bill_depth_mm", y="bill_length_mm", color="species")
                .interactive()
            )
    elif chart_type == "Histogram":
        with st.echo():
            fig = (
                alt.Chart(df, title="Count of Bill Depth Observations")
                .mark_bar()
                .encode(alt.X("bill_depth_mm", bin=True), y="count()")
                .interactive()
            )
    elif chart_type == "Bar":
        with st.echo():
            fig = (
                alt.Chart(df, title="Mean Bill Depth by Species")
                .mark_bar()
                .encode(x="species", y="bill_depth_mm")
                .interactive()
            )
    elif chart_type == "Boxplot":
        with st.echo():
            fig = (
                alt.Chart(df).mark_boxplot().encode(x="species:O", y="bill_depth_mm:Q")
            )
    elif chart_type == "Line":
        with st.echo():
            fig = (
                alt.Chart(df.reset_index(), title="Bill Length Over Time")
                .mark_line()
                .encode(x="index:T", y="bill_length_mm:Q")
                .interactive()
            )
    elif chart_type == "3D Scatter":
        st.write("Altair doesn't do 3D ☹️. Here's 2D.")
        fig = (
            alt.Chart(df, title="Just a 2D Scatterplot")
            .mark_point()
            .encode(x="bill_depth_mm", y="bill_length_mm", color="species")
            .interactive()
        )
    return fig


def return_pd_plot(plot_type: str):
    """ return pd matplotlib plots """

    fig, ax = plt.subplots()
    if chart_type == "Scatter":
        with st.echo():
            df["color"] = df["species"].replace(
                {"Adelie": "blue", "Chinstrap": "orange", "Gentoo": "green"}
            )
            ax_save = df.plot(
                kind="scatter",
                x="bill_depth_mm",
                y="bill_length_mm",
                c="color",
                ax=ax,
                title="Bill Depth by Bill Length",
            )
    elif chart_type == "Histogram":
        with st.echo():
            ax_save = df["bill_depth_mm"].plot(
                kind="hist", ax=ax, title="Count of Bill Depth Observations"
            )
            plt.xlabel("Bill Depth (mm)")
    elif chart_type == "Bar":
        with st.echo():
            ax_save = (
                df.groupby("species")
                .mean()
                .plot(
                    kind="bar",
                    y="bill_depth_mm",
                    title="Mean Bill Depth by Species",
                    ax=ax,
                )
            )
            plt.ylabel("Bill Depth (mm)")
    elif chart_type == "Boxplot":
        with st.echo():
            ax_save = df.plot(kind="box", ax=ax)
    elif chart_type == "Line":
        with st.echo():
            ax_save = df.plot(kind="line", use_index=True, y="bill_length_mm", ax=ax)
            plt.title("Bill Length Over Time")
            plt.ylabel("Bill Length (mm)")
    elif chart_type == "3D Scatter":
        st.write("Pandas doesn't do 3D ☹️. Here's 2D.")
        ax_save = df.plot(kind="scatter", x="bill_depth_mm", y="bill_length_mm", ax=ax)
        plt.title("Just a 2D Scatterplot")
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
    elif kind == "Pandas Matplotlib":
        plot = return_pd_plot(chart_type)
        st.pyplot(plot)


# output plots
if three_cols:
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
        - Color was added to scatterplots. 
        - Where an axis label shows by default, I left it at is. Generally were it was missing, I added it.
        - There are multiple ways to make some of these plots.
        - You can choose to see two columns, but with a narrow screen this will switch to one column automatically.
        - Python has many data visualization libraries. This gallery is not exhaustive. If you would like to add code for another library, please submit a [pull request](https://github.com/discdiver/data-viz-streamlit).
        - For a larger tour of more plots, check out the [Python Graph Gallery](https://www.python-graph-gallery.com/density-plot/)
        - The interactive Plotly Express 3D Scatterplot is cool to play with. Check it out! 😎
        
        Made by Jeff Hale. 
        
        Subscribe to my [Data Awesome newsletter](https://dataawesome.com) for the latest tools, tips, and resources.
        """
    )

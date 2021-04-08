import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt
from bokeh.plotting import figure


def matplotlib_plot(chart_type: str, df):
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
            df_plt = df.groupby("species", dropna=False).mean().reset_index()
            ax.bar(x=df_plt["species"], height=df_plt["bill_depth_mm"])
            plt.title("Mean Bill Depth by Species")
            plt.xlabel("Species")
            plt.ylabel("Mean Bill Depth (mm)")

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


def sns_plot(chart_type: str, df):
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


def plotly_plot(chart_type: str, df):
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
            fig = px.histogram(
                data_frame=df,
                x="species",
                y="bill_depth_mm",
                title="Mean Bill Depth by Species",
                histfunc="avg",
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


def altair_plot(chart_type: str, df):
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
                alt.Chart(
                    df.groupby("species", dropna=False).mean().reset_index(),
                    title="Mean Bill Depth by Species",
                )
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


def pd_plot(chart_type: str, df):
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
                df.groupby("species", dropna=False)
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


def bokeh_plot(chart_type: str, df):
    """ return bokeh plots """

    if chart_type == "Scatter":
        with st.echo():
            df["color"] = df["species"].replace(
                {"Adelie": "blue", "Chinstrap": "orange", "Gentoo": "green"}
            )
            fig = figure(title="Bill Depth by Bill Length")
            fig.circle(source=df, x="bill_depth_mm", y="bill_length_mm", color="color")
    elif chart_type == "Histogram":
        with st.echo():
            hist, edges = np.histogram(df["bill_depth_mm"].dropna(), bins=10)
            fig = figure(title="Count of Bill Depth Observations")
            fig.quad(
                top=hist, bottom=0, left=edges[:-1], right=edges[1:], line_color="white"
            )

    elif chart_type == "Bar":
        with st.echo():
            fig = figure(
                title="Mean Bill Depth by Species",
                x_range=["Gentoo", "Chinstrap", "Adelie"],
            )

            fig.vbar(
                source=df.groupby("species", dropna=False).mean(),
                x="species",
                top="bill_depth_mm",
                width=0.8,
            )

    elif chart_type == "Line":
        with st.echo():
            fig = figure(title="Bill Length Over Time", x_axis_type="datetime")
            fig.line(source=df.reset_index(), x="index", y="bill_length_mm")

    elif chart_type == "3D Scatter":
        st.write("Bokeh doesn't do 3D ☹️. Here's 2D.")

        df["color"] = df["species"].replace(
            {"Adelie": "blue", "Chinstrap": "orange", "Gentoo": "green"}
        )
        fig = figure(title="Bill Depth by Bill Length")
        fig.circle(source=df, x="bill_depth_mm", y="bill_length_mm", color="color")

    return fig

import pandas as pd
import plotly.express as px


def create_gantt_chart(tasks, view_option="Month"):
    df = pd.DataFrame(tasks)
    fig = px.timeline(
        df,
        x_start="Start",
        x_end="Finish",
        color="Resource",
        text="Task",
    )
    fig.update_yaxes(
        categoryorder="total ascending",
        showticklabels=False,
    )

    if view_option == "Day":
        fig.update_xaxes(tickformat="%b %d")
    elif view_option == "Week":
        fig.update_xaxes(
            tickformat="%b %d",
            dtick="M1",
            ticklabelmode="period",
            tickvals=pd.date_range(
                start=df["Start"].min(), end=df["Finish"].max(), freq="W-MON"
            ),
            minor=dict(ticklen=4, tickcolor="lightgrey"),  # 追加: サブティック
        )
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="LightGrey")
    else:
        fig.update_xaxes(tickformat="%b %Y", dtick="M1")

    task_count = len(df)
    fig_height = 80 * task_count
    fig.update_traces(
        textposition="auto",
        insidetextanchor="middle",
        # textangle="auto",
    )
    fig.update_layout(
        xaxis=dict(side="top"),
        height=fig_height,
        margin=dict(l=200),
    )

    return fig

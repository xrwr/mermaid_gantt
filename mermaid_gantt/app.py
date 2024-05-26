import streamlit as st

from mermaid_gantt.gantt_chart import create_gantt_chart
from mermaid_gantt.parser import parse_mermaid


def main():
    st.title("Mermaid to Gantt Chart Converter")
    st.markdown("## Enter your tasks in Mermaid format:")
    st.markdown(
        "Format: `task_name: start_date, end_date` or `task_name: done, start_date, end_date`"
    )

    mermaid_input = st.text_area("Mermaid Input", height=200)

    if mermaid_input:
        tasks = parse_mermaid(mermaid_input)
        view_option = st.sidebar.selectbox("View by", ["Week"])
        fig = create_gantt_chart(tasks, view_option)
        st.plotly_chart(fig)
        st.dataframe(tasks)


if __name__ == "__main__":
    main()

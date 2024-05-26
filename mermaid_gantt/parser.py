from datetime import datetime


def parse_mermaid(mermaid_text):
    lines = mermaid_text.strip().split("\n")
    tasks = []
    for line in lines:
        parts = line.split(":")
        task_name = parts[0].strip()
        dates = parts[1].strip().split(",")
        status = "done" if "done" in task_name else "in_progress"
        start_date = datetime.strptime(dates[-2].strip(), "%Y-%m-%d")
        end_date = datetime.strptime(dates[-1].strip(), "%Y-%m-%d")
        tasks.append(
            {
                "Task": task_name.replace("done", "").strip(),
                "Start": start_date,
                "Finish": end_date,
                "Resource": status,
            }
        )
    return tasks

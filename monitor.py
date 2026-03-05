from datetime import datetime
import json
import os

# Absolute project path (important for cron)
BASE_DIR = "/mnt/c/Users/rajashekar reddy/OneDrive/Desktop/log_monitor_project"

STATE_FILE = os.path.join(BASE_DIR, "state.json")
LOG_FILE = os.path.join(BASE_DIR, "server.log")
REPORT_FILE = os.path.join(BASE_DIR, "report.txt")


def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as file:
            return json.load(file)
    else:
        return {
            "last_line_count": 0,
            "total_errors": 0,
            "total_warnings": 0
        }


def save_state(state):
    with open(STATE_FILE, "w") as file:
        json.dump(state, file)


def analyze_log(state):
    error_count = 0
    warning_count = 0

    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()

            new_lines = lines[state["last_line_count"]:]

            for line in new_lines:
                if "ERROR" in line:
                    error_count += 1
                if "WARNING" in line:
                    warning_count += 1

            state["last_line_count"] = len(lines)
            state["total_errors"] += error_count
            state["total_warnings"] += warning_count

        return error_count, warning_count

    except FileNotFoundError:
        print("Log file not found!")
        return None, None


def generate_report(new_errors, new_warnings, state):
    current_time = datetime.now()

    with open(REPORT_FILE, "a") as report:
        report.write(f"\nLog Report - {current_time}\n")
        report.write(f"New Errors: {new_errors}\n")
        report.write(f"New Warnings: {new_warnings}\n")
        report.write(f"Total Errors So Far: {state['total_errors']}\n")
        report.write(f"Total Warnings So Far: {state['total_warnings']}\n")

    print("Report updated!")


def main():
    state = load_state()

    print("Running scheduled log check...")

    new_errors, new_warnings = analyze_log(state)

    if new_errors is not None and (new_errors > 0 or new_warnings > 0):
        generate_report(new_errors, new_warnings, state)
        save_state(state)
    else:
        print("No new errors or warnings found.")

    print("Log check completed.\n")


if __name__ == "__main__":
    main()

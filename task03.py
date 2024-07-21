import sys


def parse_log_line(line: str) -> dict:
    """Parse a log line and return a dictionary with log"""
    parts = line.split(' ', 3)
    log_dict = {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }
    return log_dict


def load_logs(file_path: str) -> list:
    """Load logs from a file and return a list of log dictionaries"""
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Error: Failed to read file '{file_path}'. {e}")
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Filter logs by the specified log level."""
    return [log for log in logs if log['level'] == level]


def count_logs_by_level(logs: list) -> dict:
    """Count logs by log level."""
    counts = {
        'INFO': 0,
        'DEBUG': 0,
        'ERROR': 0,
        'WARNING': 0
    }
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
    return counts


def display_log_counts(counts: dict):
    """Display log counts in a formatted table."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count:<8}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python task03.py <path_to_logfile> [log_level]")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2].upper()
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
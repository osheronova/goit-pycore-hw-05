import sys                     
from collections import Counter 

# Parse one line of log text → dictionary with 4 keys
def parse_log_line(line):
    d, t, lvl, msg = line.strip().split(" ", 3)   # Split into date, time, level, and message
    return {"date": d, "time": t, "level": lvl, "message": msg}

# Read file and parse each non-empty line
def load_logs(path):
    try:
        with open(path, encoding="utf-8") as f:   
            return [parse_log_line(x) for x in f if x.strip()]  # Parse only non-empty lines
    except FileNotFoundError:                     
        print(f"Error: File '{path}' not found.")
        sys.exit(1)                               

# Filter logs by specific level
def filter_by_level(logs, lvl):
    return list(filter(lambda r: r["level"].lower() == lvl.lower(), logs))

# Count log entries by level using Counter
def level_counts(logs):
    return Counter(map(lambda r: r["level"], logs))

# Main program
def main():
    if len(sys.argv) < 2:  # Check if log file argument is provided
        print("Usage: python task3_optional.py <log_file_path> [log_level]")
        sys.exit(1)

    logs = load_logs(sys.argv[1])       # Load logs from provided file path
    counts = level_counts(logs)         # Count entries by level

    # Display summary table
    print("Logging Level | Count")
    print("----------------|------")
    for k, v in counts.items():
        print(f"{k:<15} | {v:<5}")     # Table-like format output style

    # If user requested a specific log level
    if len(sys.argv) == 3:
        lvl = sys.argv[2]                               # Read requested level
        picked = filter_by_level(logs, lvl)              # Get only logs of that level
        print(f"\nLog details for level '{lvl.upper()}':")
        # Print all matching log lines, or show "not found" message
        print("\n".join(f"{r['date']} {r['time']} - {r['message']}" for r in picked) or
              f"No entries found for level '{lvl}'.")

if __name__ == "__main__":
    main()

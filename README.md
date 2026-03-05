# Automated Log Monitoring System

This project is a Python-based log monitoring system that automatically analyzes server log files and detects error and warning messages.

## Features
- Reads continuously growing log files
- Detects ERROR and WARNING messages
- Processes only new log entries
- Maintains persistent state using JSON
- Generates timestamped reports
- Runs automatically using Linux cron scheduler

## Technologies Used
Python  
Linux (Ubuntu / WSL)  
Cron Scheduler  
JSON  

## Project Workflow
1. Python script reads the log file.
2. Only new lines are processed.
3. ERROR and WARNING messages are detected.
4. State is stored in state.json.
5. Report is generated in report.txt.
6. Script runs automatically using cron.

## Author
Nithin Dubasi

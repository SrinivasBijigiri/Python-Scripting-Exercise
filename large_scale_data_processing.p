import json

with open('logs.json') as f:
    logs = json.load(f)

summary = {}
for log in logs:
    level = log.get('level', 'INFO')
    summary[level] = summary.get(level, 0) + 1

print("Log summary:", summary)

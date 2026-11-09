import json
import os
import sys
from pathlib import Path

import django

project_directory = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_directory))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

from ai_analyzer.ai_client import analyze_ticket

file_path = Path(__file__).resolve().parent / "test_cases.json"

with open(file_path, encoding="utf-8") as file:
    data = json.load(file)

total_tests = len(data)
completed_analyses = 0
category_passes = 0
priority_passes = 0
for item in data:
    result = analyze_ticket(item["complaint"])

    if result is not None:
        completed_analyses += 1
        category_match = result.category == item["expected_category"]
        if category_match:
            category_passes += 1

        priority_match = result.priority == item["expected_priority"]
        if priority_match:
            priority_passes += 1

        print(
            f"Expected Category: {item['expected_category']}, Actual: {result.category}, Evaluation(true=PASS/false=FAIL): {category_match}"
        )

        print(
            f"Expected Priority: {item['expected_priority']}, Actual: {result.priority}, Evaluation(true=PASS/false=FAIL): {priority_match}"
        )

    else:
        print("AI analysis failed")

print(
    f"Tests attempted: {total_tests},\nAnalyses completed: {completed_analyses},\nCategory passes: {category_passes},\nPriority passes: {priority_passes}"
)


# print(f"{len(data)} test cases loaded.")

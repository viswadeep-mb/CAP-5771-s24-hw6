#!/bin/bash

# Runs on Gradescope server
export PYTHONPATH=/autograder/MAKE-STUDENT-OUTPUT/CODE:.:pytest_utils:src_with_answers

#due_date="2024-02-15"
due_date=""  # fill in

# Current date in YYYY-MM-DD format
current_date=$(date '+%Y-%m-%d')
echo "current_date" : $current_date
echo "due_date" : $due_date

if [[ "$current_date" < "$due_date" ]]; then
    echo "Current date is earlier than the due date."

    pytest -s tests/test_structure.py

elif [[ "$current_date" > "$due_date" ]]; then
    echo "Current date is later than the due date."

    pytest -s tests/test_structure.py
    pytest -s tests/test_answers.py
else
    echo "Current date is the due date."
fi


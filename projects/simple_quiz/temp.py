from simple_quiz import read_quiz_data

try:
    quiz_data = read_quiz_data("quiz_data.json")
    print("Quiz data loaded successfully!")
    # ... use quiz_data ...
except Exception as e:
    print(f"An error occurred: {e}")

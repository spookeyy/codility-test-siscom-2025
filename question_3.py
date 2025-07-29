"""You’re building a system to grade multiple-choice quizzes. Each quiz has:
    A set of questions with fixed answers
    Each student submits answers to the quiz

You are given:
    correct_answers: a list of the correct options (e.g., ['A', 'C', 'B'])
    student_submissions: a list of student objects:
        student_id
        answers: a list of their selected answers

Rules:
    For each correct answer, the student gets +4 points
    For each wrong answer, -1 point
    No answer (represented by None) gets 0 points
    
Write a function that returns a dictionary mapping each student_id to their total score.


INPUT """
correct_answers = ['A', 'C', 'B', 'D']

student_submissions = [
    {"student_id": "S1", "answers": ['A', 'C', 'B', 'D']},  # all correct
    {"student_id": "S2", "answers": ['A', 'C', 'D', 'B']},  # 2 correct, 2 wrong
    {"student_id": "S3", "answers": ['A', None, 'B', 'C']}  # 2 correct, 1 wrong, 1 skipped
]


"OUTPUT"
{
    "S1": 16,    # 4x4
    "S2": 6,     # 4 + 4 -1 -1
    "S3": 7      # 4 (A) + 0 (None) + 4 (B) -1 (C)
}


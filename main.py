import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing is a useful skill to have.",
    "Practice makes perfect.",
    "Python is a great programming language.",
    "I love coding and learning new things.",
    "The rain in Spain stays mainly in the plain.",
    "She sells seashells by the seashore.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question."
]

def measure_accuracy(user_input, test_sentence):
    user_words = user_input.split()
    test_words = test_sentence.split()
    correct_words = sum(1 for u, t in zip(user_words, test_words) if u == t)
    total_words = len(test_words)
    accuracy = (correct_words / total_words) * 100
    return accuracy

def typing_speed_test():
    test_sentence = random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(f"\n{test_sentence}\n")
    input("Press Enter to start...")
    start_time = time.time()
    user_input = input("\nstart typing: ")
    end_time = time.time()
    time_taken = end_time - start_time
    time_taken_in_minutes = time_taken / 60
    word_count = len(test_sentence.split())
    wpm = word_count / time_taken_in_minutes
    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Words per minute (WPM): {wpm:.2f}")
    
    if user_input == test_sentence:
        print("Correct! Well done.")
    else:
        print("Incorrect. Keep practicing!")
    
    result={
        "time_taken_seconds": time_taken,
        "wpm": wpm,
        "correct": user_input == test_sentence
    }
    print(result)

    accuracy = measure_accuracy(user_input, test_sentence)
    print(f"Accuracy: {accuracy:.2f}%")



typing_speed_test()
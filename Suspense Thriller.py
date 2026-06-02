# import time
# import os
# import random

# # ---------- Utility Functions ----------
# def slow_print(text, delay=0.05):
#     for char in text:
#         print(char, end='', flush=True)
#         time.sleep(delay)
#     print()

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# # ---------- GK Puzzle Function ----------
# def gk_question():
#     while True:
#         slow_print("Puzzle: Which city is the capital of Pakistan?")
#         answer = input("Your answer: ").strip().lower()
#         if answer == "islamabad":
#             slow_print("\nCorrect! You solved the GK puzzle.\n")
#             input("Press Enter to continue to the mini puzzle...")
#             break
#         else:
#             slow_print("Incorrect! Try again.\n")

# # ---------- Mini Puzzle Function ----------
# def mini_puzzle():
#     a = random.randint(1, 10)
#     b = random.randint(1, 10)
#     while True:
#         slow_print(f"Mini Puzzle: What is {a} x {b}?")
#         try:
#             answer = int(input("Your answer: "))
#             if answer == a * b:
#                 slow_print("\nCorrect! The shadows shift...\n")
#                 input("Press Enter to continue...")
#                 break
#             else:
#                 slow_print("Wrong! Try again.\n")
#         except:
#             slow_print("Enter a valid number.\n")

# # ---------- Introduction ----------
# def intro():
#     clear_screen()
#     slow_print("You wake up in a dimly lit room...")
#     slow_print("A mysterious note appears on the table:\n'Only those with knowledge shall know their fate.'\n")
#     input("Press Enter to solve the puzzle...")

# # ---------- Final Screen ----------
# def final_screen():
#     clear_screen()
#     slow_print("A voice finally speaks clearly...\n")
#     slow_print("'Kal jana ha college?' 🤔\n")
#     choice = input("Will you go? (yes/no): ").strip().lower()
#     if choice == "yes":
#         slow_print("\nYou gather your courage and prepare for college. 📚")
#         slow_print("The mystery has been solved. Well done!")
#     else:
#         slow_print("\nYou decide to stay home. The mystery remains unsolved. 🕵️‍♂️")

# # ---------- Main ----------
# def main():
#     intro()
#     gk_question()
#     mini_puzzle()
#     final_screen()

# if __name__ == "__main__":
#     main()


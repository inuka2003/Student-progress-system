Student Progression Analysis 📊
This Python program helps in analyzing and visualizing student progression based on credits obtained in different categories: Pass, Defer, and Fail credits. It calculates and displays the outcomes such as Progress, Trailer, Retriever, or Exclude, followed by a graphical representation of the results using a histogram.

Features ✨
User Input Validation: Ensures that the entered credits are within valid ranges.
Outcome Calculation: Based on user input, the program calculates whether the student is in the "Progress," "Trailer," "Retriever," or "Exclude" category.
Histogram Visualization: A graphical representation of the results for better understanding.
Data Persistence: Saves the progression data to a text file for future reference.

Technologies Used 💻
Python 3.x
Graphics Library (graphics.py)

Requirements 🛠️
Python 3.x or higher
graphics.py library for graphical output (can be downloaded here)

How to Use 📋
Input Credits: Enter the number of Pass, Defer, and Fail credits when prompted. The program will calculate the progression based on these values.

Progression Outcomes: The outcomes can be:

Progress: If Pass credits are 120.
Progress (module trailer): If Pass credits are 100, and Defer/Fall credits are within valid ranges.
Module retriever: If the credits fall into specific ranges.
Exclude: If Fail credits are 80 or more.
Graphical Histogram: After entering data, a histogram of the results will be displayed.

Data Saving: The progression data will be saved to a text file named progression_data.txt.

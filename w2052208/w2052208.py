# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID:w2052208
# Date:14/12/2023

from graphics import *

# Define valid credit values
credit_values = [0, 20, 40, 60, 80, 100, 120]
# Function to get user inputs with validation 
def get_inputs(prompt,credit_values):
    while True:
        try:
            credits = int(input(prompt))
            if credits not in credit_values:
                print("Out of range")  #Display Out of range if credit values not in valid range
                continue
            return credits
        except ValueError:
            print("Integer required.") #Display intiger required if value not in type intiger




# Function to create a histogram
def create_histogram(progress_count, trailer_count, retriever_count, exclude_count):
    # Create a graphics window   
    win = GraphWin("Histogram", 620, 550)
    # Title of histogram    
    label = Text(Point(100, 20), "Histogram Results")
    label.setStyle("bold")
    label.setTextColor(color_rgb(25, 25, 25))
    label.draw(win)

    #Draw horizontal axis
    aLine = Line(Point(45, 450), Point(575, 450))
    aLine.draw(win)

    #Scale factor for limit bar height
    max_count = max(progress_count, trailer_count, retriever_count, exclude_count)
    scale_factor = 400 / max_count
    
    #Draw bar for progress count   
    box1 = Rectangle(Point(65, 450), Point(175, 450 - (progress_count * scale_factor)))
    box1.setFill(color_rgb(149, 239, 122))  
    box1.draw(win)

    #Display name of the bar 
    text= Text(Point(120, 470), "Progress")
    text.setStyle("bold") 
    text.setTextColor(color_rgb(117, 117, 117))
    text.draw(win)

    #Display progression count
    count1 = Text(Point(120, 440 - (progress_count * scale_factor)), progress_count)
    count1.setTextColor("black")
    count1.draw(win)


    #Draw bar for trailer count    
    box2 = Rectangle(Point(185, 450), Point(305, 450 - (trailer_count * scale_factor)))
    box2.setFill(color_rgb(83, 177, 14))
    box2.draw(win)

    #Display name of the bar
    text= Text(Point(240, 470), "Trailer")  
    text.setTextColor(color_rgb(117, 117, 117))
    text.setStyle("bold") 
    text.draw(win)

    #Display trailer count
    count2= Text(Point(240, 440 - (trailer_count * scale_factor)), trailer_count)
    count2.setTextColor("black")
    count2.draw(win)
    

    #Draw bar for retriever count   
    box3 = Rectangle(Point(315, 450), Point(425, 450 - (retriever_count * scale_factor)))
    box3.setFill(color_rgb(101, 134, 23))
    box3.draw(win)

    #Display name of the bar
    text = Text(Point(370, 470), "Retriever")
    text.setStyle("bold")    
    text.setTextColor(color_rgb(117, 117, 117))
    text.draw(win)

    #Display retriever count
    count3 = Text(Point(370, 440 - (retriever_count * scale_factor)), retriever_count)
    count3.setTextColor("black")
    count3.draw(win)


    #Draw bar for excluded count
    box4 = Rectangle(Point(435, 450), Point(545, 450 - (exclude_count * scale_factor)))
    box4.setFill(color_rgb(255, 147, 182))
    box4.draw(win)

    #Display name of the bar
    text = Text(Point(490, 470), "Excluded")
    text.setStyle("bold")    
    text.setTextColor(color_rgb(117, 117, 117))
    text.draw(win)

    #Display exclude count
    count4 = Text(Point(490, 440 - (exclude_count * scale_factor)), exclude_count)
    count4.setTextColor("black")
    count4.draw(win)

    #Display total outcomes
    total_count = progress_count + trailer_count + retriever_count + exclude_count
    total_print = str(total_count) + " " + "outcomes in total"
    total = Text(Point(150, 510),total_print)
    total.setStyle("bold")
    total.setTextColor(color_rgb(117, 117, 117))
    total.draw(win)
    #Wait for click to close the histogram window
    win.getMouse()
    win.close()


#Main programme
def main():
    progress_count = 0
    trailer_count = 0
    retriever_count = 0
    exclude_count = 0

    progression_data = []
    
    while True:
        pass_credits = get_inputs("Enter Pass credits: ", credit_values)
        defer_credits = get_inputs("Enter Defer credits: ", credit_values)
        fail_credits = get_inputs("Enter Fail credits: ", credit_values)


        # Check total credits are equal to 120
        total_credits = pass_credits + defer_credits + fail_credits
        if total_credits != 120:
            print("Total incorrect")
            continue
        
        
        # Check the progression outcome
        outcome = ""
        if pass_credits == 120:
            outcome = "Progress"
            progress_count = progress_count + 1
        elif pass_credits == 100 and defer_credits in {0, 20} and fail_credits in {0, 20}:
            outcome = "Progress (module trailer)"
            trailer_count = trailer_count + 1
        elif pass_credits in {0, 20, 40, 60, 80} and defer_credits in {0, 20, 40, 60, 80, 100, 120} and fail_credits in {0, 20, 40, 60}:
            outcome = "Module retriever"
            retriever_count = retriever_count + 1
        elif fail_credits in {80, 100, 120}:
            outcome = "Exclude"
            exclude_count = exclude_count + 1
        else:
            print("Invalid input")
            continue

        #print the outcome
        print(outcome)
        
        progression_data.append((outcome, pass_credits, defer_credits, fail_credits))

        #Ask user for next process 
        while True:
            next_process = input("Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view results: ").lower()
            if next_process not in {"y", "q"}:
                print("Invalid input")
            else:
                break
        if next_process == "q":
            break
        
    # Create histogram 
    create_histogram(progress_count, trailer_count, retriever_count, exclude_count)

    # Print progression data to a list 
    print("\nPart 2:")
    for data in progression_data:
        print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")
        
    # Save progression data to a file
    save_to_file(progression_data, "progression_data.txt")
    print("\nPart 3:")
    for data in progression_data:
        print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")

# Function to save data to a file        
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for entry in data:
            file.write(f"{entry[0]} - {entry[1]}, {entry[2]}, {entry[3]}\n")    


if __name__ == "__main__":
    main()

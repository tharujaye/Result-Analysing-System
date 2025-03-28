from graphics import *

# initializing variables
pass_credits = 0
defer_credits = 0
fail_credits = 0

def credit_validation(inputs_type):
    while True:
        try:
            input_value = int(input(f"Please enter your credits at {inputs_type} :"))
            if input_value % 20 == 0 and input_value <=120:
                return input_value
            else:
                print("Out of range")

        except ValueError:
            print("Integer required")
            continue
        except Exception:
            print("An unexpected error occurred:")
              
credit_list = []
output_list = []

c1 = 0
c2 = 0
c3 = 0
c4 = 0

def main(credit_list, output_list, c1, c2, c3, c4):
    while True:
        pass_credits = credit_validation("Pass  ")
        defer_credits = credit_validation("Defer ")
        fail_credits = credit_validation("Fail  ")

        total_inputs = [pass_credits, defer_credits, fail_credits]

        if sum(total_inputs) != 120:
            print("Total incorrect\n")
            continue
        else:
            credit_list.append(total_inputs)

        if total_inputs == [120, 0, 0]:
            output = "\nProgress"
            output_list.append(output)
            print(f"{output}\n")
            c1 += 1
            break
        elif total_inputs == [100, 20, 0] or total_inputs == [100, 0, 20] or total_inputs == [100, 0, 20]:
            output = "\nProgress (module trailer)"
            output_list.append(output)
            print(f"{output}\n")
            c2 += 1
            break
        elif (total_inputs == [80, 40, 0] or total_inputs == [80, 20, 20] or total_inputs == [80, 0, 40] or total_inputs == [60, 60, 0] or total_inputs == [60, 40, 20] or total_inputs == [60, 20, 40] or 
           total_inputs == [60, 0, 60] or total_inputs == [40, 80, 0] or total_inputs == [40, 60, 20] or total_inputs == [40, 40, 40] or total_inputs == [40, 20, 60] or total_inputs == [20, 100, 0] or 
           total_inputs == [20, 80, 20] or total_inputs == [20, 60, 40] or total_inputs == [20, 40, 60] or total_inputs == [60, 0, 60] or total_inputs == [0, 120, 0] or total_inputs == [0, 100, 20] or 
           total_inputs == [0, 80, 40] or total_inputs == [0, 60, 60] or total_inputs == [60, 0, 60]):
           output = "\nDo not progress – module retriever"
           output_list.append(output)
           print(f"{output}\n")
           c3 += 1
           break
        elif (total_inputs == [40, 0, 80] or total_inputs == [20, 20, 80] or total_inputs == [20, 0, 100] or total_inputs == [0, 40, 80] or total_inputs == [80, 40, 0] or total_inputs == [0, 20, 100] or 
           total_inputs == [0, 0, 120]):
           output = "\nExclude"
           output_list.append(output)
           print(f"{output}\n")
           c4 += 1
           break
        else:
           print("\nTotal incorrect\n")
           continue

    return total_inputs, output_list, c1, c2, c3, c4

def histogram_display(c1, c2, c3, c4):
    win = GraphWin("Histogram", 800, 600)
    win.setBackground("white")

    #printing histogram results
    message1 = Text(Point(150, 50), "Histogram Results")
    message1.setStyle("bold")
    message1.setSize(20)
    message1.draw(win)

    #drawing a line
    aLine = Line(Point(80, 500), Point(700, 500))
    aLine.draw(win)

    #draw bars for each output_list
    progress_bar = Rectangle(Point(100, 500 - 20 * c1), Point(180, 500))
    progress_bar.setFill("#97FB97")
    progress_bar.draw(win)

    trailing_bar = Rectangle(Point(250, 500 - 20 * c2), Point(330, 500))
    trailing_bar.setFill("#96C783")
    trailing_bar.draw(win)

    module_retriever_bar = Rectangle(Point(400, 500 - 20 * c3), Point(480, 500))
    module_retriever_bar.setFill("#A2BD6E")
    module_retriever_bar.draw(win)

    exclude_bar = Rectangle(Point(550, 500 - 20 * c4), Point(630, 500))
    exclude_bar.setFill("#D8B5B4")
    exclude_bar.draw(win)

    #naming the bars
    Text(Point(140, 525), f"Progress").draw(win)
    Text(Point(290, 525), f"Trailer").draw(win)
    Text(Point(440, 525), f"Retriever").draw(win)
    Text(Point(590, 525), f"Excluded").draw(win)

    #displaying the total number of students in each output_list
    Text(Point(140, 490 - 20 * c1), f"{c1}").draw(win)
    Text(Point(290, 490 - 20 * c2), f"{c2}").draw(win)
    Text(Point(440, 490 - 20 * c3), f"{c3}").draw(win)
    Text(Point(590, 490 - 20 * c4), f"{c4}").draw(win)

    #display the total number of students
    total_students = c1 + c2 + c3 + c4
    Text(Point(170, 570), f"{total_students} Outcome(s) in total.").draw(win)

while True:
    if credit_list == []:
        credit_list,output_list,c1,c2,c3,c4 = main(credit_list,output_list,c1,c2,c3,c4)
    else:
        print("Would you like to enter another set of data?")
        replay = input("\tEnter 'y' for yes or 'q' to quit and view results: ")
        if replay == 'y':
            credit_list,output_list,c1,c2,c3,c4 = main(credit_list,output_list,c1,c2,c3,c4)
        else:
            histogram_display(c1,c2,c3,c4)

            print("\nPart 2:")
            for x in range(0,len(credit_list)):    
                print(f"{output_list[x]} - {str(credit_list[x]).replace('[','').replace(']','')}")





























































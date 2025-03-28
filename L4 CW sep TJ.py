#importing elements
import graphics

#initializing variables
marks=0

pass_credits=0
defer_credits=0
fail_credits=0
    
total_inputs = pass_credits + defer_credits + fail_credits
valid_credit_values = {0, 20, 40, 60, 80, 100, 120} 

#input_credits=[pass_credits,defer_credits,fail_credits]

def credit_validation(inputs_type):  
    while True:
        try:   
            inputs_type = int(input(f"\nPlease enter your credits at {inputs_type} :"))
        
        except ValueError :
            print("Integer required")
            continue
        except Exception :
            print("An unexpected error occurred:")
       
        if int(inputs_type) > 120 or int(inputs_type) < 0:
            print("Out of range")
            continue
        else:
            break
        
    return inputs_type

credit_list=[]
output_list=[]

c1 = 0
c2 = 0
c3 = 0
c4 = 0

def main(credit_list,output_list,c1,c2,c3,c4):
    while True:
        pass_credits=credit_validation("Pass: ")
        defer_credits=credit_validation("Defer: ")
        fail_credits=credit_validation("Fail: ")

        total_inputs = [pass_credits,defer_credits,fail_credits]

        if total_inputs[0] + total_inputs[1] + total_inputs[2] != 120:
            print("Total incorrect\n")            
            continue

        else:
            credit_list.append(total_inputs)
    
        if total_inputs == [120, 0, 0]:
            output = "Progress"
            output_list.append(output)
            print(f"{output}\n")
            c1 += 1
            break
        elif total_inputs == [100, 20, 0] or total_inputs == [100, 0, 20] or total_inputs == [100, 0, 20]:
            output = "Progress (module trailer)"
            output_list.append(output)
            print(f"{output}\n")
            c2 += 1
            break
        elif (total_inputs == [80, 40, 0] or total_inputs == [80, 20, 20] or total_inputs == [80, 0, 40] or total_inputs == [60, 60, 0] or total_inputs == [60, 40, 20] or total_inputs == [60, 20, 40] or 
            total_inputs == [60, 0, 60] or total_inputs == [40, 80, 0] or total_inputs == [40, 60, 20] or total_inputs == [40, 40, 40] or total_inputs == [40, 20, 60] or total_inputs == [20, 100, 0] or 
            total_inputs == [20, 80, 20] or total_inputs == [20, 60, 40] or total_inputs == [20, 40, 60] or total_inputs == [60, 0, 60] or total_inputs == [0, 120, 0] or total_inputs == [0, 100, 20] or 
            total_inputs == [0, 80, 40] or total_inputs == [0, 60, 60] or total_inputs == [60, 0, 60]):
            output = "Do not progress – module retriever"
            output_list.append(output)
            print(f"{output}\n")
            c3 += 1
            break
        elif (total_inputs == [40, 0, 80] or total_inputs == [20, 20, 80] or total_inputs == [20, 0, 100] or total_inputs == [0, 40, 80] or total_inputs == [80, 40, 0] or total_inputs == [0, 20, 100] or 
            total_inputs == [0, 0, 120]):
            output = "Exclude"
            output_list.append(output)
            print(f"{output}\n")
            c4 += 1
            break
        else:
            print("Totally incorrect\n")
            continue

    return total_inputs,output_list,c1,c2,c3,c4

while True:
    if credit_list == []:
        credit_list,output_list,c1,c2,c3,c4 = main(credit_list,output_list,c1,c2,c3,c4)
    else:
        replay = input("Enter 'y' for yes or 'q' to quit and view results: ")
        if replay == 'y':
            credit_list,output_list,c1,c2,c3,c4 = main(credit_list,output_list,c1,c2,c3,c4)
        else:
            fo = open("text.txt","w+")
            for x in range(0,len(credit_list)):
                fo.write(f"{output_list[x]} - {str(credit_list[x]).replace('[','').replace(']','')}")
                print(f"{output_list[x]} - {str(credit_list[x]).replace('[','').replace(']','')}")
                fo.close()

            x = graphics.GraphWin("Histogram",660,700)
            topic = graphics.Text(graphics.Point(100,100),"Histogram results")
            topic.draw(x)
            
            rec1 = graphics.Rectangle(graphics.Point(160,600 - c1 * 6),graphics.Point(30,600))
            graphics.Text(graphics.Point(100,590 - c1 * 6),c1).draw(x)
            r1 = graphics.Text(graphics.Point(250,620),"Progress")
            rec1.setFill("#97FB97")
            rec1.draw(x)
            r1.draw(x)

            rec2 = graphics.Rectangle(graphics.Point(320,600 - c2 * 6),graphics.Point(190,600))
            graphics.Text(graphics.Point(250,590 - c2 * 6),c2).draw(x)
            r2 = graphics.Text(graphics.Point(400,620),"Trailer")
            rec2.setFill("#96C783")
            rec2.draw(x)
            r2.draw(x)

            rec3 = graphics.Rectangle(graphics.Point(480,600 - c3 * 6),graphics.Point(350,600))
            graphics.Text(graphics.Point(400,590 - c3 * 6),c3).draw(x)
            r3 = graphics.Text(graphics.Point(550,620),"Retriever")
            rec3.setFill("#A2BD6E")
            rec3.draw(x)
            r3.draw(x)

            rec4 = graphics.Rectangle(graphics.Point(630,600 - c4 * 6),graphics.Point(500,600))
            graphics.Text(graphics.Point(550,590 - c4 * 6),c4).draw(x)
            r4 = graphics.Text(graphics.Point(100,620),"Excluded")
            rec4.setFill("#D8B5B4")
            rec4.draw(x)
            r4.draw(x)

            graphics.Text(graphics.Point(100,650),f"{c1+c2+c3+c4} Outcomes in total").draw(x)
            break



# def validate_credits(pass_credits, defer_credits, fail_credits):
#     total_credits = pass_credits + defer_credits + fail_credits

#     valid_credit_values = {0, 20, 40, 60, 80, 100, 120}

#     if not all(isinstance(credit, int) for credit in [pass_credits, defer_credits, fail_credits]):
#         raise ValueError("Integer required")

#     if total_credits != 120:
#         raise ValueError("Total incorrect")

#     if total_credits not in valid_credit_values:
#         raise ValueError("Out of range")


# # Example usage:
# try:
#     pass_credits = int(input("Enter pass credits: "))
#     defer_credits = int(input("Enter defer credits: "))
#     fail_credits = int(input("Enter fail credits: "))

#     validate_credits(pass_credits, defer_credits, fail_credits)

#     print("Credits validation successful.")

# except ValueError as ve:
#     print(f"Error: {ve}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")

 # except ValueError:
            #     print("Integer required")
            # except (pass_credits or defer_credits or fail_credits)>120:
            #     print("Out of range")
            # except (pass_credits or defer_credits or fail_credits)>121 and (pass_credits and defer_credits and fail_credits) %20==0:
            #     print("Total incorrect")
            # 
#except ValueError:
    #print("Integer required")

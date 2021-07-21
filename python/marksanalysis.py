#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,18,20,21)

def find_more_than_average():
    global list_of_marks
    list_of_more_than_avg=[]
    avg=sum(list_of_marks)/len(list_of_marks)
    for mark in list_of_marks:
         if mark >avg:
             list_of_more_than_avg.append(mark) 
    return len(list_of_more_than_avg)/len(list_of_marks)*100
    #Remove pass and write your logic here

def sort_marks():
    return sorted(list_of_marks)
    #Remove pass and write your logic here

def generate_frequency():
    return list_of_marks.count(int(input('which marks frequency do you like to know? ')))
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
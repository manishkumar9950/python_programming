#Function-Based Question
#1 Sum of list
def list_sum(numbers):
    s,l=0,len(numbers)
    while l>0:
        s=s+numbers[l-1]
        l-=1
    return s

a=list_sum([2,4,6])
print(a)

#2 Even or Odd Counter
def count_even_odd(numbers):
    e,d=0,0
    for i in numbers:
        if i%2==0:
            e+=1
        else:
            d+=1
    return(e,d)
print(count_even_odd([1,2,3,4,5]))

#3 Largest and smallest 
def find_min_max(data):
    min,max=data[0],0
    for i in data:
        if min>i:
            min=i
        if max<i:
            max=i
    return (min,max)
print(find_min_max([7,2,9,4]))

#4 Remove duplicate
def unique_item(items):
    for i in items:
        c=items.count(i)
        while c>1:
            items.remove(i)
            c-=1
    return items
print(unique_item([1,2,2,3,3,3]))

#5 Common Elements
def common_element(set1,set2):
    return (set1 & set2) 
print(common_element({1,2,3},{2,3,4}))

#6 Word frequency
def word_count(sentence):
    l=sentence.split()
    d={}
    for i in l:
        c=l.count(i)
        d[i]=c
    return d
print(word_count("to be or not to be"))

#7 Student Grade
def get_grade(marks_dict):
    for i in marks_dict.keys():
        if marks_dict[i]>=80:
            marks_dict[i]="A"
        elif marks_dict[i]>=60:
            marks_dict[i]="B"
        elif marks_dict[i]>=40:
            marks_dict[i]="C"
        else:
            marks_dict[i]="Fail"
    return marks_dict
print(get_grade({"Ravi":85,"Sita":62,"Amit":38}))

#8 Default Argument
def power(base,exponent=2):
    return base**exponent
print(power(5))

#9 Keyword Arguments
def student_info(name,age,city="Lucknow"):
    return (f"Name:{name}, Age:{age}, City:{city}")
print(student_info("Ravi",19,"Sirohi"))

#10 Combined Challenge
def analyze_scores(students):
    students=dict(students)
    l=0
    for i in students.keys():
        if l<students[i]:
            l=students[i]
            p=i
        if students[i]>=40:
            students[i]="Passed"
        else:
            students[i]="failed"
    students[p]="Topper"
    return students
print(analyze_scores([("Ravi", 85), ("Sita", 62),("Amit", 38)]))
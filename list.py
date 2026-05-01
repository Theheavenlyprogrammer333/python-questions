 
print("Techobytes Technologies, Galaxy Diamond Plaza")

print("list questions hihi")
# Q1 perform basic list operations
# Access the third element of a list
#List Length: Print the total number of items
#Check if the list is empty
print("Q1")
lst=[2,3,4,5,6,7,9]
print(lst[4])
print(len(lst))

if not list:
    print("liste is empty")
else:
    print("list is not empty")

# Q2 Exercise 2. Perform List Manipulation

#Practice Problem: Take a given list and modify it through five specific actions:

#Change Element: Change the second element of a list to 200 and print the updated list.
#Append Element: Add 600 o the end of a list and print the new list.
#Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
#Remove Element (by value): Remove 600 from the list and print the list.
#Remove Element (by index): Remove the element at index 0 from the list print the list.
print("Q2")
lst =[100, 50, 400, 500]
lst[1]=200 #changed element to 200 
lst.append(600)
print(lst) #list prints 600 at last 
lst.insert(2,300)
lst.remove(600)
print(lst) # 600 removed
lst.pop(2)
print(lst)

#3. Sum and Average of All Numbers in a List
print("Q3")
lst=[4,3,2,2,1]
total=0
for i in lst:# total of the lst elements
    total += i 
    
print("total in list : ",total)

avg = total / len(lst)# avg of list elemnts
print("avg in list",avg)
#4. Find Maximum and Minimum from List
print("Q4")
lst=[939,3932,934,452] 
print("max no.",max(lst))# max number in list
print("min no.",min(lst))# min no. in list

#5. Calculate the Product of All Elements
print("Q5")
lst=[4,3,2,2,4]
product=1
for i in lst:
    product *= i 
   
print(product)

#6. Count Even and Odd Numbers 
print("Q6")
lst=[43,23,45,32,123,62,42,64]
count_odd=0 
count_even=0 
for i in lst :
    if i % 2 == 0 :
        count_even += 1
    else:
        count_odd += 1 

print("no. of even no .",count_even)
print("no. of odd no . ",count_odd)
# 7. Reverse a List 
print("Q7")
lst=[1,2,3,4,5]
rev=[]
for i in range(len(lst) -1 , -1, -1 ):
    rev.append(lst[i])

print(rev)

#8. Sort a List of Numbers 
print("Q8")
lst=[53,64,24,25,67,89,45,34]
lst.sort()
print(lst)# sorted list

#Q9 Create a Copy of a List
print("Q9")
lst=[2,3,54,67]
lst_cop=lst.copy()
print(lst_cop)# copy of list

#Q 10. Combine Two Lists
print("Q10")
lista = ["Physics", "Chemistry"]
listb = ["Maths", "Biology","social science"]

# Combine using the + operator
combined = lista + listb

print(f"Combined List: {combined}")

#Q 11. List Slicing: Extract Middle Elements
print("Q11")
lst=[43,23,45,33,22]
print(lst[1:4])
# Q  12. Swap Two Elements at Given Indices
print("Q12")
lst=[3,2,11,32,4,5]
lst[2],lst[5]=lst[5],lst[2]
print(lst) # swapped 

# Q 13. Access Nested Lists (Simple Indexing)
print("Q 13 ")
#.    0.    1.    2. 
lst=[[3,5],[5,6],[9,1]]
print(lst[2][1])# 2 is   [9,1] and 1 is 1 
# Q 14. Check if List Contains a Specific Item 
print("Q14")
lst=['monitor','tablet','phone']
target='tablet'
if target in lst : 
    print("yes target is there ")
else : 
    print("target is not there")

#Q  15. Find the Longest String in a List
print("Q15")
lst=['python','lol','mango']
longest = max(lst,key=len)
print(longest)

# Q 16. Turn Every Item of a List into its Square 
print("Q16")
lst = [2,3,4,5,6,7]
power=[i * i for i in lst]
print(power)

 # Q 17. Count Occurrences of an Item
print("Q17")
lst=[1,2,3,2,2,3,4,]
target=2 # element to count
count= 0 
for i in lst : 
    if i == target:
        count += 1 

print(count)

# Q 18 remove all occurence of a specific item 
print("Q18")
lst=[2,1,2,3,4,5,6]
target = 2 
for i in lst : 
    if i == target:
        lst.remove(target)

print(lst)

# Q19 remove duplicates from a list 
print("Q19")
lst=[2,1,2,3,4,5,5]
print(f"un filtered list : {lst}")
new_lst=[]
for i in lst : 
    if i not in new_lst:
        new_lst.append(i)

print(new_lst)

# Q 21. List Comprehension for Filtering Numbers
#Practice Problem: Given a list of integers, use list comprehension to create a new list that contains only the even numbers from the original list.
print("Q21")
lst = [ 26,3,45,3,22,24,1]
even_lst=[]
for i in lst : 
    if i % 2 == 0 : 
        even_lst.append(i)

print("even lsit is",even_lst) 

#Q 22. Concatenate Two Lists Index-wise
lst = ['py', '', 'awso']
lst2 = ['thon', 'is', 'me']

res = []
for i in range(len(lst)):
    res.append(lst[i] + lst2[i])

print(res)

#Q 23. Iterate Both Lists Simultaneously
print("Q23")
lst1=[1,2,3]
lst2=[10,100,1000]
for i , j in zip(lst1,lst2):
    print(i,j)

# Q24. Add New Item After a Specified Item 
print("Q24")
lst1 = [10, 20, 30, 40, 50]
target = 30
new_val = 35

index = lst1.index(target)

lst1.insert(index + 1, new_val)

print(f"Updated List: {lst1}")

# 25. Replace List’s Item with New Value if Found
#Practice Problem: Find the first occurrence of a specific value in a list and replace it with a new value.
print("Q25")
lst=[1,3,5,46,2,4,45]
replace=200
target=2 
if target in lst:
    index=lst.index(target)
    lst[index] = replace
    print(lst)

# Q 26. Find the Second Largest Number in a List 
print("Q26")
def get_second_largest(nums):
    # Remove duplicates by converting to a set
    unique_nums = list(set(nums))
    
    if len(unique_nums) < 2:
        return None
    
    # Sort the list in descending order
    unique_nums.sort(reverse=True)
    
    # Return the second element
    return unique_nums[1]

# Test the function
numbers = [12, 35, 1, 10, 34, 1, 35]
result = get_second_largest(numbers)
print(f"List: {numbers}")
print(f"Second Largest: {result}")

# Q  27. Find the Most Frequent Element
print("Q27")
def find_mode(arr):
    frequency = {}
    
    # Count occurrences of each element
    for item in arr:
        frequency[item] = frequency.get(item, 0) + 1
    
    # Find the key with the maximum value
    mode = max(frequency, key=frequency.get)
    return mode

# Test the function
data = [1, 3, 3, 2, 1, 1, 4, 3, 3]
result = find_mode(data)
print(f"List: {data}")
print(f"Mode: {result}")

# Q 28. Extract Every Nth Element from a List 
print("Q28")
def extract_nth(lst, n):
    res = []
    for i in range(0, len(lst), n):
        res.append(lst[i])
    return res

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
n_value = 3

result = extract_nth(my_list, n_value)
print(result)
 
# Q 29 check if list is palindrome 
print("Q29")
lst = [1,0,1]
lst_rev=[]
for i in range(len(lst) - 1, -1, -1):   
    lst_rev.append(lst[i])
    
if lst_rev == lst :
    print("the list is palindorome")
else : 
    print("list not palindrome")

# Q 30. Find All Common Elements Between Three Lists 
print("Q30")
def find_common(lst1,lst2,lst3):
    common = set(lst1) & set(lst2) & set(lst3)
    return list(common)


lst1=[2,30,57,1,67,92]
lst2=[1,67,900,300,920]
lst3=[1,67,909023,233,1233,4232]

result=find_common(lst1,lst2,lst3)
print(result)


#Q 31 filter strings by length in a list
print("Q31")
lst=['laptop','mobile','cam','bazooka','granade','guns','lolipop','choclate']

 

filtered = [k for k in lst if len(k) > 6]#any string longer than length of 6 shall be printed


print(filtered)
 

# Q  32 Check if List is Sorted 
print("Q32")
lst = [1, 2, 3, 4, 5]

is_sorted = True 

for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:# if the previous element is bigger
        is_sorted = False
        break

if is_sorted:
    print("List is sorted")
else:
    print("List is not sorted")

# Q 33. List to Dictionary Conversion
def lists_to_dict(keys, values):
    # Zip pairs the elements, dict() converts pairs to key-value entries
    return dict(zip(keys, values))

# Test the function
fields = ["name", "age", "city"]
data = ["Alice", 25, "New York"]
result = lists_to_dict(fields, data)

print(f"Keys: {fields}")
print(f"Values: {data}")
print(f"Resulting Dict: {result}")

#Q 34. Find the Difference Between Two Lists
lst1=[1,2,3,54,65,76]
lst2=[1,2,800,900,700,500]
for i in lst1:
    if i not in lst2:
        print(i)
     


# Q  35. Remove Negative Numbers In-place 
print("Q35")
lst=[-90,-80,54,24,65,-78,-97]

for i in range(len(lst) -1 , -1 , -1):
    if lst[i] < 0 :
        del lst[i]
print(lst)

# Q 36. Extend Nested List by Adding a Sublist
print("Q36")
fru=[['apple', 'banana'], ['cherry', 'date']]
fru[1].append("cranberry")
print(fru)


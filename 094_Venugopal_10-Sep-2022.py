# 1. Implement palindrome using iterator(for loop) and generator mechanism.
print("'''---------------------------Program-1------------------------'''")
def palindrome(str1):
   return str1 == str1[::-1]
ispalin = 'malayalam'
a = palindrome(ispalin)
if a:
    print("The given string is palindrome:", True)
else:
    print("The given string is palindrome:", False)
print()

# 2. Sum of 2 digits into output
# 		n1 = 1234 # int(input("Enter number1 :" ))
# 		n2 = 9999 # int(input("Enter number2 :" ))
# 		Output: 9+1 2+9 3+9 4+9
# 		         10 + 11 + 12 + 13
# 				 46
print("'''------------------------------------Program-2----------------------------------'''")
def smt(n1, n2):
    st1 = str(n1)
    st2 = str(n2)
    lis1 = list(st1)
    lis2 = list(st2)
    n5 = []
    for i in range(len(st1)):
        sum1 = int(lis1[i]) + int(lis2[i])
        n5.append(sum1)
    sumOfTwo = 0
    for j in n5:
        sumOfTwo += j
    return "Sum of Two numbers is ",sumOfTwo
nn1 = 1234
nn2 = 9999
print(smt(nn1, nn2))
print()

# 3. st = "ab@#cd!ef"
#    Reverse string considering only alphabets. Symobls should not be reversed
#    # Output: fe@#dc!ba
print("'''--------------------------------Program-3----------------------------------'''")
def reverseString(rs):
    '''Reverse string considering only alphabets. Symobls should not be reversed'''
    rev = -1
    for i in range(len(rs)-1, int(len(rs)/2), -1):
        if rs[i].isalpha():
            rev1 = rs[i]
            while True:
                rev += 1
                if rs[rev].isalpha():
                    rs[i] = rs[rev]
                    rs[rev] = rev1
                    break
    return rs
st = "ab@#cd!ef"
print("Input of String :", st)
st = reverseString(list(st))
print("Output of String :","".join(st))
print()

# 4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
# findout elements duplicate count output in  dict format
print("'''------------------------------Program-4----------------------------------'''")
def sumList(l1):
    dic = {}
    for i in l1:
        if i in l1:
            dic[i] = dic.get(i, 0)+1
            pass
        else:
            dic[i] = dic.count(i)
    return dic
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
l2 = sumList(some_list)
print("The given list is :", some_list)
print("The Output of Dictionary is :",l2)
print()

# 5. # t1 = (1, 2, 3, "a", "c")
#    # t2 = ("b", "d", 9, 8, 7)
#    # Output: (10,10,10,"ab","cd")
print("'''------------------------------------Problem-5--------------------------------'''")
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
t3 = []
print("---------------In-Progress---------------")
print()


# 6  #Write a Python program to remove leading zeros from an IP address.
# 			  inp = "216.08.094.196"
# 			# o/p =  216.8.94.196
print("'''-----------------------------------Problem-6--------------------------------'''")

def removeZero(in1):
    rz = ''
    for i in in1:
        if i == '0':
            continue
        rz += i
    return "After Removing zeros",rz
inp = "216.08.094.196"
print(removeZero(inp))
print()

# 7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
#    #output= [1,2,3,4,5,6,7,8,9,10]
print("'''-------------------------------Program-7---------------------------------'''")
def sorted(sort11):
    rr1=[]
    for i in sort11:
        if type(i)==list:
            rr1.extend(i)
        else:
            rr1.append(i)
    rr2=[]
    for i in rr1:
        if type(i)==list:
            rr2.extend(i)
        else:
            rr2.append(i)
    return "Final Output is :", rr2
laa = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
print(sorted(laa))
print()

# 8. Load sample content in text file.
#    Read data and find
#   1. No of lines in file
# 	2. No of words in each line
# 	3. No of chars in each line
# 	4. No of vowels and consonants
# 	5. No of special chars linewise and total
print("'''------------------------------------Program-8----------------------------------'''")
print("--------------------In-Progress--------------------")


















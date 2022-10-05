def divide_string(string):
    off=0
    capitalize= 1
    for i in range(len(string)):
        if string[i] in comma or string[i] in punctuation or i==len(string):
            if capitalize==1:
                array_string.append(string[off:i+1].strip().capitalize())
                capitalize=0
            else:
                array_string.append(string[off:i+1].strip())
            off=i+1
            if string[i] in punctuation:
                capitalize=1   
    return array_string

def count_w_m_p(string):
# Analysis of string
    c_word=0
    c_marks=0
    phrases=0
    dic_word = { }# define a list of dictionaries {word:'a' , cont: 3}
    for i in range(len(string)):
        # count punctuation marks
        # number of phrases is same as marks
        if string[i] in comma or string[i] in punctuation:
            c_marks+=1
            phrases+=1
        # count words not punctuation marks
        elif string[i]!=' ':
            c_word+=1
            # count character max and min
            if string[i].lower() in dic_word:
                dic_word[string[i]]+=1
            else:
                dic_word[string[i]]=1
    return c_word,c_marks,phrases,dic_word

def max_min_ele(dictionaries):
    max_char=0
    min_char=999
    min_ele=""
    max_ele=""
    for i , k in dictionaries.items():
        if k>max_char:
            max_char=k
            max_ele=i
        if k<min_char:
            min_char=k
            min_ele=i
    return max_char,max_ele,min_char,min_ele

def print_data(c_word,c_marks,phrases,max_char,max_ele,min_char,min_ele):
    print("\r number of word : ",c_word )
    print("\r number of marks : ",c_marks)
    print("\r number of phrases : ",phrases )
    print("\r most frequent character is '{}' with :  {} elements".format(max_ele,max_char))
    print("\r least frequent character is' {}' with  : {} elements ".format(min_ele,min_char))


print(" -----  Exercise  ----")
comma = [","]
punctuation = ["?",".","!"]
print("hi everyone . in this exercise we try to manipulate the string, we use a different command. like split or replace! are you read?")
string='1'
while(string!='0'):
    print(" \n ------------------------   \n ")
    if(string=='1'):
        string = "hi everyone . in this exercise we try to manipulate the string, and we use a different command. like split or replace! are you read?"
        print(" this is a EXAMPLE \n")
        print("string = ",string)
    else:
        string=input("insert a long string or 0 to end: ")

    if(string!='0'):
        array_string = []
        print(" this is the punctuation that the program can scan : '. , !' ")
        array_string=divide_string(string)
        print("this is a list of substring:" ,array_string)
        c_word,c_marks,phrases,dictionaries=count_w_m_p(string)
        max_char,max_ele,min_char,min_ele= max_min_ele(dictionaries)
        print_data(c_word,c_marks,phrases,max_char,max_ele,min_char,min_ele)

print("Bye Bye")


#Possible implementations
'''
1) insert more phrases by keyboard
2) output menage with table
3) less code lines to find min and max 
4) manage punctuation by keyboard 

'''


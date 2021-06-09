import re   # the module of the regular expression

"""
                                    :: SOME IMPORTANT SHORTCUTS TO USE ::
                                      
\d ====> Any numeric digit from 0 to 9.
\D ====> Any character that is not a numeric digit from 0 to 9.
\w ====> Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.).
\W ====> Any character that is not a letter, numeric digit, or the underscore character.
\s ====> Any space, tab, or newline character. (Think of this as matching “space” characters.).
\S ====> Any character that is not a space, tab, or newline.


                                    :: SOME OTHER IMPORTANT SIGNS ::
                                    
() "parentheses" ==> to separate the regex to groups 
                                        << in example 0 and 1 >>
                                        
| "pipe" ==> to detect the match of it exist in the first regex, or the second regex (like OR gate)
                                        << in example 2 and 3 >>
                                    
? =======> to detect if the regex is exist or not
                                        << in example 4 >>
                                
* "asterisk" =======> to match the regex using (zero or more) strategy, mean if exist print it, if not no problem.
                                        << in example 5 >>
                                        
+ "add" ====> like 'star', but it different that it use (one or more) strategy, it have to find the match, or more.
                                        << in example 6 >>
                                        
{'number of repeated times '} ==> used to detect the match that exist number of repeated times as you want
                                        << in example 7 >>
                                        
['regex'] ===> to choose a range or some only characters and so on.
                                        << in example 9, 10 and 11 >>

[^] =====> mean to search for the matched in the string which not match the regex (negative class character).
                                        << in example 11 >>
                                        
^   =====> put in the beginning of regex, mean to match only the string that matched in the begging of the string only.
                                        << in example 12 >>
                                            
$   =====> put in the end of regex, mean to indicate the match only in the end of the string.
                                        << in example 12 >>
                                        
^\d$ ====> will check if all the string is digits, you can change \d to what ever u want baby.
                                        << in example 12 >>
                                        
."dot" ==> called wild card character, and used to match any character except the new line, and match only one character
                                        << in example 13 >>
                                        
.* ==> will match any thing in the message (of course without the new lines) ( match in greedy way).
                                        << in example 14 >>
                                        
.*? ==> like the above, but it it match in nonGreedy way.
                                        << in example 14 >> 
                                        
'.*', re.DOTALL ==> used to make this regex also match the new lines.
                                        << in example 15 >>
"""

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

num = phoneNumRegex.search("my phone num is 415-555-4242.")
print(" ==================== 0 ==================== \n")
print(num.group())
print(num.group(0))
print(num.group(1))
print(num.group(2))  # according to the parentheses you put in the pattern (phoneNumRegex)
print(num.group(1, 3), end="\n\n ==================== 1 ==================== \n")

groupOne, groupTwo, groupThree = num.groups()  # groups() not group()
print(groupOne)
print(groupTwo)
print(groupThree, end="\n\n ==================== 2 ==================== \n")

heroRegex = re.compile(r'Batman|Tina Fey')  # the pipe to use more than one pattern
mo1 = heroRegex.search("Tina Fey and Batman")
print(mo1.group())
mo2 = heroRegex.search('Batman and Tina Fey.')
print(mo2.group())
mo3 = heroRegex.findall('Batman and Tina Fey.')  # findall() will find all the patterns
# we can use findall() also with parentheses (groups).
print(mo3, end="\n\n ==================== 3 ==================== \n")  # no group() method to use.

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')  # another usage [pipe with groups]x.
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1), end="\n\n ==================== 4 ==================== \n")

batRegex = re.compile(r'bat(wo)?man')  # to check whether or not the word "wo" is there, using "?".
mo = batRegex.search("hello batwoman")
print(mo.group())
mo = batRegex.search("hello batman")
print(mo.group(), end="\n\n ==================== 5 ==================== \n")

batRegex = re.compile(r'bat(wo)*man')  # using "*" => "asterisk" to check if the word 'wo' is even written many times.
# and mean also (( match zero or more )) ==> mean match 'wo' if exist, and if not no problem ignore it. like "?"
mo = batRegex.search("hello batman")
print(mo.group())
mo = batRegex.search("hello batman")
print(mo.group())
mo = batRegex.search("hello batwowowowowowowoman")
print(mo.group(), end="\n\n ==================== 6 ==================== \n")

batRegex = re.compile(r'bat(wo)+man')  # the difference between this and *, that + mean ((match one or more)).
mo = batRegex.search("hello batwoman")
print(mo.group())
mo = batRegex.search("hello batwowowowowoman")
print(mo.group(), end="\n\n ==================== 7 ==================== \n")

regex = re.compile(r'(Ha){3}')  # used to repeat the word more than one if u want
mo = regex.search("Hello there, HaHaHa boys")
print(mo.group())

regex = re.compile(r'(Ha){3,5}')  # here it can display it when it's three or five.
mo = regex.search("Hello there, HaHaHaHaHa boys")
print(mo.group(), end="\n\n ==================== 8 ==================== \n")

xmasRegex = re.compile(r'\d+\s\w+')
# this is the format of the next text, /d+ ==> for any digit number "one or more",
# then (\s\w+) ==> mean that any letter like space and so on, and \w for any word,, all those are "one or more"
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, '
                       '3 hens, 2 doves, 1 partridge')
print(mo, end="\n\n ==================== 9 ==================== \n")

# using the [] ::

# if u want a range only of digits, class [0-5] will match only the numbers 0 to 5; this is much shorter
# than typing (0|1|2|3|4|5).
# for example
xmasRegex = re.compile(r'[0-5]+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, '
                       '3 hens, 2 doves, 1 partridge')
print(mo, end="\n\n ==================== 10 ==================== \n")

rangeRegex = re.compile(r'[abcdABCD]')
message = rangeRegex.findall("Hello There boys , My Name is Omar Ahmed Mohamed")
print(message)

# or also using this
rangeRegex = re.compile(r'[a-zA-Z0-9]')
message = rangeRegex.findall("Hello There boys , My Name is Omar Ahmed Mohamed")
print(message, end="\n\n ==================== 11 ==================== \n")


# to opposite the regex with []
rangeRegex = re.compile(r'[^0-5]+\s\w+')  # called negative class character
mo = rangeRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, '
                        '3 hens, 2 doves, 1 partridge')
print(mo, end="\n\n ==================== 12 ==================== \n")


# usage of ^ and $
# ^
beginRegex = re.compile(r'^Hello')
message = beginRegex.findall("Hello there boys")
print(message)

message = beginRegex.search("i have said hello before")  # when changing the position of regex, it wont work
print(message is None)  # because it has no value , it will print True.


# $
endRegex = re.compile(r'\d+$')
message = endRegex.findall("Hello,it was 18 and now 19")
print(message)
# it will print only the last digit number ( i put \d+ not \d to print 19 not only 9.

# another usage
wholeRegex = re.compile(r'^\d+$')  # if u used the regex without "+", it will just check if the message is only 1 digit
message = wholeRegex.search("124848")
print(message.group())
message = wholeRegex.search("158548sdsd158585")  # i put a string in the middle of the message
print(message is None, end="\n\n ==================== 13 ==================== \n")
# it will print True because the regex check if all the message contains only digits.


# the WildCard character (.) [dot]
DotRegex = re.compile(r'.at')  # if u put it just only "." ==> it will print all the characters alone in the screen.
message = DotRegex.findall("The cat in the hat sat on the flat mat.")
print(message, end="\n\n ==================== 14 ==================== \n")


# usage of "dot . " with "star * "
allRegex = re.compile(r'first name: (.*) last name: (.*)')
message = allRegex.search("first name: Omar last name: Shehata")
print(message.group())
print(message.group(1))
print(message.group(2))

# all the above is to match in a greedy way, the dot and star will search for any text as much as it possible
# to avoid this use the nonGreedy way, using ? character, like this :
nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# if we use it without the ? :
nonGreedyRegex = re.compile(r'<.*>')
mo = nonGreedyRegex.search('<To serve man> for dinner.>')
# Both regexes roughly translate to “Match an opening angle bracket,
# followed by anything, followed by a closing angle bracket.”
# ” But the string '<To serve man> for dinner.>' has two possible matches for the closing angle
# bracket. In the nonGreedy version of the regex, Python matches the shortest
# possible string: '<To serve man>'. In the greedy version, Python matches the
# longest possible string: '<To serve man> for dinner.>'.
# I have copied it form the book, page 185.
print(mo.group(), end="\n\n ==================== 15 ==================== \n")

# to make the regex match the new lines too :
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(mo.group())

newlineRegex = re.compile('.*', re.DOTALL)  # here the new line will match also.
mo2 = newlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.')
print(mo2.group())


"""
##  before using the regular expression >>>

def isaPhoneNum(Number):
    if len(Number) != 12:
        return False
    for i in range(0, 3):
        if not Number[i].isdecimal():
            return False
    if Number[3] != "-":
        return False

    for i in range(4, 7):
        if not Number[i].isdecimal():
            return False
    if Number[7] != "-":
        return False

    for i in range(8, 12):
        if not Number[i].isdecimal():
            return False

    return True


message = "hello there boys , this is my phone number 415-585-4242 , 415-555-8842 bye"
check = False
for i in range(len(message)):
    package = message[i:i+12]
    if isaPhoneNum(package):
        print(f"phone number found, and here it is : {package} ")
        print("done")
        check = True

if not check:
    print("not found")

 ## another way ::

while 1:
    phone = input("enter the phone number : ")
    print(isaPhoneNum(phone))

    check = input("run again ? \n")
    if check == "y" or check == "yes":
        continue
    else:
        break
"""

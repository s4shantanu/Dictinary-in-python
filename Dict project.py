print("hello Shantanu")
myDict = {
    "Admire" : "Huge Respect",
    "Assure" : "Confidently",
    "Bride" : "Wommen Wedding Form",
    "Fought" : "Past",
    "Xerox" : "Photocopy"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi Word\n")
print("The meaning of your word is:", myDict.get(a))
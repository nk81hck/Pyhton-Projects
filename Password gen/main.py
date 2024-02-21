import string
import random
# s0 = string.ascii_letters   # The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.
# print(s0)
s1 = string.ascii_uppercase
# print(s1)
s2 = string.ascii_lowercase
# print(s2)
s3 = string.digits
# print(s3)
s4 = string.punctuation
# print(s4)
# Todo1: Handle Gibberish(unintelligible or meaningless speech or writing; nonsense.)
while (True):
    try:
        plen = int(input("Enter the password length\n"))  # plen is describing a length of user password!
        break
    except ValueError:
        print("that's not a valid number, so please try again:")
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
# print(s)
random.shuffle(s)   # it use for shuffling  the characters and  make a difficult password.
# print(s)
print("your password is :\n")
print("".join(s[0:plen]))   # The join() method takes all items in an iterable and joins them into one string. A string must be specified as the separator.
#  Alternative is :
#  Firstly you comment out the random.shuffle(s) and print("".join(s[0:plen])), and then = print("".join(random.sample(s,plen))).....









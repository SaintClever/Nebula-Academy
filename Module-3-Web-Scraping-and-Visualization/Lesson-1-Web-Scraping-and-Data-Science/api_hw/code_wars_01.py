# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive. The string can contain any char.

def xo(s): return sum([1 if i == 'x' else -1 if i == 'o' else 0 for i in s.lower()]) == 0

def xo(s):
    # x, o = 0, 0
    # 
    # for i in s.lower():
    #     if i == 'x':
    #         x += 1
    #     elif i == 'o':
    #         o += 1
    # 
    # return x == o

    return s.lower().count('x') == s.lower().count('o')

print(xo("ooxx")) # => true
print(xo("xooxx")) # => false
print(xo("ooxXm")) # => true
print(xo("zpzpzpp")) # => true // when no 'x' and 'o' is present should return true
print(xo("zzoo")) # => false





def to_jaden_case(string):
    # return ' '.join(word[0].upper() + word[1:].lower() for word in string.split())
    return ' '.join(word.capitalize() for word in string.split())


quote = "How can mirrors be real if our eyes aren't real"
print((to_jaden_case(quote))) # => "How Can Mirrors Be Real If Our Eyes Aren't Real")
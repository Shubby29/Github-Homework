def solve(word):
    wordlist = []
    if word in wordlist:
        if word.isalpha():
            if word in wordlist:
                return False
            wordlist.append(word)
    return True


word = "isogram", "uncopyrightable", "ambidextrously"
print(solve(word))

# class IncorrectInput(Exception):
#     def solve(self):
#         try:
#             wordlist = []
#             if self in wordlist:
#                 if self.isalpha():
#                     if self in wordlist:
#                         return False
#                 wordlist.append(self)
#                 return True
#         except TypeError:
#             raise IncorrectInput
#
#     def isalpha(self):
#         pass
#
#
# self = "isogram", "uncopyrightable", "ambidextrously"
# print(self)

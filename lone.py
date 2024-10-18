# # Input: s = "babad"
# # Output: "bab"
# # Explanation: "aba" is also a valid answer.
# def call(m,s):
#  w=''
#  for i in range(len(s)):
    
#     if i<=m:
#         w+=s[i]
#  return w
# s='baad'
# m=round((len(s)-1)/2)
# s2=s
# for i in range(len(s)):
#     w=call(m,s2)
#     if w[::-1] == w:
#        print('number is plamdrome')
#        break
#     else:
#        s2=s2[1:]
#        m2=call(m,s2)
#        print(m2)

#        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# s="PAYPALISHIRING"
# r=int((len(s)/2)-1)
# r1=" "
# for w in range(len(s)-1):
#       if(w%4==0 or w==0):
#          r1+=s[w]+" "
# r1+="\n"+" "
# for w in range(1,len(s)-1):
#       if w%2!=0:
#          r1+=s[w]+" "
# r1+="\n"+" "
# for w in range(1,len(s)-1):
#       if w%2==0:
#          r1+=s[w]+" "

# print(r1)

# def zigzag_convert(s, num_rows):
#     if num_rows == 1 or num_rows >= len(s):
#         return s

#     rows = [' '] * num_rows
#     current_row = 0
#     going_down = False

#     for char in s:
#         rows[current_row] += char+" "
#         if current_row == 0:
#             going_down = True
#         elif current_row == num_rows - 1:
#             going_down = False
        
#         current_row += 1 if going_down else -1

#     return '\n'.join(rows)

# # Example usage
# s = "PAYPALISHIRING"
# num_rows = 3
# result = zigzag_convert(s, num_rows)
# print(result)


  




        

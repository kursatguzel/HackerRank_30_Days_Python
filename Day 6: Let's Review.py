"""
Objective
Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given a string,
, of length that is indexed from to , print its even-indexed and odd-indexed characters as space-separated strings on a single line (see the Sample below for more detail). 
"""
T = int(input())
for i in range (0 , T):
    S = input()
    print(S[0::2] + " " + S[1::2])

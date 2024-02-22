#!/usr/bin/env python
# Author: N_V_NAIDU
# Date: 22/02/2024
# Level 5 Puzzle by Zden Puzzle Decoder https://twitter.com/Zd3N/status/1060955171591766018

import math

def string_decode(input, length=8):
    input_l = [input[i:i+length] for i in range(0,len(input),length)]
    return ''.join([chr(int(c,base=2)) for c in input_l])

# Ribbon Key

key = "011010"

# Sum of two consecutive following rectangles areas creates one byte of the private key
# short (0) or tall (1)
# narrow (0) or wide (1)

# Read clockwise around the picture frame from inside edge starting from the top left
# once a full loop is made continue on the outer edge counter-clockwise

rectangles = [
	"0010", # Top Inner (left -> right)
	"1011",
	"1001",
	"0101",
	"1010",
	"1110",
	"0001",
	"1100",
	"1001",
	"0001",
	"1110",
	"0011",
	"0100",
	"0101",
	"1000",
	"0110",
	"1110",
	"1110",
	"0001",
	"1011",
	"1101",
	"0011",
	"1110",
	"1110",
	"0000",
	"0001",
	"1000",
	"1010",
	"1011", # Right Inner (top -> bottom)
	"1010",
	"0000",
	"1000",
	"1100",
	"1000",
	"1111",
	"1110",
	"0110",
	"1001",
	"1101",
	"0100",
	"1111",
	"1011",
	"0001",
	"1011",
	"1100",
	"1111",
	"1110",
	"1110",
	"0001",
	"0000",
	"1001",
	"0011",
	"1101", # Bottom Inner (right -> left)
	"0001",
	"0101",
	"0001",
	"1110",
	"1110",
	"1111",
	"0011",
	"0010",
	"0010",
	"1001",
	"0100",
	"1100",
	"1110",
	"0011",
	"1001",
	"1001",
	"1110",
	"1010",
	"1101",
	"0101",
	"1101",
	"1110",
	"1101",
	"1100",
	"1101",
	"0010",
	"1111",
	"1001",
	"1110",
	"1100",
	"1100",
	"0000",
	"0001", # Left Inner (bottom -> top)
	"1101",
	"1110",
	"1111",
	"0101",
	"0001",
	"1111",
	"1001",
	"0001",
	"1110",
	"1110",
	"0000",
	"1011",
	"1100", # Left Outer (top -> bottom)
	"0001",
	"1111",
	"1000",
	"0001",
	"1101",
	"1101",
	"0010",
	"1111", # Bottom Outer (left -> right)
	"0100",
	"0000",
	"0000",
	"1110",
	"0100",
	"1010",
	"1000",
	"0000",
	"1110",
	"1101",
	"1110",
	"1110",
	"1011",
	"0001",
	"0001",
	"1111", # Right Outer (bottom -> top)
	"0110",
	"1010",
	"0010",
	"0010",
	"0010",
	"1110",
	"1011",
	"1100",
	"1111",
	"0101",
	"0000",
	"1111", # Top Outer (right -> left)
	"0010",
	"1110",
	"1101",
	"0010",
	"0010",
	"1001",
	"1110",
	"1111",
	"0101",
	"0000",
	"1101",
	"1110",
	"0111",
	"1010",
	"1011",
	"0101",
	"0001",
]

# Concatenate binary string

data = ""

for x in rectangels:
	data = data + x

# Generate XOR binary string

xor = int(math.ceil(len(data)/6.0)) * key

# print(data)
# print(xor)

# XOR data and xor strings together

results = ""

for i,c in enumerate(data):
	results = results + str(int(c) ^ int(xor[i]))

# print(results)

# Decode result as ascii string

decoded_str = string_decode(results)

print(decoded_str)

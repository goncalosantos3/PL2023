import re

# input = "MOEDA 10c, 30c, 50c, 2e."
# # input = "MOEDA 10c, 30c."
# 
# print(re.match(r'MOEDA\s+((\d+(?:c|e)(?:,|\.)\s*)+)', input).group(1))

input = "T=2536044709"
print(re.match(r'T\s*=\s*(00\d+|\d{9})\s*', input).group(1))

# moedas = "10c, 30c, 50c, 2e."
# print(re.findall(r'(\d+(?:c|e))', moedas))
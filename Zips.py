s1 = {1,2,34,4,5,6,7,5}
s2 = {1,4,5,4,32,5,2,9}
s3 = list(zip(s1,s2))
print(s3, "\n")

# reversed mapping
l1 = [1,2,3,4]
l2 = [3,2,4,3]

for x,y in zip(l1, l2[::-1]):
    print(x,y)

# Lists into Dictionary
stocks = ['Infosys', 'Tcs', 'Reliance', 'Cadbury']
prices = [123,314,124,75]
new_dict = {stocks:prices for stocks, prices in zip(stocks,prices)}
print(new_dict)
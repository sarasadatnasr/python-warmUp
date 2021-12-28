myList = [int(input()), int(input()), int(input()), int(input())]
sum1 = myList[0] + myList[1] + myList[2] + myList[3]
product1 = myList[0] * myList[1] * myList[2] * myList[3]

sum ="{:.6f}".format(sum1)
print("Sum :", sum)

average ="{:.6f}".format(sum1/4)
print("Average :", average)

product = "{:.6f}".format(product1)
print("Product :", product)

maxi = "{:.6f}".format(max(myList))
print("MAX :", maxi)

mini = "{:.6f}".format(min(myList))
print("MIN :", mini)






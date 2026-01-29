# Start Here

'''
message = 'Welcome to PythonReview'
print(type(message))
print(len(message))

print(3*'3')


#boolean
print(len('greg')==4)


a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)  #division returns float number
print(a//b) #floor division (get only int)
print(a**b)
print(a%b)

'''

professors = ['Greg', 'kianoosh', 'Richard','Jose']

print(professors[0])
print(professors[1])
print(professors[2])
print(professors[-1])
print(professors)
professors.append('leo')
print(professors)
professors.extend(['heather','kevin'])
print(professors)

professors.insert(2,'trevor')

professors[3] = 'mark'
print(professors)

#range 9 means 0 through 8
print(professors[3:5])              #accessing professors in i 3 and 5
print(professors[5:])
print(professors[:3])
print(professors[:])                #interesting, creates a copy for manipulations or else error since cannot modify existing list
professors.remove('kianoosh')
print(professors)
print(professors.index('mark') )

x = professors.pop(6)
print(professors)
print(x)

print(len(professors))
print(type(professors))

professors.sort()
print(professors)
professors.sort(reverse=True)
print(professors)

for i in professors:
    print(i.title())

print('FIU')



water_data = {

    "temperature": [78,89,92],
    "ph":[6.5,6.7,6.3],
    "oxygen": [7.2,5.6,3.5],
}

print(water_data["oxygen"])    # smth related to JSON


import pandas as pd

df = pd.DataFrame(water_data)
print(df)


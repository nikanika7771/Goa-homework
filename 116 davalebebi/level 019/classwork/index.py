#sum gvexmareba gavigot jami tuple shi arsebuli ricxvebit
numbers = (2, 3, 6 ,8) 
print(sum(numbers))

numbers1 = (100, 3, 20 ,2)
print(sum(numbers1))

#gvexmareba gaovitanot umciresi ricxvi tupleshi da aseve listshi
numbers2 = (2, 3, 6 ,8)
print(min(numbers2))

numbers3 = (2, 150, 6 ,10)
print(min(numbers3))
# gvexmareba gamovitanot udidesi ricxvi tuplesh da aseve listshi
numbers4 = (2, 3, 6 ,8)
print(max(numbers4))

numbers5 = (60, 30, 100 ,1000)
print(max(numbers5))

#gvexmareba davalagot tupleshi arsebuli ricxvebi tanmimdevrobit
numbers6 = (10, 3, 6 ,8)
print(sorted(numbers6))

numbers7 = (90, 100, 6 ,99)
print(sorted(numbers7))


#2


mixed_tuple = (1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15)

total = 0

for i in mixed_tuple:
    total+= i

    print("jami", total)


    #3


tuple = (1,2,3,4,6,7,8,11,12,13,14)
name = "nika"

tuple = tuple +  (name,)
print(tuple)
# friends = ["Aman", "Bhavya", "Charu", "Dhruv", "Aryan"]
# name=input("enter your friend name")
# found=False
# for y in friends:
#     if name==y:
#         found=True
#         break
#     else:
#         pass
#
# if found==True:
#     print("Your friend is present in the list")
# else:
#     print("Your friend is not present in the list")
num_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
n= len(num_list)
i=0
while i<n:
    temp=num_list[i]
    num_list[i]=num_list[n-1]
    num_list[n-1]=temp
    i=i+1;
    n=n-1;
print(num_list)
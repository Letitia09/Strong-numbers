#lex_auth_01269437118923571233
def factorial(number):
    fact=1
    if number>1:
        while(number>0):
        #remove pass and write your logic to find and return the factorial of given number
            fact=fact*number
            number-=1
    else:
        fact=1
    return fact

def find_strong_numbers(num_list):
     #remove pass and write your logic to find and return the list of strong numbers from the given list
    
    stronglist=[]
    for i in range(len(num_list)):
         t=num_list[i]
         sum=0
         if t==0:
            sum+=factorial(t)
         else:
             while(t!=0):
                r=t%10
                sum+=factorial(r)
                t=t//10
         if sum==num_list[i]:
             stronglist.append(sum)
    return stronglist

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)

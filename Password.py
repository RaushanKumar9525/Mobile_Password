from time import sleep
#Fived or Defined a password key
CorrectPassword="123456789"
# define the Retries Times  only give three times.
tries=3

#Main loop
while True:
 #Defin a Input variable// Take a User input
 UserInput=input("Enter the Password ---> ")
#Check the password when password is correct then print Unclock otherwise print Retrie.
 if UserInput == CorrectPassword:
    print("Unlock !")
    break
 else:
    print("Retrie !")
    # Reduce the tries by 1
    tries=tries-1
    #if tries reduce 0 then start timer for 30 second
    if tries<=0:
      for i in range(30,0,-1):
        print(i)
        sleep(1)
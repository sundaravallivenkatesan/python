j=input()
v=['a','e','i','o','u','A','E','I','O','U']
c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','K','J','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
if j in v:
    print("Vowels")
elif j in c:
    print("Consonants")
else: 
    print("Invalid")

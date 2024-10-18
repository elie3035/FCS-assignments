
# Author: Elie Boulos
# Assignment 15-09-2024
# Exercice 1

age = int (input("Enter student age"))


if age > 100 or age <=0 :
  print("incorrect student age")  
elif age < 18:
  print("insufficient age")
else:
 country = str (input ("Enter country of residency"))   
 if country != "lebanon":
  print ("foreign country")
 else:
  score = int (input ("Enter hacker rank score")) 
  if score   >= 110:
      print("welcome to FCS")
  else:
      print("insuffisient hacker rank score")
        
 
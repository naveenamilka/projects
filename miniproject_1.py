dictionary={}
while 1:
 print("1.Add a word")
 print("2.search for meaning")
 print("3.display all words")
 print("4.update meaning")
 print("5.delete word")
 print("6.exit")

 choice=int(input("enter choice(1-6):"))
 if choice==1:
  word=input("enter word:")
  meaning=input("enter meaning:")
  dictionary[word]=meaning
  print("word added successfully")
  print(dictionary)
 elif choice==2:
  word=input("enter search word:").lower()
  if word in dictionary:
   print("meaning:",dictionary[word])
  else:
   print("search word doesn't exist in dictionary")
 elif choice==3:
  print(dictionary)
 elif choice==4:
  word=input("enter key:")
  if word in dictionary:
   meaning=input("enter meaning which to be updated:")
   dictionary[word]=meaning
   print(dictionary)
  else:
   print("word not found you can't update the meaning")
 elif choice==5:
  word=input("enter word which to be removed:")
  if word in dictionary:
   dictionary.pop(word)
   print(dictionary)
  else:
   print("you can't delete because the word not existed")
 elif choice==6:
  break
  
print('''
          welcome to
         BAYTARA🐶😸
''')
print("where your animal is safe in our hands!🐻‍❄️🏥")
animal =input("what animal do you want to ask about?")


if animal=="cat" or animal=="dog" or animal=="bird":
      print('''great! we can help you 
      but first we will take some information about your pet💕 ''')
      animal_name =input(f"what is your {animal}'s name?")
else:
   print("we are still working on adding more pets on baytara!")
   suggestion = input("would like us to suggest some animal hospitals for your pet in kuwait? ")
   if suggestion == "yes":
       print("https://www.bing.com/ck/a?!&&p=4b96dfde0caf628eJmltdHM9MTY5NDM5MDQwMCZpZ3VpZD0xNzU3MmRiZC0xMmQwLTY1ZTQtMGFjOS0zZWVkMTNkOTY0NDgmaW5zaWQ9NTE4Mw&ptn=3&hsh=3&fclid=17572dbd-12d0-65e4-0ac9-3eed13d96448&psq=%d9%85%d8%b3%d8%aa%d8%b4%d9%81%d9%89+%d8%a7%d9%84%d8%af%d9%87%d9%85%d8%a7%d8%a1+%d8%a7%d9%84%d8%a8%d9%8a%d8%b7%d9%8a%d8%b1%d9%8a%d8%a9&u=a1aHR0cHM6Ly9rdy5kYWxlZWwud2FzZWV0Lm5ldC9hci9rdXdhaXQtY2l0eS9oZWFsdGhjYXJlLW1lZGljaW5lL2hvc3BpdGFscy1tZWRpY2FsLWNlbnRlcnMvcGV0LWNhcmUtY2VudGVycy8lRDklODUlRDglQjMlRDglQUElRDglQjQlRDklODElRDklOEEtJUQ4JUE3JUQ5JTg0JUQ4JUFGJUQ5JTg3JUQ5JTg1JUQ4JUE3JUQ4JUExLSVEOCVBNyVEOSU4NCVEOCVBOCVEOSU4QSVEOCVCNyVEOCVCMSVEOSU4QS03MTc1Mzcw&ntb=1")
       print("https://www.bing.com/ck/a?!&&p=557120f6685971cdJmltdHM9MTY5NDM5MDQwMCZpZ3VpZD0xNzU3MmRiZC0xMmQwLTY1ZTQtMGFjOS0zZWVkMTNkOTY0NDgmaW5zaWQ9NTE3OQ&ptn=3&hsh=3&fclid=17572dbd-12d0-65e4-0ac9-3eed13d96448&psq=%d9%85%d8%b3%d8%aa%d8%b4%d9%81%d9%8a%d8%a7%d8%aa+%d8%a7%d9%84%d8%ad%d9%8a%d9%88%d8%a7%d9%86%d8%a7%d8%aa+%d8%a8%d8%a7%d9%84%d9%83%d9%88%d9%8a%d8%aa&u=a1aHR0cHM6Ly9pdmhxOC5jb20vYXIvJWQ4JWE3JWQ5JTg0JWQ4JWI1JWQ5JTgxJWQ4JWFkJWQ4JWE5LSVkOCVhNyVkOSU4NCVkOCViMSVkOCVhNiVkOSU4YSVkOCViMyVkOSU4YSVkOCVhOS8&ntb=1")
       print(''' thank you for visting baytara
         we welcome your all of your suggestions
                 for better BAYTARA
           for better life to our bets💕''')
   else:
         print(''' thank you for visting baytara
         we welcome your all of your suggestions
                 for better BAYTARA
           for better life to our bets💕''')

# animal_proplem        
print("please use your animal's name while discribing the problem") 
animal_problem=input(f"what is {animal_name}'s problem?")



# main if statment
if  animal=="cat" and animal_problem == f"{animal_name} has fleas" :
             print(f'''*Do the following steps:                  
                       1.use lemon
                       2.Buy antiparasitic collars
                       3.Wash the {animal}'s bedding with hot water
                   ''')
             print("thank ypu for chosing baytara as your animal saver!🐻‍❄️")    
elif animal =="cat" and animal_problem ==f"{animal_name} suffers from fungus":
      print('''*Do the following steps: 
            1.Apply Lamisil cream once a day to the fungal site
            2.Wash the fungus area with chlorhexidine shampoo''')
      print("here is a website for more information👇🏼")
      print (" https://saudi.desertcart.com/products/32779649-curaseb-antifungal-antibacterial-chlorhexidine-shampoo-for-dog-cats-treats-yeast-infections-ringworm-pyoderma-skin-allergies-broad-spectrum-veterinary-formula-16-oz")
      print("thank ypu for chosing baytara as your animal saver!🐻‍❄️")
elif animal =="cat" and animal_problem==f"{animal_name} is vomiting":
      print(f'''*Do the following steps: 
             1.make sure that{animal_name}'s water is clean
             2.give {animal_name} babylight solution every 2-5 hours''')
      print("if you want to buy it👇🏼")
      print("https://www.nahdionline.com/ar/babylyte-oral-solution-240ml")
      print("thank ypu for chosing baytara as your animal saver!🐻‍❄️")
elif animal =="dog" and animal_problem== f"{animal_name} is fat":  
      print(f'''*Do the following steps: 
            1.do not feed {animal_name} home made meals
            2.go for a walk with your dog daily for 30 mintues
            3.give {animal_name} vegetabels insted of sweets''')
      print("for more information👇🏼")
      print("https://blog.whiskers.shop/%D8%A7%D9%84%D8%B3%D9%85%D9%86%D8%A9-%D8%B9%D9%86%D8%AF-%D8%A7%D9%84%D9%83%D9%84%D8%A7%D8%A8/#google_vignette")
      print("thank ypu for chosing baytara as your animal saver!🐻‍❄️")
elif animal=="dog" and animal_problem == f"{animal_name} suffers from arthritis":
      print(f'''
            *Do the following steps: 
            1.buy dietary supplement
            2.buy arthrities medications
            *note:we recommend visting veterinarian for getting specific of medications👆🏼
            3.walk out with your dog!💕
            4.buy heating pad for {animal_name}''')
      print("thank ypu for chosing baytara as your animal saver!🐻‍❄️")
elif animal=="dog" and animal_problem==f"{animal_name} has fleas":
      print(f'''   *Do the following steps:                
                       1.use lemon
                       2.Buy antiparasitic collars
                       3.Wash the {animal}'s bedding with hot water
                   ''')
      print("thank ypu for chosing baytara as your animal saver!🐻‍❄️")
elif animal=="bird" and animal_problem==f"{animal_name}is suffering from diarrhea":
      print(f'''*Do the following steps: 
            1.you should isolate {animal_name} away from other birds
            2.keep the cage clean
            3.you can give him/her two drops of olive oil
            4. keep your bird away from water!''')
      print("thank ypu for chosing baytara as your animal saver!🐻‍❄️")   
elif animal=="bird" and animal_problem==f"{animal_problem} is counstantly chirping ":
      print(f'''
            coungratulations!🎉{animal_name} wants to get married
            you can look for a partner here👇🏼''') 
      print("https://q8rupee.com/info-73390.html")
      print("thank ypu for chosing baytara as your animal saver!🐻‍❄️") 
elif animal=="bird" and animal_problem==f"{animal_name} lays eggs":
      print(f'''
            congrats!🎉 your having a newborn bird🐣
            *Do the following steps: 
           1.do not touch {animal_name} alot
           2.do not separate the male bird from the female bird
           3.make sure that the birds cage is big enough''')
      bird_baby=input("what is the baby bird's name?")
      print(f"{bird_baby} is a lovely name!😇")
      print("thank ypu for chosing baytara as your animal saver!🐻‍❄️") 
else:
      print('''we are still adding more animal diseases
        for better baytara😸🐶
    for better life to our pets!''')
      
print("thank you") 
              
          
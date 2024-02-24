def should_serve_drink(age, inSession):
   
    if  age > 18 and inSession == False:
       print("True")

    else: 
      print("False")

should_serve_drink(17, True)
should_serve_drink(19, False)
should_serve_drink(30, True)

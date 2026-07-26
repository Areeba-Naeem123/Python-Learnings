def ticket_price(day,age):
    if day:
        price = 10 if age >=18 else 6
    else:
        price=12 if age >=18 else 8

    return price
wednesday=input("is today wednesday ?")
wednesday=wednesday.lower()
is_wednesday= (wednesday=="yes")

age =int (input("what is your age ?"))


price=ticket_price(is_wednesday,age )
print (price)

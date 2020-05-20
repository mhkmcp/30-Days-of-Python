# Lists

my_cart = [12.99, 312, 32, 142]
print(my_cart)
print('Sum: ', sum(my_cart))

my_cart.append(234)
print(my_cart)
print(len(my_cart))

print(my_cart[0])

msg = "Hello World"
# print 'o'
print(msg[4])


my_items = ["mouse", "laptop", "mic", "snack", "speaker"]
print(my_items)
print(my_cart)

print(my_items[2])
print(my_cart[2])

my_products = [my_items, my_cart]
print(my_products)

# my_dict = {my_items:my_cart}
# print(my_dict)

# Dictionaries
my_data = {'name': "Humayun Kabir", 'location': "Sylhet"}
print(my_data)
print(my_data['location'])
print(my_data.keys())
print(my_data.values())

my_data['Profession'] = "Software Engineer"
print(my_data)
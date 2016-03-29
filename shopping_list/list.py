list = []

def show_help():
	print("To see your list, type 'SHOW'")
	print("To see a list of commands, type 'HELP'")
	print("To quit, type 'DONE'")
	
def show_list():
	for items in list:
		print(items)
		
def add_to_list():
	list.append(item)
	print("Added {}. List now has {} items.".format(item, len(list)))

print("Shopping List")
print("To see a list of commands, type 'HELP'")

while True:
	item = input("Add an item: ")
	
	if item == 'DONE':
		break
		
	if item == 'SHOW':
		show_list()
		continue
			
	if item == 'HELP':
		show_help()
		continue
	
	add_to_list()

	
print("Here's your list:")

for items in list:
	print(items)

	

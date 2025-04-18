
my_list = ["apple", "banana", "cherry", "date", "fig", "grape"]

def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range!"


def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return "Element updated successfully!"
    else:
        return "Index out of range!"

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except:
        return "Invalid indices!"

def index_game():
    print("Welcome to the Index Game!")
    print("Your starting list is:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1 - Access an element")
        print("2 - Modify an element")
        print("3 - Slice the list")
        print("4 - Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            index = int(input("Enter the index to access: "))
            result = access_element(my_list, index)
            print("Result:", result)
        
        elif choice == "2":
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(my_list, index, new_value)
            print(result)
            print("Updated list:", my_list)
        
        elif choice == "3":
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)
        
        elif choice == "4":
            print("Thanks for playing the Index Game!")
            break
        
        else:
            print("Invalid choice. Try again.")


index_game()

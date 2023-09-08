# Function to perform operations on the inventory list
def perform_operations(N, initial_inventory, M, operations):
    inventory = dict(initial_inventory)

    # Initialize a variable to keep track of the total quantity
    total_quantity = sum(inventory.values())

    # Process each operation
    result = []

    for operation in operations:
        operation_name, item_name, quantity = operation.split()
        quantity = int(quantity)

        if operation_name == 'ADD':
            if item_name not in inventory:
                inventory[item_name] = quantity
                result.append(f'ADDED Item {item_name}')
            else:
                inventory[item_name] += quantity
                result.append(f'UPDATED Item {item_name}')
            total_quantity += quantity
        elif operation_name == 'DELETE':
            if item_name not in inventory:
                result.append(f'Item {item_name} does not exist')
            else:
                if inventory[item_name] < quantity:
                    result.append(f'Item {item_name} could not be DELETED')
                else:
                    inventory[item_name] -= quantity
                    result.append(f'DELETED Item {item_name}')
                    total_quantity -= quantity

    # Print the results of operations
    for line in result:
        print(line)

    # Print the total quantity
    print(f'Total Items in Inventory: {total_quantity}')

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N = int(input())
    initial_inventory = {}
    for _ in range(N):
        item_name, item_quantity = input().split()
        initial_inventory[item_name] = int(item_quantity)

    M = int(input())
    operations = [input() for _ in range(M)]

    perform_operations(N, initial_inventory, M, operations)

class InventoryItem:
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def update_quantity(self, amount):
        self.quantity += amount

    def total_value(self):
        return self.quantity * self.price_per_unit


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price_per_unit):
        if name in self.items:
            self.items[name].update_quantity(quantity)
        else:
            self.items[name] = InventoryItem(name, quantity, price_per_unit)

    def remove_item(self, name, quantity):
        if name in self.items:
            if self.items[name].quantity >= quantity:
                self.items[name].update_quantity(-quantity)
                if self.items[name].quantity == 0:
                    del self.items[name]
            else:
                print(f"Not enough quantity of {name} to remove.")
        else:
            print(f"Item {name} not found in inventory.")

    def view_inventory(self):
        print("\nCurrent Inventory:")
        for item in self.items.values():
            print(f"{item.name}: Quantity: {item.quantity}, Price per unit: {item.price_per_unit}, Total Value: {item.total_value():.2f}")

    def total_inventory_value(self):
        total_value = sum(item.total_value() for item in self.items.values())
        print(f"\nTotal Inventory Value: {total_value:.2f}")


def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Total Inventory Value")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price_per_unit = float(input("Enter price per unit: "))
            inventory.add_item(name, quantity, price_per_unit)

        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            inventory.remove_item(name, quantity)

        elif choice == '3':
            inventory.view_inventory()

        elif choice == '4':
            inventory.total_inventory_value()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

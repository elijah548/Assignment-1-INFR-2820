class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

class OnlineShop:
    def __init__(self):
        self.products = []
# Load products
    def load_products(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                id, name, price, category = line.strip().split(', ')
                self.products.append(Product(id, name, float(price), category))
        print("Loaded products from file.")
# Insert a product
    def insert_product(self, product):
        self.products.append(product)
        print(f"Inserted product: {product.name}")
# Update a product
    def update_product(self, id, **kwargs):
        for product in self.products:
            if product.id == id:
                product.name = kwargs.get('name', product.name)
                product.price = kwargs.get('price', product.price)
                product.category = kwargs.get('category', product.category)
                print(f"Updated product {id}: {product.name}, {product.price}, {product.category}")
                return True
        print(f"No product found with ID {id} to update.")
        return False
# Delete a product 
    def delete_product(self, id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                print(f"Deleted product with ID {id}")
                return True
        print(f"No product found with ID {id} to delete.")
        return False
# Search for a product
    def search_product(self, **kwargs):
        for product in self.products:
            if all(getattr(product, key) == value for key, value in kwargs.items()):
                print(f"Found product by {kwargs}: {product.name}")
                return product
        print(f"No product found with attributes {kwargs}.")
        return None
# Sorting algorithm Implementation
    def bubble_sort_by_price(self):
        n = len(self.products)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.products[j].price > self.products[j+1].price:
                    self.products[j], self.products[j+1] = self.products[j+1], self.products[j]
        print("Products have been sorted by price using Bubble Sort.")

    def insertion_sort_by_price(self):
        for i in range(1, len(self.products)):
            key = self.products[i]
            j = i-1
            while j >=0 and key.price < self.products[j].price :
                    self.products[j + 1] = self.products[j]
                    j -= 1
            self.products[j + 1] = key
        print("Products have been sorted by price using Insertion Sort.")

    # Interactive methods
    def interactive_insert_product(self):
        id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")
        self.insert_product(Product(id, name, price, category))

    def interactive_update_product(self):
        id = input("Enter product ID to update: ")
        name = input("Enter new name (leave blank to keep current): ")
        price = input("Enter new price (leave blank to keep current): ")
        category = input("Enter new category (leave blank to keep current): ")
        kwargs = {}
        if name:
            kwargs['name'] = name
        if price:
            kwargs['price'] = float(price)
        if category:
            kwargs['category'] = category
        self.update_product(id, **kwargs)

    def interactive_delete_product(self):
        id = input("Enter product ID to delete: ")
        self.delete_product(id)

    def interactive_search_product(self):
        search_attribute = input("Search by 'id' or 'name'? ")
        search_value = input(f"Enter {search_attribute}: ")
        if search_attribute == 'id':
            self.search_product(id=search_value)
        elif search_attribute == 'name':
            self.search_product(name=search_value)
        else:
            print("Invalid search attribute.")

# The main loop for interactive prompts
if __name__ == "__main__":
    shop = OnlineShop()
    shop.load_products('product_data.txt')

    while True:
        print("\nAvailable operations:")
        print("1: Insert a new product")
        print("2: Update a product")
        print("3: Delete a product")
        print("4: Search for a product")
        print("5: Display all products")
        print("6: Sort products by price")
        print("0: Exit")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            shop.interactive_insert_product()
        elif choice == '2':
            shop.interactive_update_product()
        elif choice == '3':
            shop.interactive_delete_product()
        elif choice == '4':
            shop.interactive_search_product()
        elif choice == '5':
            print("\nList of all products:")
            for product in shop.products:
                print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")
        elif choice == '6':
            method = input("Choose a sorting method (bubble or insertion): ")
            if method.lower() == 'bubble':
                shop.bubble_sort_by_price()
            elif method.lower() == 'insertion':
                shop.insertion_sort_by_price()
            else:
                print("Invalid sorting method.")
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


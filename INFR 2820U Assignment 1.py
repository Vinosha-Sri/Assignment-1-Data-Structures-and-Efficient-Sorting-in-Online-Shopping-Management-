import time
import random
# A class named Product was created to contain all the details of the product:
class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Category: {self.category}"
# Creates an array to manage all the products:
class ProductArray:
    def __init__(self):
        self.products = []
        self.id_index = {}
        self.name_index = {}
        self.price_index = {}
        self.category_index = {}
    def loaddata(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                id, name, price, category = line.strip().split(',')
                product = Product(int(id), name, float(price), category)
                self.products.append(product)
                self.indices(product)
        sorttime = self.pricebubblesort()  # Sorts array.
        print(f"Data loaded and sorted in {sorttime:.6f} seconds")  # States time for sorting.
    def savedata(self, filename):
        with open(filename, 'w') as file:
            for product in self.products:
                file.write(f"{product.id},{product.name},{product.price},{product.category}\n")
    # Function that inserts new products to the array: 
    def insert_product(self, product):
        self.products.append(product)
        self.indices(product)
        sorttime = self.pricebubblesort()  # Sorts array after the insertion.
        print(f"Product inserted and sorted in {sorttime:.6f} seconds")  # States time for sorting.
    # Function that updates existing products to the array: 
    def update_product(self, product_id, updatedproduct):
        product = self.id_index.get(product_id)
        if product:
            self.remove_from_indices(product)
            product.name = updatedproduct.get("Name", product.name)
            product.price = updatedproduct.get("Price", product.price)
            product.category = updatedproduct.get("Category", product.category)
            self.indices(product)
            sorttime = self.pricebubblesort()  # Sorts array after updating.
            print(f"Product updated and sorted in {sorttime:.6f} seconds")  # States time for sorting.
    # Function that deletes products in the array: 
    def delete_product(self, product_id):
        product = self.id_index.get(product_id)
        if product:
            self.remove_from_indices(product)
            self.products.remove(product)
            sorttime = self.pricebubblesort()  # Sorts array after deletion.
            print(f"Product deleted and sorted in {sorttime:.6f} seconds")  # States time for sorting.
    # Function that searches products by the ID in the array: 
    def search_product_by_id(self, product_id):
        return self.id_index.get(product_id, None)
    # Function that searches products by the Product Name in the array: 
    def search_product_by_name(self, product_name):
        return self.name_index.get(product_name.lower(), [])
    # Function that searches products by the Price in the array: 
    def search_product_by_price(self, price):
        return self.price_index.get(price, [])
    # Function that searches products by the Category in the array: 
    def search_product_by_category(self, category):
        return self.category_index.get(category.lower().strip(), [])
    def pricebubblesort(self):
        starttime = time.time()
        n = len(self.products)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.products[j].price > self.products[j+1].price:
                    self.products[j], self.products[j+1] = self.products[j+1], self.products[j]
        end_time = time.time()
        return end_time - starttime
    def indices(self, product):
        self.id_index[product.id] = product
        self.name_index.setdefault(product.name.lower().strip(), []).append(product)
        self.price_index.setdefault(product.price, []).append(product)
        self.category_index.setdefault(product.category.lower().strip(), []).append(product)
    def remove_from_indices(self, product):
        del self.id_index[product.id]
        self.name_index[product.name.lower().strip()].remove(product)
        if not self.name_index[product.name.lower().strip()]:
            del self.name_index[product.name.lower().strip()]
        self.price_index[product.price].remove(product)
        if not self.price_index[product.price]:
            del self.price_index[product.price]
        self.category_index[product.category.lower().strip()].remove(product)
        if not self.category_index[product.category.lower().strip()]:
            del self.category_index[product.category.lower().strip()]
    def printproduct(self):
        for product in self.products:
            print(product)

# Main Function: 
if __name__ == "__main__":
    # Product array formed and loads data: 
    product_manager = ProductArray()
    product_manager.loaddata("product_data.txt")
    # Prints the initial products:
    print("Initial Product List:")
    product_manager.printproduct()
    print()
    # Inserts a new product to the array:
    new_product = Product(12345, "Macbook", 1200.99, "Category: Electronics")
    product_manager.insert_product(new_product)
    print("After Insertion of Macbook:")
    product_manager.printproduct()
    print()
    # Update an existing product in the array:
    updatedproduct = {"Name": "Updated Macbook", "Price": 1304.99}
    product_manager.update_product(12345, updatedproduct)
    print("After Updating Macbook Product:")
    product_manager.printproduct()
    print()
    # Delete a product in the array:
    product_manager.delete_product(12345)
    print("After Deleting Macbook Product:")
    product_manager.printproduct()
    print()
    # Search for a product by ID in the array,
    search_result = product_manager.search_product_by_id(85197)
    print("Search Result for Product with ID 85197:")
    if search_result:
        print(search_result)
    else:
        print("Product is not in the inventory.")
    print()
    # Search for a product by Name in the array,
    search_results = product_manager.search_product_by_name("Dress FRSMO")
    print("Search Results for Product with Name 'Dress FRSM':")
    if search_results:
        for result in search_results:
            print(result)
    else:
        print("Product is not in the inventory.")
    print()
    # Search for a product by Price in the array.
    search_results = product_manager.search_product_by_price(647.08)
    print("Search Results for Products with Price 647.08:")
    if search_results:
        for result in search_results:
            print(result)
    else:
        print("Product is not in the inventory.")
    print()
    # Search for a product by Category in the array.
    search_results = product_manager.search_product_by_category("Clothing")
    print("Search Results for Products in Category 'Clothing':")
    if search_results:
        for result in search_results:
            print(result)
    else:
        print("Product is not in the inventory.")
    print()
    # Sorting and Complexity Analysis:
    random.shuffle(product_manager.products)  
    print("Shuffled Products:")
    product_manager.printproduct()
    print()
    # Bubble Sort and Complexity Analysis:
    bubblesorttime = product_manager.pricebubblesort()
    print("Bubble Sort Time:", bubblesorttime)
    print("Sorted List (Bubble Sort):")
    product_manager.printproduct()
    print()
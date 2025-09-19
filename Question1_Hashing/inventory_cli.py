from product import Product
from hash_table import Hashtable

# menu to display options
def menu():
    print("********************************************")
    print("=== Baby Shop Inventory System ===")
    print("********************************************")
    print("1. Insert product")
    print("2. Search product")
    print("3. Edit product")
    print("4. Delete product")
    print("5. Display all products")
    print("********************************************")
    print("6. Exit")
    print("********************************************")

# main function
def main():
    hashtable = Hashtable(size=20)

    while True:
        menu()
        choice = int(input("Enter a choice (1-6): "))

        # insert new product
        if choice == 1:
            productID = input("Enter Product ID: ")
            name = input("Enter name: ")
            category = input("Enter category: ")
            brand = input("Enter brand: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter stock quantity: "))
            product = Product(productID, name, category, brand, price, stock)
            hashtable.insert(productID, product)  # Insert into hash table
            print("Product inserted.")

        # search product
        elif choice == 2:
            productID = input("Enter the product ID to search: ")
            product = hashtable.search(productID)
            if product:
                print(f"Product Found: {product}")
            else:
                print("Product Not Found.")

        # edit product
        elif choice == 3:
            productID = input("Enter the product ID to edit: ")
            product = hashtable.search(productID)
            if product:
                print(f"Editing: {product}")
                # input new value or remain same if no input
                name = input(f"Enter new name ({product.name}): ") or product.name
                category = input(f"Enter new category ({product.category}): ") or product.category
                brand = input(f"Enter new brand ({product.brand}): ") or product.brand
                price = input(f"Enter new price ({product.price}): ")
                stock = input(f"Enter new stock ({product.stock_quantity}): ")

                # Create updated product
                product = Product(productID, name, category, brand, float(price) if price else product.price,
                                  int(stock) if stock else product.stock_quantity )
                hashtable.edit(productID, product)
                print("Product Updated.")
            else:
                print("Product Not Found.")

        # delete product
        elif choice == 4:
            productID = input("Enter product ID to delete: ")
            if hashtable.delete(productID):
                print("Product Deleted.")
            else:
                print("Product Not Found.")

        # display all product
        elif choice == 5:
            hashtable.display()
        
        # exit the program
        elif choice == 6:
            print("Exiting...")
            break

       # invalid input     
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

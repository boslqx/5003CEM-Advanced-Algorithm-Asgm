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


def upload_products(ht):
    sample_products = [
        Product("P001", "Baby Diapers (S)", "Diapers", "Pampers", 35.90, 50),
        Product("P002", "Baby Diapers (M)", "Diapers", "Huggies", 38.50, 40),
        Product("P003", "Baby Diapers (L)", "Diapers", "Mamypoko", 42.00, 35),
        Product("P004", "Baby Milk Formula 0-6M", "Milk", "Enfagrow", 120.00, 20),
        Product("P005", "Baby Milk Formula 6-12M", "Milk", "Similac", 110.00, 25),
        Product("P006", "Baby Bottle 250ml", "Feeding", "Philips Avent", 25.00, 60),
        Product("P007", "Baby Bottle 150ml", "Feeding", "Tommee Tippee", 22.00, 55),
        Product("P008", "Pacifier (0-6M)", "Accessories", "Nuk", 15.00, 70),
        Product("P009", "Pacifier (6-18M)", "Accessories", "MAM", 18.00, 65),
        Product("P010", "Baby Stroller", "Equipment", "Chicco", 450.00, 10),
        Product("P011", "Baby Car Seat", "Equipment", "Graco", 520.00, 8),
        Product("P012", "Baby Walker", "Equipment", "Fisher-Price", 280.00, 12),
        Product("P013", "Baby Lotion", "Care", "Johnson’s", 18.50, 100),
        Product("P014", "Baby Shampoo", "Care", "Sebamed", 22.90, 80),
        Product("P015", "Baby Soap", "Care", "Dove", 8.90, 120),
        Product("P016", "Wet Wipes (80 sheets)", "Care", "Pureen", 9.50, 150),
        Product("P017", "Baby Blanket", "Bedding", "Mothercare", 45.00, 30),
        Product("P018", "Baby Pillow", "Bedding", "SweetDreams", 25.00, 35),
        Product("P019", "Baby Onesie (0-3M)", "Clothing", "Carter’s", 39.90, 40),
        Product("P020", "Baby Socks (5 pairs)", "Clothing", "H&M", 15.90, 60),
    ]

    for product in sample_products:
        ht.insert(product.product_id, product)

# main function
def main():
    hashtable = Hashtable(size=20)
    upload_products(hashtable)

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
                product = Product(productID, name, category, brand, float(price) 
                                  if price else product.price,
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

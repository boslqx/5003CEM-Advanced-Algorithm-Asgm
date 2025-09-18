import time
from product import Product
from hash_table import Hashtable

# create array and hash table to compare
def performance_test():
    hashtable = Hashtable(size=50)
    arr = []

    # insert dummy data
    for i in range(1000):
        product = Product(str(i), f"Product{i}", "CategoryA", "BrandX", i * 1.5, 10)
        hashtable.insert(product.product_id, product) # insert into hash table
        arr.append(product) # insert into array

    # Search value in hash table and measure time
    start = time.perf_counter_ns() # start timer
    hashtable.search("500")
    end = time.perf_counter_ns() # end timer
    print(f"Hash Table search time: {end - start} ns")

    # search value in array format and measure time
    start = time.perf_counter_ns()
    for p in arr:
        if p.product_id == 500:
            break
    end = time.perf_counter_ns()
    print(f"Array search time: {end - start} ns")

if __name__ == "__main__":
    performance_test()
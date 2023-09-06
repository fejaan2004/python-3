# Initialize an empty list to store real estate listings
listings = []

# Function to add a new listing
def add_listing():
    print("Add a New Listing")
    address = input("Enter the property address: ")
    price = input("Enter the listing price: ")
    bedrooms = input("Enter the number of bedrooms: ")
    bathrooms = input("Enter the number of bathrooms: ")

    listing = {
        "Address": address,
        "Price": price,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
    }

    listings.append(listing)
    print("Listing added successfully!")

# Function to view all listings
def view_listings():
    print("\nReal Estate Listings:")
    for index, listing in enumerate(listings, start=1):
        print(f"Listing {index}:")
        for key, value in listing.items():
            print(f"{key}: {value}")
        print("")

# Function to search for listings by price range
def search_by_price():
    min_price = input("Enter minimum price: ")
    max_price = input("Enter maximum price: ")

    print(f"Listings between {min_price} and {max_price}:")

    for listing in listings:
        price = float(listing["Price"])
        if float(min_price) <= price <= float(max_price):
            print(f"Address: {listing['Address']}, Price: {listing['Price']}")

# Main program loop
while True:
    print("\nReal Estate Listings Menu:")
    print("1. Add Listing")
    print("2. View Listings")
    print("3. Search by Price Range")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        add_listing()
    elif choice == "2":
        view_listings()
    elif choice == "3":
        search_by_price()
    elif choice == "4":
        print("Exiting Real Estate Listings. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

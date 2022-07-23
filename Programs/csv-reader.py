USERS = "./data_store/users.csv"
ADDRESSES = "./data_store/addresses.csv"

def load_users():
    """
    Loads users csv
    :return:
    """

    with open(USERS, "r") as file:
        # creates dictionary to separate csv values to make it easy to iterate between them
        # the hash() function is used to identify the values in the csv, as they have their individual hash
        # keys, and as the csv is immutable it'll be the same throughout
        users = {}
        for user in file:
            user = user.strip().split(",")
            user_tuple = create_user(*user[:5], int(user[5]))
            users[hash(user_tuple)] = user_tuple

    return users

def load_addresses():
    """
    Loads adddresses csv
    :return:
    """

    with open(ADDRESSES, "r") as file:
        addresses = {}
        for address in file:
            address_tuple = create_address(*address.strip().split(","))
            addresses[hash(address_tuple)] = address_tuple

    return addresses

def load_datastore():
    """
    Creates datastore data structure (similar to a database)
    A dictionary containing two keys ["users", "addresses"]. The "Users" entry stores a dictionary with keys containing
    the hashed user's and the entries containing the user datastructures. The same principle is applied to "Addresses"
    :return: (dict)
    """

    return {"users": load_users(), "addresses": load_addresses()}

def write_users(users):
    with open(USERS, "w") as file:
        file.write("\n".join([
            "{0},{1},{2},{3},{4},{5}".format(*user) for user in users
        ]))

def write_addresses(addresses):
    with open(ADDRESSES, "w") as file:
        file.write("\n".join([
            "{0},{1}".format(*address) for address in addresses
        ]))

def write_datastore(datastore):
    write_users(datastore["users"].values())
    write_addresses(datastore["addresses"].values())

def create_address(house_number, post_code):
    """
    Creates immutable address data structure
    :param house_number: user's house number (string)
    :param post_code: user's post code (string)
    :return: (tuple)
    """

    return (house_number, post_code)

def create_user(first_name, last_name, email, phone_number, dob, address_id):
    """
    Creates immutable user data structure
    :param first_name: user's first name (string)
    :param last_name: user's last name (string)
    :param email: user's email (string)
    :param phone_number: user's phone number (string)
    :param dob: user's date of birth (string)
    :return: (tuple)
    """

    return (first_name, last_name, email, phone_number, dob, address_id)

def format_user(datastore, user_hash):
    """
    :param datastore:
    :param user_hash:
    :return:
    """

    return "First Name: {0}, Last Name: {1}, Email: {2}, Phone Number: {3}, Date of Birth: {4}, Address: {5}".format(
        *datastore["users"][user_hash][:5],
        format_address(datastore, datastore["users"][user_hash][5])
    )

def format_address(datastore, address_hash):
    """
    :param datastore:
    :param address_hash:
    :return:
    """

    return "{0}, {1}".format(*datastore["addresses"][address_hash])

def main_page(datastore):
    options = [
        (1,"Create new user", new_user),
        (2, "Search for user", search_user),
        (3, "Exit", exit_data_entry)
    ]
    print("""
        +------------------------+
        |                        |
        | Data Entry Application |
        |                        |
        +------------------------+
    """)
    print("Options:")
    for id, option, *_ in options:
        print("{0}: {1}".format(id, option))

    choice = int(input("> "))
    results = list(filter(lambda x: choice == x[0], options))

    if results:
        results[0][2](datastore=datastore)
    else:
        print("Failed to select valid option. Trying again.")

    main_page(datastore)

def exit_data_entry(datastore):
    write_datastore(datastore)
    print("[+] Successfully saved the datastore.")
    print("[+] Exiting...")
    exit()

def new_user(datastore):
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    dob = input("Enter your data of birth: ")
    house_number = input("Enter your house number: ")
    post_code = input("Enter your post code: ")

    address = create_address(house_number, post_code)
    address_hash = hash(address)
    datastore["addresses"][address_hash] = address
    print(address_hash)
    print(datastore)

    user = create_user(first_name, last_name, email, phone_number, dob, address_hash)
    user_hash = hash(user)
    datastore["users"][user_hash] = user

    print("[+] Successfully added new user with the following details:")
    print(format_user(datastore, user_hash))
    print(datastore)


def search_user(datastore):
    first_name = input("Enter first name: ")
    users = list(filter(lambda x: first_name == x[0], datastore["users"].values()))

    print("[+] {0} results (0 seconds)".format(len(users)))
    for id, user in enumerate(users):
        print("\t" + format_user(datastore, hash(user)))

if __name__ == "__main__":
    main_page(load_datastore())

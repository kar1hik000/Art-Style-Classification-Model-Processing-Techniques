def get_user_input():
    # Get input for the first list
    list1 = list(map(int, input("Enter the elements of the first list separated by space: ").split()))
    
    # Get input for the second list
    list2 = list(map(int, input("Enter the elements of the second list separated by space: ").split()))
    
    return list1, list2


def find_common_elements(list1, list2):
    # Find the common elements using set intersection
    common_elements = set(list1) & set(list2)
    return list(common_elements)


def count_common_elements(list1, list2):
    # Get the count of common elements
    common_elements_count = len(find_common_elements(list1, list2))
    return common_elements_count


if __name__ == "__main__":
    # Get user input for two lists
    input_lists = get_user_input()
    list1, list2 = input_lists

    # Find the common elements
    common_elements = find_common_elements(list1, list2)

    # Count the number of common elements
    common_elements_count = count_common_elements(list1, list2)

    # Print the results
    print(f"Common Elements: {common_elements}")
    print(f"Number of Common Elements: {common_elements_count}")

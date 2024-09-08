import json

def sortFood():
    # Step 1: Load the JSON file
    with open('static/food.json', 'r') as file:
        data = json.load(file)

    # Step 2: Sort the items within each category based on 'ranking'
    for menu in data['menus']:
        # Tim Sort ; merge sort and insertion sort.
        menu['items'].sort(key=lambda x: x['ranking'], reverse=True)

    # Step 3: Write the sorted data to a new JSON file
    with open('static/sorted_food.json', 'w') as sorted_file:
        json.dump(data, sorted_file, indent=4)

    print("Sorted data has been written to sorted_food.json")

sortFood()
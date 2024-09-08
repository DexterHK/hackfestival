
var jsony = JSON.parse('{{ user | tojson | safe}}');

    function renderMenu(menuData) {
    const menuContainer = document.getElementById('menu-container');

    menuData.menus.forEach(menu => {
        // Create a div for each category
        const categoryDiv = document.createElement('div');
        categoryDiv.className = 'category';

        // Add category title
        const categoryTitle = document.createElement('h2');
        categoryTitle.textContent = menu.category;
        categoryDiv.appendChild(categoryTitle);

        // Loop through each item in the category
        menu.items.forEach(item => {
            const foodItemDiv = document.createElement('div');
            foodItemDiv.className = 'food-item';

            // Add food name and ranking
            const foodName = document.createElement('h3');
            foodName.innerHTML = `${item.food_name} (Ranking: <span class="ranking">${item.ranking}</span>)`;
            foodItemDiv.appendChild(foodName);

            // Add ingredients
            const ingredients = document.createElement('p');
            ingredients.textContent = `Ingredients: ${item.ingredients.join(', ')}`;
            foodItemDiv.appendChild(ingredients);

            // Add food picture (comment out if not needed)
            const foodImage = document.createElement('img');
            foodImage.src = item.food_picture;
            foodImage.width = 400;
            foodImage.height = 200;
            foodImage.alt = item.food_name;
            foodItemDiv.appendChild(foodImage);

            if (item.ranking >= 7) {
                const decarbonizationSymbol = document.createElement('span');
                decarbonizationSymbol.className = 'decarbonization-symbol';
                decarbonizationSymbol.innerHTML = '🌿'; // Green symbol for decarbonization
                foodItemDiv.appendChild(decarbonizationSymbol);
            }
            else if (item.ranking < 7 && item.ranking >= 5) {
                const decarbonizationSymbol = document.createElement('span');
                decarbonizationSymbol.className = 'gelbdecarbonization-symbol';
                decarbonizationSymbol.innerHTML = '🍂'; // Green symbol for decarbonization
                foodItemDiv.appendChild(decarbonizationSymbol);
            }
            else {
                const decarbonizationSymbol = document.createElement('span');
                decarbonizationSymbol.className = 'reddecarbonization-symbol';
                decarbonizationSymbol.innerHTML = '🍁'; // Green symbol for decarbonization
                foodItemDiv.appendChild(decarbonizationSymbol);
            }


            // Append each food item to the category div
            categoryDiv.appendChild(foodItemDiv);
        });

        // Append each category to the container
        menuContainer.appendChild(categoryDiv);
    });
}

// Call the function to render the menu
renderMenu(jsony);


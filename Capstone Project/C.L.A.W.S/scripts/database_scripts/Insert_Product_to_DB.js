const fs = require('fs');
const mysql = require('mysql2');
const process = require('process');

// Create a MySQL database connection
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'BobcatClawsDev',
    password: 'CS#4398DB',
    database: 'BobcatClawsDB'
});

// Connect to the MySQL database
connection.connect((err) => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('Connected to MySQL database');
});

// Read the JSON file
const json_file_name = process.argv[2] || 'BestBuy.json';
fs.readFile(`/home/workspace/Software-Engineering-Project-Course/scripts/json_files/${json_file_name}`, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading the JSON file:', err);
        return;
    }
    // Parse the JSON data
    try {
        const dataArray = JSON.parse(data);
        const store = dataArray.Store;

        // Function to check if a store exists
        function checkIfStoreExists(storeName, callback) {
            const checkStoreStatement = `
                SELECT ID FROM Store WHERE Name = ?
            `;

            connection.query(checkStoreStatement, [storeName], (err, results) => {
                if (err) {
                    console.error('Error checking if the store exists:', err);
                    callback(err, null);
                } else {
                    callback(null, results.length > 0 ? results[0].ID : null);
                }
            });
        }

        // Function to check if a product exists
        function checkIfProductExists(productName, callback) {
            const checkProductStatement = `
                SELECT ID FROM Product WHERE Name = ?
            `;

            connection.query(checkProductStatement, [productName], (err, results) => {
                if (err) {
                    console.error('Error checking if the product exists:', err);
                    callback(err, null);
                } else {
                    callback(null, results.length > 0 ? results[0].ID : null);
                }
            });
        }

        // Check if the store exists
        checkIfStoreExists(store.Name, (err, storeExists) => {
            if (err) {
                return; // Handle the error as needed
            }

            let storeID;
            if (!storeExists) {
                // Store does not exist, insert it into the 'stores' table
                const insertStoreStatement = `
                    INSERT INTO Store (ID, Name)
                    VALUES (?, ?)
                `;

                const storeIdValue = store.Name.slice(0,4).toUpperCase();
                connection.query(insertStoreStatement, [storeIdValue, store.Name], (err, storeResults) => {
                    if (err) {
                        console.error('Error inserting store data:', err);
                    } else {
                        storeID = storeIdValue;
                        console.log(`Store data inserted successfully with ID: ${storeIdValue}`);
                    }
                });
            } else {
                console.log(`Store with name '${store.Name}' already exists. with ID: ${storeExists}`);
                storeID = storeExists;
            }

            const products = store.Products;
            products.forEach(product => {
                checkIfProductExists(product.Name, (err, productExists) => {
                    if (err) {
                        return; 
                    }

                    if (!productExists) {
                        const insertProductStatement = `
                            INSERT INTO Product (UPC, Name, Category_ID, Sub_category_ID, Description, Img_URL, Keywords)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                        `;

                        connection.query(insertProductStatement, [product.UPC, product.Name, product.Category_ID, product.Sub_category_ID, product.Description, product.Img_URL, '[]'], (err, productResults) => {
                            if (err) {
                                console.error('Error inserting product data:', err);
                            } else {
                                const productID = productResults.insertId;
                                console.log(`Product data inserted successfully with ID: ${productID}`);

                                // Insert Product_Store_Price
                                const insertProduct_Store_PriceStatement = `
                                    INSERT INTO Product_Store_Price (Product_ID, Store_ID, Price, URL)
                                    VALUES (?, ?, ?, ?)
                                `;
                                let price = product.Price.replace("$", "").replace(',', "");
                                price = isNaN(price) ? null : price;

                                connection.query(insertProduct_Store_PriceStatement, [productID, storeID, price, product.URL], (err, Product_Store_Price_Results) => {
                                    if (err) {
                                        console.error('Error inserting product price data:', err);
                                    } else {
                                        console.log(`Product price data inserted successfully with ID: ${Product_Store_Price_Results.insertId}`);
                                    }
                                });
                            }
                        });
                    } else {
                        console.log(`Product with name '${product.Name}' already exists. With ID: ${productExists}`);
                    }
                });
            });
        });
    } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
    }
});

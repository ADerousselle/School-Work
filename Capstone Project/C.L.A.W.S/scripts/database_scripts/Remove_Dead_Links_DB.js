const mysql = require('mysql2');
const axios = require('axios');

// Configure your MySQL connection
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'BobcatClawsDev',
    password: 'CS#4398DB',
    database: 'BobcatClawsDB'
});

// Connect to MySQL
connection.connect(err => {
    if (err) {
        console.error('Error connecting to MySQL:', err);
        return;
    }
    console.log('Connected to MySQL');

    // Query all URLs from the Product_Store_Price table
    const queryAllLinks = 'SELECT Product_ID, URL FROM Product_Store_Price';
    connection.query(queryAllLinks, async (err, results) => {
        if (err) {
            console.error('Error querying for links:', err);
            return;
        }

        for (let row of results) {
            try {
                // Check each URL
                await axios.get(row.URL);
            } catch (error) {
                // If URL is dead, delete the related product
                if (error.response) {
                    const productId = row.Product_ID;
                    console.log(`Dead link found for Product ID ${productId}, URL: ${row.URL}`);

                    // Delete from Product_Store_Price table
                    const deleteProductStorePrice = 'DELETE FROM Product_Store_Price WHERE Product_ID = ?';
                    connection.query(deleteProductStorePrice, [productId], (err, result) => {
                        if (err) {
                            console.error(`Error deleting from Product_Store_Price for Product_ID ${productId}:`, err);
                            return;
                        }
                        console.log(`Deleted from Product_Store_Price for Product_ID ${productId}`);
                    });

                    // Optionally, delete from Product table
                    // const deleteProduct = 'DELETE FROM Product WHERE ID = ?';
                    // connection.query(deleteProduct, [productId], (err, result) => {
                    //     if (err) {
                    //         console.error(`Error deleting from Product for ID ${productId}:`, err);
                    //         return;
                    //     }
                    //     console.log(`Deleted from Product for ID ${productId}`);
                    // });
                }
            }
        }
    });
});

// Close the connection on process exit
process.on('exit', () => {
    connection.end();
});

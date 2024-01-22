import axios from 'axios';

// Function to retrieve discount information from the Honey API
async function getDiscountFromAPI(productId: string): Promise<number> {
    try {
        // Replace 'API_ENDPOINT' with the actual endpoint from Honey API documentation
        const apiEndpoint = `API_ENDPOINT/discounts/${productId}`;

        // Make a GET request to the Honey API
        const response = await axios.get(apiEndpoint);

        // Check if the request was successful (status code 200)
        if (response.status === 200) {
            // Parse the JSON response
            const discountInfo = response.data;

            // Return the discount percentage
            return discountInfo.discountPercentage;
        } else {
            // Log an error message if the request was not successful
            console.error(`Error: ${response.status} - ${response.data}`);
            return 0; // Default to no discount in case of an error
        }
    } catch (error) {
        console.error(`An error occurred: ${error.message}`);
        return 0; // Default to no discount in case of an error
    }
}

// Function to apply the discount retrieved from the Honey API
async function applyDiscount(originalPrice: number, productId: string): Promise<number> {
    // Retrieve the discount percentage from the Honey API
    const discountPercentage = await getDiscountFromAPI(productId);

    // Calculate the discount amount
    const discountAmount = (originalPrice * discountPercentage) / 100;

    // Return the discounted price
    return originalPrice - discountAmount;
}

// Test the function with a hypothetical product ID
const productId = '123'; // Replace with an actual product ID from your system
const originalPrice = 100; // For example, $100

// Apply the discount and log the results
applyDiscount(originalPrice, productId)
    .then(discountedPrice => {
        console.log(`Original Price: $${originalPrice}`);
        console.log(`Discounted Price: $${discountedPrice.toFixed(2)}`);
    })
    .catch(error => console.error(`Error: ${error.message}`));

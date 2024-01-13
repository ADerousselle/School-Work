# CS4398 Software Project
## Welcome to C.L.A.W.S. Project Repository
C.L.A.W.S. - College Lifstyle Affordable Wares is an innovative project that has been in development for the past three months. Our goal with this project has been to create a powerful tool that effectively gathers and manages product data. The working prototype that we have developed reflects our dedication to this goal, and we are excited to present our progress thus far. While staying true to our original vision, we've had to make strategic adjustments to our scope, considering our data gathering capabilities and the evolving needs of the project. As we continue to develop C.L.A.W.S., we are constantly evaluating and refining our approach, ensuring that our final product will not only meet but exceed our expectations.

At the heart of the C.L.A.W.S. project is our sophisticated database system, designed to store and manage product data in a structured manner. The database is organized into three main categories and sixteen subcategories, making it straightforward for both front-end and back-end processes to access and utilize the data efficiently. Our data collection strategy leverages APIs from major retailers such as Walmart and Target, complemented by web scraping techniques for Best Buy. This comprehensive approach enables us to provide a rich dataset that powers the core functionalities of C.L.A.W.S. As we prepare for our final presentation on November 30th, we continue to focus on quality control, testing, and maintenance procedures, ensuring the reliability and effectiveness of our project.


My code is located 

CLAWS\scripts\api_scripts\Parsehub.py
	Uses the Parsehub API to call on Parsehub to scrape the BestBuy website for	predefined product information.
CLAWS\scripts\api_scripts\tAPI.py
	Uses the RedCart API to pull product information from the Target webstore.
CLAWS\scripts\api_scripts\wmAPI.py
	Uses the BlueCircle API to pull product information from the Walmart webstore.
CLAWS\scripts\api_scripts\tests\test_Parsehub.py
CLAWS\scripts\api_scripts\tests\test_tAPI.py
CLAWS\scripts\api_scripts\tests\test_wmAPI.py

//TODO once the code is pulled
run these in the terminal

"sudo apt-get update --fix-missing" #Check if any necessary packages need to be updated or downloaded

"sudo make all" #run the makefile

"sudo npm install bootstrap --save" 

"sudo ng -serve" #agree to autocompletion and use a port that is not in use if asked

#from here it will diplay the local host that the website is running on. 
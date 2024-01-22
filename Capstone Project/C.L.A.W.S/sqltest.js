const fs = require('fs');
const mysql = require('mysql');
const path = require('path');

// Database configuration
const dbConfig = {
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'people',

};


const dir = 'test_new';
const dirOld = 'test_old';

function parseNewFile(filepath){

	// Read the JSON file
	fs.readFile('example.json', 'utf8', (err, data) => {
	  if (err) {
	    console.error('Error reading the file: ' + err);
	    return;
	  }

	  try {
	    const jsonData = JSON.parse(data);

	    // Create a MySQL database connection
	    const connection = mysql.createConnection(dbConfig);

	    // Connect to the database
	    connection.connect((err) => {
	      if (err) {
		console.error('Error connecting to the database: ' + err.stack);
		return;
	      }

	      console.log('Connected to the database as ID ' + connection.threadId);

	      // Insert JSON data into the database
	      jsonData.forEach((item) => {
		const sql = 'INSERT INTO peopletable (name, age) VALUES (?, ?)';
		const values = [item.name, item.age];

		connection.query(sql, values, (err, result) => {
		  if (err) {
		    console.error('Error inserting data: ' + err.message);
		  } else {
		    console.log('Inserted row ID: ' + result.insertId);
		  }
		});
	      });

	      // Close the database connection
	      connection.end((err) => {
		if (err) {
		  console.error('Error closing the database connection: ' + err.message);
		} else {
		  console.log('Database connection closed.');
		}
	      });
	    });
	  } catch (error) {
	    console.error('Error parsing JSON: ' + error);
	  }
	});

	const fileName = path.basename(filepath);
	const newFilePath = path.join(dirOld, fileName);

	fs.rename(filepath, newFilePath, (err) => {
		if (err) {
			console.log('Error moving file: ' + err);
		} else {
			console.log('File moved to: ${newFilePath}');
		}


	});	
}
//watch new directory for JSON files
fs.watch(dir, (eventType, fileName) => {
	if (eventType == 'rename' && path.extname(fileName) === '.json'){
		const filePath = path.join(dir, fileName);
		parseNewFile(filePath);

	}






});	

console.log("Watching for a new JSON file in the directory: test_new");

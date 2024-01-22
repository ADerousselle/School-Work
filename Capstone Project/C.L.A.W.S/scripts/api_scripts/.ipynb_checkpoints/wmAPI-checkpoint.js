const axios = require('axios');

const fs = require('fs');
let key = null;
fs.readFile('api.env', 'utf8', (err, data) => {
	if(err){
		console.error(err)
	}
	const lines = data.split('\n');
	console.log("data split");
	for (const line of lines){
		if (line.includes("BlueCart")){
			console.log("Found line that contains right words");
			const parts = line.split('" = "');
			if (parts.length == 2){
				key = parts[1].replace(/"/g, '');
				console.log("key is " + key)
				break;

			}
		}


	}

})


// set up the request parameters
 
const params = {
api_key: key,
  search_term: "laptop",
  type: "search",
  output: "json"
}
template = {
	
	Store: {
		Name: '',

		Products: [
			//{
				/**
				UPC:  null,
				Name:  '',
				Price: null,
				Category_ID:  null,
				Sub_Category_ID:  null,
				Desecription:  '',
				Keywords:  [],
				Img_URL:  '',
				**/

			//}
		]

	}
}


//make the http GET request to BlueCart API
axios.get('https://api.bluecartapi.com/request', { params })
.then(response => {
     //print the JSON response from BlueCart APiI
    var finaldata = JSON.stringify(response.data, 0, 2);
    fs.writeFile(params.search_term + ".json", JSON.stringify(response.data,0,2) , function (err, file) {
        if (err) console.log(err);

    });




    console.log(JSON.stringify(response.data, 0, 2));




  })
  .catch(error => {
   //catch and print the error
  console.log(error);
  })


 
for(i = 0; i < data.search_results.length; i++){
	template.Store.Products.push({
		UPC: data.search_results[i].product.item_id,
		Name: data.search_results[i].product.title,
		Price: data.search_results[i].offers.primary.price,
		//Category_ID: 
		//Sub_Category_ID:
		Description: data.search_results[i].product.title,
		//Keywords: 
		Img_URL: data.search_results[i].product.main_image,
	});


}
console.log(template.Store.Products[0]);
toJSON = JSON.stringify(template, 0,1 );
console.log(toJSON);


fs.writeFile(params.search_term + ".json", toJSON, (err) => {
	if (err) console.log(err);
	console.log("File wrriten");


});

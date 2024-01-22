const axios = require('axios');
const fs = require('fs');


let key = null;
fs.readFile('api.env', 'utf8', (err, data) => {
	if(err){
		console.error(err)
	}
	const lines = data.split('\n');
	for (const line of lines){
		if (line.includes("RedCircle")){
			const parts = line.split('" = "');
			if (parts.length == 2){
				key = parts[1].replace(/"/g, '');
				break;

			}
		}


	}

})

// set up the request parameters
const params = {
api_key: "7F36076AFCFB41D8BC6C14D1E7F24641",
  search_term: "laptop",
 // category_id: "5zja3",
  type: "search"
}
const store = '_Target';
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
/**
// make the http GET request to RedCircle API
axios.get('https://api.redcircleapi.com/request', { params })
.then(response => {

    // print the JSON response from RedCircle API
    console.log(JSON.stringify(response.data, 0, 2));

fs.writeFile(
	params.search_term + store +  ".json", 
	JSON.stringify(response.data,0,2) , 
	function (err, file) {
        	if (err) console.log(err);

});





  }).catch(error => {
// catch and print the error
console.log(error);
})

**/

var data = fs.readFileSync('../json_files/lapT.json','utf8', (err, data) =>{
        if (err){
                console.log(err);
                return;

        }

        try{
                //data = JSON.parse(data);

        }
        catch (err) {
                console.log(err);
        }
});
data = JSON.parse(data);
//console.log(data);

for(i = 0; i < data.search_results.length; i++){
        template.Store.Products.push({
                UPC: data.search_results[i].product.tcin,
                Name: data.search_results[i].product.title,
                Price: data.search_results[i].offers.primary.price,
                //Category_ID:
                //Sub_Category_ID:
                Description: data.search_results[i].product.title,
                //Keywords:
                Img_URL: data.search_results[i].product.main_image,
        });


}

toJSON = JSON.stringify(template, 0,1 );
console.log(toJSON);


fs.writeFile(
	params.search_term + store +  ".json", toJSON, (err) => {
        if (err) console.log(err);
        console.log("File wrriten");


});


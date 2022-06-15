const axios = require('axios');

async function request(sub_path){
	
	const url = 'http://13.124.193.201:8844/' + sub_path
	
	try{
	
		const response = await axios.get(url);							
				
		return response.data
	}
	catch(e){

		console.log(e)
	}
}


const array = [{word:'a'}, {word:'b'}, {word:'c'}, {word:'d'}, {word:'e'}]

array.forEach(async (item) => {
  
        const resovle = await request(item.word)

        console.log(resovle)
})

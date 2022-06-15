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

const promise_list = []

array.forEach((item) => {

        const promise = request(item.word)

        promise_list.push(promise)
})

Promise.all(promise_list).then((values) => {

        values.forEach((resolve) => {console.log(resolve)})
})

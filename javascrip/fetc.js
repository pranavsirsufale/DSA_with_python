

const url = 'https://api.freeapi.app/api/v1/ecommerce/profile';
const options = {
  method: 'PATCH',
  headers: {accept: 'application/json', 'content-type': 'application/json'},
  body: '{"countryCode":"+91","firstName":"John","lastName":"Doe","phoneNumber":"9893894838"}'
};



const const_api = async () => {
    const res = await fetch(url,options)
    const data = await res.json()
    console.log(data)

}

const_api()









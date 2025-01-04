const url = 'http://res.cloudinary.com/dgxrvlrzc/image/upload/v1735385894/kf3cu48rf3cftvvtaep4.jpg'


const getUniqeId = (url) => {
const regex = /\/upload\/(?:v\d+\/)?([^\/]+)\.\w+$/;
const match = url.match(regex);
const unique =  match ? match[1] : null;
return unique
}




console.log(getUniqeId(url))
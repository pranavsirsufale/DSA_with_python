//  Q1) 

//? written by me 
/* 
const fetchData = async () => {
    const promise = new Promise((resolve, reject) => {
        let success = true;
        if (success) {
            
        resolve({ name : 'pooja' , messege : "Data Fetched"})
    } else {
        reject("Data Not laoded")
}
})
return promise  
}
setTimeout( async () => {
    try {
        const data = await fetchData()
        console.log("WHOLE DATA : " , data)
        console.log("MESSEGE OF THE DATA :",data.messege)
        console.log("DATA : ", data.name)
        
    } catch (error) {
        console.log(error);
    }
}, 2000);

*/



//? GPT Generated >>>> 
/*
function fetchData() {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        const data = { name : 'Pooja ' };
        resolve(data); // Resolves after 2 seconds
      }, 2000);
    });
  }
  
  fetchData()
    .then((data) => {
      console.log("Fetched data:", data);
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
  
*/


//! Q2>>> Q.2) Write a function parseJSON() that:
//?>>• Takes a JSON string as input.
//?>> • Returns the parsed JavaScript object if the JSON string is valid.
//?>>• If the JSON string is invalid (i.e., it cannot be parsed), catch the error and return the message "Invalid JSON".


const valid_json = JSON.stringify({
    "employees": [
      {
        "id": 1,
        "name": "John Doe",
        "age": 29,
        "department": "Engineering",
        "skills": ["JavaScript", "React", "Node.js"],
        "isFullTime": true
      },
      {
        "id": 2,
        "name": "Jane Smith",
        "age": 34,
        "department": "Marketing",
        "skills": ["SEO", "Content Writing", "Social Media"],
        "isFullTime": false
      },
      {
        "id": 3,
        "name": "Mike Johnson",
        "age": 41,
        "department": "Human Resources",
        "skills": ["Recruitment", "Employee Relations", "Training"],
        "isFullTime": true
      }
    ]
  })

const invalid_json = {
    "employees": [
      {
        id: 1,              // Missing quotes around key
        "name": "John Doe",
        "age": 29,
        "department": "Engineering",
        "skills": ["JavaScript", "React", "Node.js"],
        "isFullTime": true,
      },                    // Trailing comma here
      {
        "id": 2,
        "name": "Jane Smith",
        "age": "34",        // Age should be a number, not a string
        "department": null,
        "skills": "SEO",    // Skills should be an array, not a string
        "isFullTime": false
      }
    ]
  }
  
const json_validator_fun = (jsonData) => {
    try {
        return JSON.parse(jsonData)
    } catch (error) {
        // console.log(error.messege || error);
        return 'Invalid Json'
        
    }
}
console.log( " VALID JSON DATA : " ,json_validator_fun(valid_json))

console.log("INVALID JSON DATA : ", json_validator_fun(invalid_json))




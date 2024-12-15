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


//! Q2>>>Write a function parseJSON() that:
//?>>• Takes a JSON string as input.
//?>> • Returns the parsed JavaScript object if the JSON string is valid.
//?>>• If the JSON string is invalid (i.e., it cannot be parsed), catch the error and return the message "Invalid JSON".



/*
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

*/


// ? Q.3) Write a function reverseString()

/*

let str = "hello JavaScript Developer"
let spt_str = str.split(' ')
const reverse_str = (st) => {
    let new_str = ''
    for( let i = st.length-1 ; i > -1 ; i--){
        new_str += st[i]
    }
    return new_str
}
let reversed_str = []
let to_uppend = ""
let counter = 0 
for(let vlaue of spt_str){
    counter === 0 ? to_uppend += reverse_str(vlaue) : to_uppend += ` ${reverse_str(vlaue)}` 
    counter++
}
console.log(to_uppend)
 */



//? Both the code written by me >>>
/*
let str = "hello JavaScript Developer".split(' ')
console.log(str);
function reverse_str(st){
  let rev_str = ''
  for(let i = st.length -1 ; i > -1 ; i--){
    rev_str += st[i]
  }
  return rev_str
}
let new_empty_array = []
for(let vlaues of str){
  new_empty_array.push(reverse_str(vlaues))
}

console.log(new_empty_array.join(' ',','))


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



    // ? Q. 4) Write an arrow function groupBy() that:


    /*
  const an_array = [
    { "name": "Amit", "age": 25 },{ "name": "Sanjay", "age": 25 },
    { "name": "Rajesh", "age": 30 }, { "name": "Priya", "age": 30 },
    { "name": "Neha", "age": 35 }
    ]


    const groupBy = (array, property) => {
      return array.reduce((acc, obj) => {
        const key = obj[property];
        if (!acc[key]) {
          acc[key] = []; 
        }
        acc[key].push(obj); 
        return acc;
      }, {});
    };
    

    
    // Group by 'age'
    const result = groupBy(an_array, "age");
    console.log(result);

*/





//? Q. 5) Write a JavaScript function createTable() that:



/*
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title> Pooja's Dynamic Table Generator </title>
  <style>
    table {
      border-collapse: collapse;
      width: 100%;
      margin-top: 20px;
    }
    table, th, td {
      border: 1px solid black;
    }
    th, td {
      padding: 8px;
      text-align: center;
    }
    input[type="number"] {
      margin-bottom: 10px;
    }
  </style>
</head>
<body>
  <h1>Dynamic Table Generator</h1>

  <label for="columns">Number of Columns:</label>
  <input type="number" id="columns" min="1" value="3">
  <button onclick="createTable()">Create Table</button>

  <table id="dynamicTable">
    <!-- Table will be dynamically generated here -->
  </table>

  <button onclick="addRow()">Add Row</button>

  <script>
    function createTable() {
      const columnCount = parseInt(document.getElementById("columns").value, 10);
      const table = document.getElementById("dynamicTable");

      // Clear any existing table content
      table.innerHTML = "";

      // Create the initial table with 3 rows
      for (let i = 0; i < 3; i++) {
        const row = table.insertRow();
        for (let j = 0; j < columnCount; j++) {
          const cell = row.insertCell();
          const input = document.createElement("input");
          input.type = "text";
          cell.appendChild(input);
        }
      }
    }

    function addRow() {
      const table = document.getElementById("dynamicTable");
      const columnCount = parseInt(document.getElementById("columns").value, 10);

      // Add a new row
      const row = table.insertRow();
      for (let i = 0; i < columnCount; i++) {
        const cell = row.insertCell();
        const input = document.createElement("input");
        input.type = "text";
        cell.appendChild(input);
      }
    }

    // Create the default table on page load
    window.onload = createTable;
  </script>
</body>
</html>


*/



//? Q.6) Write an arrow function mergeArrays that takes two arrys as input and returns a new array that is the concatenation of both arrays.
/*
const mergeArrays = (arr1,arr2) =>{
  return [...arr1,...arr2]
}
let ar1 = [1,2]
let ar2 = [3,4]
console.log(mergeArrays(ar1,ar2))

*/


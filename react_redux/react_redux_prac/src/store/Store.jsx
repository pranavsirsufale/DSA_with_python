import { createStore, applyMiddleware } from 'redux'
import { composeWithDevTools } from '@redux-devtools/extension'
import { thunk } from 'redux-thunk'


// defined action types
const ADD_TASK = "task/add";
const DELETE_TASK = "task/delete";


// step 1: create reducer 

const initialState = {
  task: [],
};

const taskReducer = (state = initialState, action) => {
  switch (action.type) {
    case ADD_TASK:
      return {
        ...state,
        task: [...state.task, action.payload],
      };

    case DELETE_TASK:
      return {
        ...state,
        task: state.task.filter((item,index) => index !== action.payload),
      };

    default:
      return state;
  }
};


// step 2 : Create the Redux store using the reducer
export const store = createStore(taskReducer, composeWithDevTools(applyMiddleware(thunk)));

console.log(store);


// step 3 : Log the initial state
/* The getState method is a synchronous 
function that returns the current
state of a Redux application . It indludes the 
entire state of the application, including all 
the reducers and their respective states.
*/




// step 4 : Dispatch an action to add a task

console.log("Initial State : ", store.getState());


export const addTask = (data) => {
  return {
       type : ADD_TASK,
       payload : data || 'go to gym' 
   }
}



export const delteteTask = (id=0) => {
   return { type : DELETE_TASK ,payload : id }
}


store.dispatch(addTask("Exercise daily"))
console.log("Initial State : ", store.getState());



// store.dispatch({
//     type : DELETE_TASK,
//     payload : 0
// })
// console.log("Initial State : ", store.getState());

// step 5 : Create action creators 


const line = 'https://jsonplaceholder.typicode.com/todo?_limit=3'


export const fetchTask = () => {
  return async ( dispatch ) => {
    try {
      const res = await fetch(line);

      const task = await res.json();
    } catch (error) {
      
    }
  }
}


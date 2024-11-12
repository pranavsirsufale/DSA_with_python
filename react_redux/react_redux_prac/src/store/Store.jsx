import { createStore } from 'redux'



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
const store = createStore(taskReducer);

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


store.dispatch(addTask())
console.log("Initial State : ", store.getState());



store.dispatch({
    type : DELETE_TASK,
    payload : 0
})
console.log("Initial State : ", store.getState());


const addTask = (data) => {
   return {
        type : ADD_TASK,
        payload : data 
    }
}



const delteteTask = (id) => {
    return { type : ADD_TASK,payload : id }
}


import { createSlice }  from '@reduxjs/toolkit'


const userSlice = createSlice({
        name : "user",
        initialState : [],
        reducers:{
            addUser(state,action){
                state.push(action.payload)
            },
            removeUser(state,action){
                state = state.filter((storeName,index)=>(
                    storeName = action.payload
                    
                ))
                console.log(action.payload);
                
            },
            deleteUsers(state,action){},
        }
    }
)

export default userSlice.reducer;

export const { addUser ,removeUser } = userSlice.actions;

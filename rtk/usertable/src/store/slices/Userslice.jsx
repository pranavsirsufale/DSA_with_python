import { createSlice }  from '@reduxjs/toolkit'


const userSlice = createSlice({
        name : "user",
        initialState : [],
        reducers:{
            addUser(state,action){
                state.push(action.payload)
            },
            removeUser(state,action){
                state.splice(action.payload,1)
            },
            clearUser(state,action){
                return []
            },
        },
        extraReducers(builder){
            builder.addCase(userSlice.actions.clearUser,()=>{
                return [];
            })
        }
    }


)

export default userSlice.reducer;

export const { addUser ,removeUser , clearUser } = userSlice.actions;

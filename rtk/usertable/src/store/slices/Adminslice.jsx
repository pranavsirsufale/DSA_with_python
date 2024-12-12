import { createSlice } from "@reduxjs/toolkit";

const adminSlice = createSlice({
    name : 'admin',
    initialState : [],
    reducers : {
        addAdmin(state,action){
            state.push(action.payload)
        },
        removeAdmin(state,action){
            state.splice(action.payload,1)
        },
        clearAdminData(state,action){
            return [];
        },
    },
    extraReducers(builder){
        builder.addCase(adminSlice.actions.clearAdminData,()=>{
            return [];
        })
    }
})


export default adminSlice.reducer;

export const { addAdmin , removeAdmin } = adminSlice.actions;
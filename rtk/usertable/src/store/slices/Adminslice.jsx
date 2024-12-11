import { createSlice } from "@reduxjs/toolkit";

const adminSlice = createSlice({
    name : 'admin',
    initialState : [],
    reducers : {
        addAdmin(action,payload){},
        removeAdmin(action,payload){},
        clearAdminData(action,payload){
            
        },
    },
    extraReducers(builder){
        builder.addCase(adminSlice.actions.clearAdminData,()=>{
            return [];
        })
    }
})


export default adminSlice.reducer
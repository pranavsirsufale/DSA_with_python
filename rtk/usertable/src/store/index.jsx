import { configureStore } from "@reduxjs/toolkit";
import userSlice from "./slices/Userslice";
const store = configureStore({
    reducer :{
        users : userSlice
    }
})

export default store;

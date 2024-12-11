import { configureStore } from 'react-redux'
import userSlice from "./slices/Userslice";
import adminSlice from './slices/Adminslice'
import reducer from './slices/Userslice';

const store = configureStore({
   reducer : {
    user : userSlice,
    admin : adminSlice
   }
})

export default store




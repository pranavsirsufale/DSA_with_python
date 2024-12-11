import styled from "styled-components"
import { useSelector } from "react-redux"

const DisplayUsrs = () => {

    const data = useSelector((state)=> ( state.users) )
    console.log(data)



  return (
    <div>DisplayUsrs</div>
  )
}

export default DisplayUsrs
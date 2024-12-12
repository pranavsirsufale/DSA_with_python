import styled from 'styled-components';
import { useDispatch , useSelector} from 'react-redux';
import { clearUser } from '../store/actions';
export const DeleteAllUser = () => {

  const dispatch = useDispatch()
  return (
    <Wrapper>
    <button className='btn clear-btn'  onClick={()=>dispatch(clearUser())} >
    Clear All User 
  </button>
  </Wrapper>
  )
}

const Wrapper = styled.section`
.clear-btn{
text-transform : capitalize;
background-color : #db338a;
margin-top: 2rem;
}
`


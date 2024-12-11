import { useState } from 'react'
import Navbar from './components/Navbar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Navbar/>
      <div>
        <h1> Hi there, It's Pranav sirsufale </h1>
       </div>
    </>
  )
}

export default App

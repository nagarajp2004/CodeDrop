import React from 'react'

const Usercards = (props) => {
  return (
    <div>
      <input type='text' onChange={(e)=>props.setname(e.target.value)}/>
      <p>props.name={props.name}</p>
    </div>
  )
}

export default Usercards

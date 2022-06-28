import { useState } from 'react'
import './App.scss'
import axios from "axios"
import settigns from './settings'
import { useEffect } from 'react'

function App() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [fname, setFname] = useState("")
  const [lname, setLname] = useState("")
  const [data, setData] = useState([])

  const get_data = () => {
    axios.get(`${settigns.HOST}/api/users/user/`).then(data=>{
      setData(data.data)
    })
  }

  useEffect(()=>{
    get_data()
  }, [])

  const submitClicked = e => {
    axios.post(`${settigns.HOST}/api/users/user/`, {
      username: username,
      password: password,
      first_name: fname,
      last_name: lname,
    }).then(()=>{
      get_data()
    })
  }

  const delete_row = id => {
    axios.delete(`${settigns.HOST}/api/users/user/${id}`).then(()=>{
      get_data()
    })
  }

  return (
    <div className="App">
      <div className='form'>
        <label for="_username">Username: </label>
        <input id="_username" defaultValue={username} onChange={e=>setUsername(e.target.value)}/>
        <br/>
        <label for="_password">Password: </label>
        <input id="_password" defaultValue={password} onChange={e=>setPassword(e.target.value)}/>
        <br/>
        <label for="_fname">Firstname: </label>
        <input id="_fname" defaultValue={fname} onChange={e=>setFname(e.target.value)}/>
        <br/>
        <label for="_lname">Lastname: </label>
        <input id="_lname" defaultValue={lname} onChange={e=>setLname(e.target.value)}/>
        <br/>
        <button onClick={submitClicked}>Submit</button>
        <br/>
        <br/>
        <table border={1}>
          <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Password</th>
            <th>Firstname</th>
            <th>Lastname</th>
            <th>Operations</th>
          </tr>
          {data.map(item=>{
            return (
              <tr>
                <td>{item.id}</td>
                <td>{item.username}</td>
                <td>{item.password}</td>
                <td>{item.first_name}</td>
                <td>{item.last_name}</td>
                <td><button onClick={e=>delete_row(item.id)}>delete</button></td>
              </tr>
            )
          })}
        </table>
      </div>
    </div>
  )
}

export default App

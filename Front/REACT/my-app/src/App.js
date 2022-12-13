import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {

    const MY_SERVER = "http://127.0.0.1:5000/students/"
    const [city, setCity] = useState("");
    const [sname, setsName] = useState("");
    const [addr, setAddr] = useState("");
    const [pin, setPin] = useState("");
    const [msg, setMsg] = useState("");
    const [students, setStudents] = useState([]);
    const loadData = async() => {
        const res = await axios.get(MY_SERVER)
        setStudents(res.data)
    }
    useEffect(() => {
        loadData()
    }, []);

    const addData = async() => {
        await axios.post(MY_SERVER ,
            {
                city, name:sname, addr, pin
            })
            loadData()
    }
    const delData = async(id) => {
        const temp=await axios.delete(MY_SERVER+id )
        setMsg(temp.data)
        loadData()
    }
    const updData = async(id) => {
        const temp=await axios.put(MY_SERVER+id ,
            {
                city, name:sname, addr, pin
            })
        setMsg(temp.data)
        loadData()
    }

    return (
        <div >
            <h1 style={{color:"red"}}>{msg}</h1>
            city: <input onChange={(e) => setCity(e.target.value)} /><br />
            name: <input onChange={(e) => setsName(e.target.value)} /><br />
            addr: <input onChange={(e) => setAddr(e.target.value)} /><br />
            pin: <input onChange={(e) => setPin(e.target.value)} />
            <button onClick={() => addData()}>ADD</button>
            
            Students: count - {students.length}
            {students.map((stu,i) =><div key={i}>{i+1} -<button onClick={()=>delData(stu.id)}>DEL</button><button onClick={()=>updData(stu.id)}>UPDATE</button> city: {stu.city}, name{stu.name}, addr{stu.addr}, pin{stu.pin},id:{stu.id}</div>)}
        <img src="https://picsum.photos/200/300"></img>
        </div>
    );
}

export default App;


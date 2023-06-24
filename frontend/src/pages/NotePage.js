import React, { useState, useEffect } from 'react'
import { Link, useParams,useNavigate } from 'react-router-dom'
import { ReactComponent as ArrowLeft } from '../assets/arrow-left.svg'


const NotePage = ({ match, history }) => {

    const navigate = useNavigate();
    
    let {id}=useParams()

    let [note, setNote] = useState(null)

    useEffect(() => {
        getNote()
    }, [id])

    let getNote = async () => {
        if (id === 'new') return

        let response = await fetch(`http://localhost:8000/api/notes/${id}/`)
        let data = await response.json()
        setNote(data)
    }

    function createNote() {
        fetch('http://localhost:8000/api/tes/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })
        navigate('/')
    }

    let updateNote = async () => {
        
        fetch(`http://localhost:8000/api/notes/${id}/update/`, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })

    }

    let deleteNote = async () => {
        fetch(`http://localhost:8000/api/notes/${id}/delete/`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        navigate('/')
        
    }
    let handleSubmit = () => {
        console.log('NOTE:', note)
        if (id !== 'new' && note.body == '') {
            deleteNote()
        } else if (id !== 'new') {
            updateNote()
        } else if (id === 'new' && note.body !== null) {
            createNote()
        }
        navigate('/')
        
    }

    let handleChange = (value) => {
        setNote(note => ({ ...note, 'body': value }))
        console.log('Handle Change:', note)
    }

    // function test(){
    //     fetch(`http://localhost:8000/api/tes2`, {
    //         method: 'GET',
    //         headers: {
    //             'Content-Type': 'application/json'
    //         }
    //     }).then(res=>{
    //         res.json().then(data=>{
    //             console.log(data);
    //         })
    //     })
    //     navigate('/')
    // }
    
  return (
    <div className="note" >
        <div className="note-header">
            <h3>
                <ArrowLeft onClick={handleSubmit} />
            </h3>
            {id !== 'new' ? (
                <button onClick={deleteNote}>Delete</button>
            ) : (

                <button onClick={createNote}>Done</button>
                
            )}

        </div>
        <textarea onChange={(e) => { handleChange(e.target.value) }} value={note?.body}></textarea>
    </div>
)
}

export default NotePage

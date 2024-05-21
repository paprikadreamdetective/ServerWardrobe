import React, { useState } from 'react';
import axios from "axios";
import { IonButton, IonInput, IonItem, IonLabel, IonList, IonLoading, IonNote } from '@ionic/react';
import '../components/registeru-component.css'
import { loginUser } from '../firebaseConfig';
//import httpClient from "./httpClient";
import { useHistory } from 'react-router-dom';

// import {toast} from '../toast'
import { error } from 'console';

function Registeru_input() {

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [name, setName] = useState('')
  const [lastname, setLastname] = useState('')
  const [acceso, setAcceso] = useState('');
  const [message, setMessage] = useState('');
  const history = useHistory();
  const [busy, setBusy] = useState<boolean>(false)


  const logInUser = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/register_username', {
        username: username,
        password: password,
        name: name,
        lastname: lastname,
      });
      const data = response.data;
      if (data.success) {
        setMessage(data.message);
        setUsername('')
        setPassword('')
        setName('')
        setLastname('')
        history.push('/landing');
      } else {
        setMessage(data.message);
      }
    } catch (error) {
      setMessage('Error al procesar la solicitud');
    }
  };

  return (
    <>
    {/* <IonLoading message={'Please wait...'} duration={0} isOpen={busy}></IonLoading> */}

    <div className="input-register">
      <IonInput 
        class='custom3' label="Username: " type="text" placeholder="NombreUsuario" value={username}
        onIonChange={(e:any) => setUsername(e.target.value)}
      ></IonInput>
    </div>
    <br/>
    <div className="input-email">
      <IonInput 
        class='custom3' label="Password: " type="password" placeholder="fgud5j89"value={password}
        onIonChange={(e:any) => setPassword(e.target.value)}  
      >
      </IonInput>
    </div>

    <br/>
    <div className="input-name">
    <IonInput 
        class='custom3' label="Name: " type="text" placeholder="Your Name" value={name}
        onIonChange={(e:any) => setName(e.target.value)}  
    ></IonInput>
    </div>

    <br/>

    <div className="input-lastname">
    <IonInput 
        class='custom3' label="Lastname: " type="text" placeholder="Your Lastname" value={lastname}
        onIonChange={(e:any) => setLastname(e.target.value)}  
    ></IonInput>
    </div>

    {/*<IonButton routerLink='/home' className='button-register'> Log In </IonButton>*/}
    <IonButton className='button-register' onClick={logInUser}> Register </IonButton>

    <br/>
    </>
  );
}


export default Registeru_input;

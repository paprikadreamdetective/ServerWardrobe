import React, { useState } from 'react';
import axios from "axios";
import { IonButton, IonInput, IonItem, IonLabel, IonList, IonLoading, IonNote } from '@ionic/react';
import '../components/mail-component.css'
import { loginUser } from '../firebaseConfig';
//import httpClient from "./httpClient";
import { useHistory } from 'react-router-dom';

// import {toast} from '../toast'
import { error } from 'console';

function Email_input() {

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [acceso, setAcceso] = useState('');
  const [message, setMessage] = useState('');
  const history = useHistory();
  const [busy, setBusy] = useState<boolean>(false)


  const logInUser = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/login_email', {
        email: username,
        password: password,
      });
      const data = response.data;
      if (data.success) {
        setMessage(data.message);
        setUsername('')
        setPassword('')
        history.push('/home');
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

    <div className="input-email">
      <IonInput 
        class='custom2' label="Email: " type="email" placeholder="email@domain.com" value={username}
        onIonChange={(e:any) => setUsername(e.target.value)}
      ></IonInput>
    </div>
    <br/>
    
    <div className="input-email">
      <IonInput 
        class='custom2' label="Password: " type="password" placeholder="fgud5j89"value={password}
        onIonChange={(e:any) => setPassword(e.target.value)}  
      >
      </IonInput>
    </div>

    {/*<IonButton routerLink='/home' className='button-register'> Log In </IonButton>*/}
    <IonButton className='button-register' onClick={logInUser}> Log In </IonButton>

    <br/>
    </>
  );
}


export default Email_input;

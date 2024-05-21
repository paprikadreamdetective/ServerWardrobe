import React from 'react';
import { IonButton, IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';
import ExploreContainer from '../components/ExploreContainer';
import './Register_username.css';

import logo from '../assets/wardrobe.svg'
import google from '../assets/google-logo.svg'
import Registeru_input from '../components/register-component';

const Register_username: React.FC = () => {
  return (
    <IonPage>
      {/* <IonHeader>
        <IonToolbar>
          <IonTitle>Welcome to SmartWardrobe</IonTitle>
        </IonToolbar>
      </IonHeader> */}

      <IonContent class='Container'>
        <img className="img-logo" alt='Hola' src={logo} />
        <div className="title-content">
            <h1 className='title-home'>Welcome_u!</h1>
        </div>

        <div className="buttons-container">
            <Registeru_input></Registeru_input>
            
        </div>

        <div className="social-media">
          <h3>Register with Social Media</h3>
          <div className="container-logos">
            <IonButton fill="outline" routerLink='/login' className='social-media'>
              <img className="logo-social" alt='Hola' src={google} />
            </IonButton>
          </div>
        </div>


      </IonContent>
    </IonPage>
  );
};

export default Register_username;
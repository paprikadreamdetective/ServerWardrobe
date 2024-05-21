import React from 'react';
import { IonButton, IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';
import ExploreContainer from '../components/ExploreContainer';
import './Register.css';

import logo from '../assets/wardrobe.svg'
import google from '../assets/google-logo.svg'
import Register_input from '../components/register-component';

const Register: React.FC = () => {
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
            <h1 className='title-home'>Welcome!</h1>
        </div>

        <div className="buttons-container">
            <Register_input></Register_input>
            
        </div>

        <div className="social-media">
          <h3>Register with Social Media</h3>
          <div className="container-logos">
            <IonButton fill="outline" routerLink='/register_username' className='social-media'>
              <img className="logo-social" alt='Hola' src={google} />
            </IonButton>
          </div>
        </div>


      </IonContent>
    </IonPage>
  );
};

export default Register;
import React from 'react';
import { IonButton, IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';
import ExploreContainer from '../components/ExploreContainer';
import './Login.css';
import logo from '../assets/wardrobe.svg'
import google from '../assets/google-logo.svg'


import Email_input from '../components/mail-component';

const Login: React.FC = () => {
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
            <h1 className='title-home'>Welcome Back!</h1>
        </div>

        <div className="buttons-container">
            <Email_input></Email_input>
            
        </div>

        <div className="social-media">
          <h3>Login with Social Media</h3>
          <div className="container-logos">
            <IonButton fill="outline" routerLink='/login_username' className='social-media'>
              <img className="logo-social" alt='Hola' src={google} />
            </IonButton>
          </div>
        </div>


      </IonContent>
    </IonPage>
  );
};

export default Login;
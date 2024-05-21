import React, {useState} from 'react';
//import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar, useIonViewDidEnter } from '@ionic/react';
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar, IonFab, IonFabButton, IonIcon, IonGrid, IonRow, IonCol, IonImg, IonActionSheet } from '@ionic/react';
import { camera, trash, close } from 'ionicons/icons';
import ExploreContainer from '../components/ExploreContainer';
import './Tab2.css';

import { Person } from '../models/person.model'
import cloud_icon from '../assets/cloud.png'
import '../firebaseConfig'
import WebcamCapture from '../components/photoCapture';

import Links  from '../components/Links';


const Tab4: React.FC = () => {
  
  const [people, setPeople] = useState<Person[]>([]);
 
  // useIonViewDidEnter(async () => {

  // })
  
  return (
   
    /*
    <IonPage>
      <IonContent fullscreen>
        <Links></Links>
      </IonContent>
    </IonPage>*/
    
    <IonPage>
      <IonContent fullscreen>
        <WebcamCapture></WebcamCapture>
      </IonContent>
    </IonPage>
  );
};

export default Tab4;

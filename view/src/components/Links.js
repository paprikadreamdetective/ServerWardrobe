import React, {useEffect, useState} from "react";
import LinkForm from '../components/LinkForm';
import { usePhotoGallery, UserPhoto } from './photoCapture';
import { db } from "../firebaseConfig";

const Links = () => {

    const [ropa, setRopa] = useState([]);
    
    const addOrEdit = async (object) => {
        await db.collection('ropa').doc().set(object)
        console.log('prenda agregada')
    }

    const getData = async () => {
        db.collection('ropa').onSnapshot((querySnapshot) => {
            const docs = [];
            querySnapshot.forEach(doc =>{
                // console.log(doc.data());
                // console.log(doc.id);
                docs.push({...doc.data(), id:doc.id});
            });
            setRopa(docs);
            console.log(docs)
        });
    }

    useEffect(() => {
        getData();
    }, []);

    return (
        <>
        {/*<LinkForm addOrEdit={addOrEdit}></LinkForm>*/}
        
        </>
    )
}

export default Links;
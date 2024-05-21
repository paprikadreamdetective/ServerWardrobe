import React, {useState, useEffect} from "react";
import PropTypes from 'prop-types';
import { uploadFile } from "../firebaseConfig";
import { IonInput, IonItem, IonList } from "@ionic/react";
import './LinkForm.css'
import axios from 'axios';



// import removeBg from "remove.bg";


// API key: aTG5BZzJ7Y7FnXVYxTxPHvyg

const LinkForm = (props) => {
    // const apiKey = 'aTG5BZzJ7Y7FnXVYxTxPHvyg'

    const initialValues = {
        tipo: '',
        clima: '',
        color: '',
        categoria: '',
        url: ''
    }

    const [file, setFile] = useState(null);
    const [values, setValues] = useState(initialValues);


    const handleInputChange = e => {
        const {name, value} = e.target;
        setValues({...values, [name]: value})
        
    }
    

    const handleSubmit = async (e) => {
        e.preventDefault();
        

        if (!file) {
        alert('Select a file first');
        return;
        }
    
        const formData = new FormData();
        
        formData.append('file', file);
        console.log('Variable formData: \n'+ formData)
    
        try {
        const response = await fetch('http://127.0.0.1:5000/user/upload', {
            method: 'POST',
            body: formData,
        });
    
        const result = await response.text();
        const resultObject = JSON.parse(result)
        console.log('Valor de url = ' + resultObject.image_url)
        console.log('Tipo de dato de url = ', typeof resultObject.image_url)
        setValues({...values, url: resultObject.image_url})
        console.log('Valores del formulario final: \n', values)
        // console.log('resultObject = ', resultObject);
        } catch (error) {
        console.error('Error uploading file:', error);
        }


    };


    useEffect(() => {
        if (values.url !== '') {
            props.addOrEdit(values);
            setValues({...initialValues});
        }
    }, [values]);

    return(
        <>
        <div className="content-inputs">
            <section className="form-register">
                <h4>Añadir Prenda</h4>

                <input className="controls" type="text" name="tipo" placeholder="Tipo" onChange={handleInputChange} value={values.tipo}></input>
                <input className="controls" type="text" name="clima" placeholder="Clima" onChange={handleInputChange} value={values.clima}></input>
                <input className="controls" type="text" name="color" placeholder="Color" onChange={handleInputChange} value={values.color}></input>
                <input className="controls" type="text" name="categoria" placeholder="Categoria" onChange={handleInputChange} value={values.categoria}></input>
                <input className="image-inputs" type="file" name="image" onChange={e => setFile(e.target.files[0])}></input>

                {/* <input type="file" name="image" onChange={async (e) => {const res = await uploadFile(e.target.files[0]); console.log('AL cargar:',res)}} value={values.url}></input> */}

                <button className="botons" onClick={handleSubmit}>Save</button>
            </section>
        </div>
        </>
    )
}

LinkForm.propTypes = {
    addOrEdit: PropTypes.func.isRequired,
};

export default LinkForm;

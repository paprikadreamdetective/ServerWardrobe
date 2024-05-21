/*
import React, {useState, useEffect} from "react";
import Carousel from "react-multi-carousel";
import fs from 'fs'; 
import cloud_icon from '../assets/cloud.png'
import { db } from "../firebaseConfig";

import "react-multi-carousel/lib/styles.css";

import './carruselPrendas.css'


import PropTypes from 'prop-types';

const CarruselPrendas = ({ categoria }) => {
    const responsive = {
        superLargeDesktop: {
         
          breakpoint: { max: 4000, min: 3000 },
          items: 5
        },
        desktop: {
          breakpoint: { max: 3000, min: 1024 },
          items: 3
        },
        tablet: {
          breakpoint: { max: 1024, min: 464 },
          items: 2
        },
        mobile: {
          breakpoint: { max: 390, min: 0 },
          items: 3
        }
      };

      const [ropa, setRopa] = useState([]);

      const getData = async () => {
        console.log('La categoria a buscar es = '+categoria)
        db.collection('ropa').where('categoria', '==', categoria)
        .onSnapshot((querySnapshot) => {
            const docs = [];
            querySnapshot.forEach(doc =>{
                
                docs.push({...doc.data(), id:doc.id});
            });
            setRopa(docs);
            console.log(docs)
        });
      }

    useEffect(() => {
      getData();
    }, []);

    return(
        <>
        <div className="carruselApp">
          <Carousel responsive={responsive}>
            {
              ropa.map((r,index) => {
                return (
                  <>
                    <div className="card">
                       
                        {console.log('Url de la imagen: ' + r.url)}
                        <img src={r.url} alt="" />
                
                    </div>
                  </>
                )
              })
            }
          </Carousel>
        </div>
        </>
    )
}

export default CarruselPrendas;

CarruselPrendas.propTypes = {
  categoria: PropTypes.string.isRequired,
};*/
import React, { useState, useEffect } from "react";
import Carousel from "react-multi-carousel";
import "react-multi-carousel/lib/styles.css";
import PropTypes from 'prop-types';

const CarruselPrendas = ({ categoria }) => {
    const responsive = {
        superLargeDesktop: {
            breakpoint: { max: 4000, min: 3000 },
            items: 5
        },
        desktop: {
            breakpoint: { max: 3000, min: 1024 },
            items: 3
        },
        tablet: {
            breakpoint: { max: 1024, min: 464 },
            items: 2
        },
        mobile: {
            breakpoint: { max: 50, min: 0 },
            items: 1
        }
    };

    const [ropa, setRopa] = useState([]);

    const getData = () => {
        const imagenesList = [];
        const imagenesDir = require.context('./outputs', true, /\.(jpg|png)$/);
        const files = imagenesDir.keys();

        files.forEach(file => {
            imagenesList.push({ url: imagenesDir(file) });
        });

        setRopa(imagenesList);
    }

    useEffect(() => {
        getData();
    }, []);

    return (
        <div className="carruselApp">
            <Carousel responsive={responsive}>
                {ropa.map((imagen, index) => (
                    <div className="card" key={index}>
                        <img src={imagen.url} alt={`Prenda ${index}`} />
                    </div>
                ))}
            </Carousel>
        </div>
    );
}

CarruselPrendas.propTypes = {
    categoria: PropTypes.string.isRequired,
};

export default CarruselPrendas;

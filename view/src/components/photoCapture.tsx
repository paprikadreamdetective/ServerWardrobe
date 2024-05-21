/*
import React, { useCallback, useRef, useState } from 'react';
import Webcam from "react-webcam";

function WebcamCapture() {
  const webcamRef = useRef<Webcam>(null);
  const [imgSrc, setImgSrc] = useState<string | null>(null); // initialize it

  // create a capture function
  const capture = useCallback(() => {
    if (webcamRef.current) {
      const imageSrc = webcamRef.current.getScreenshot();
      setImgSrc(imageSrc);
    }
  }, [webcamRef]);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      {imgSrc === null? (
        <>
        <Webcam height={350} width={350} ref={webcamRef} style={{ marginBottom: '10px' }}/>
        <button style={{ marginTop: '10px', padding: '10px 20px', fontSize: '16px', backgroundColor: '#007bff', color: '#fff', border: 'none', borderRadius: '5px', cursor: 'pointer' }} onClick={capture}>Capture photo</button>
        </>
        ) : (
        <>
        <img  src={imgSrc} alt="webcam" style={{ marginTop: '40px', borderRadius: '5px' }}/>
        <br/>
        <button style={{ marginTop: '10px', padding: '10px 20px', fontSize: '16px', backgroundColor: '#007bff', color: '#fff', border: 'none', borderRadius: '5px', cursor: 'pointer' }} onClick={() => setImgSrc(null)}>Recapture</button>
        </>
      )}
    </div>
  );
}

export default WebcamCapture;*/
/*
import React, { useCallback, useRef, useState } from 'react';
import Webcam from "react-webcam";

function WebcamCapture() {
  const webcamRef = useRef<Webcam>(null);
  const [imgSrc, setImgSrc] = useState<string | null>(null); // initialize it

  // create a capture function
  const capture = useCallback(() => {
    if (webcamRef.current) {
      const imageSrc = webcamRef.current.getScreenshot();
      setImgSrc(imageSrc);
    }
  }, [webcamRef]);

  // Función para enviar la imagen al servidor
  const sendToServer = (imageSrc: string) => {
    fetch('http://localhost:5000/upload', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ image: imageSrc })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
  };


  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      {imgSrc === null? (
        <>
        <Webcam height={350} width={350} ref={webcamRef} style={{ marginBottom: '10px' }}/>
        <button style={{ marginTop: '10px', padding: '10px 20px', fontSize: '16px', backgroundColor: '#007bff', color: '#fff', border: 'none', borderRadius: '5px', cursor: 'pointer' }} onClick={capture}>Capture photo</button>
        </>
        ) : (
        <>
        <img  src={imgSrc} alt="webcam" style={{ marginTop: '40px', borderRadius: '5px' }}/>
        <br/>
        <button style={{ marginTop: '10px', padding: '10px 20px', fontSize: '16px', backgroundColor: '#007bff', color: '#fff', border: 'none', borderRadius: '5px', cursor: 'pointer' }} onClick={() => setImgSrc(null)}>Recapture</button>
        </>
      )}
    </div>
  );
}

export default WebcamCapture;*/
import React, { useCallback, useRef, useState } from 'react';
import Webcam from "react-webcam";

function WebcamCapture() {
  const webcamRef = useRef<Webcam>(null);
  const [imgSrc, setImgSrc] = useState<string | null>(null);

  // Función para capturar la imagen
  const capture = useCallback(() => {
    if (webcamRef.current) {
      const imageSrc = webcamRef.current.getScreenshot();
      setImgSrc(imageSrc);
      if (imageSrc) {
        sendToServer(imageSrc);
      }
    }
  }, [webcamRef]);

  // Convertir base64 a Blob
  const base64ToBlob = (base64: string) => {
    const byteString = atob(base64.split(',')[1]);
    const mimeString = base64.split(',')[0].split(':')[1].split(';')[0];
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
      ia[i] = byteString.charCodeAt(i);
    }
    return new Blob([ab], { type: mimeString });
  };

  // Función para enviar la imagen al servidor
  const sendToServer = (imageSrc: string) => {
    const blob = base64ToBlob(imageSrc);
    const formData = new FormData();
    formData.append('file', blob, 'captured_image.jpg');

    fetch('http://localhost:5000/upload_picture', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      {imgSrc === null? (
        <>
        <Webcam height={350} width={350} ref={webcamRef} style={{ marginBottom: '10px' }}/>
        <button style={{ marginTop: '10px', padding: '10px 20px', fontSize: '16px', backgroundColor: '#007bff', color: '#fff', border: 'none', borderRadius: '5px', cursor: 'pointer' }} onClick={capture}>Capture photo</button>
        </>
      ) : (
        <>
        <img src={imgSrc} alt="webcam" style={{ marginTop: '40px', borderRadius: '5px' }}/>
        <br/>
        <button style={{ marginTop: '10px', padding: '10px 20px', fontSize: '16px', backgroundColor: '#007bff', color: '#fff', border: 'none', borderRadius: '5px', cursor: 'pointer' }} onClick={() => setImgSrc(null)}>Recapture</button>
        </>
      )}
    </div>
  );
}

export default WebcamCapture;
// DropZone.js

import React from 'react';
import { useDrop } from 'react-dnd';
import PropTypes from 'prop-types';
const DropZone = ({ onDrop }) => {
    const [{ isOver }, drop] = useDrop(() => ({
        accept: 'item',
        drop: (item) => onDrop(item),
        collect: (monitor) => ({
            isOver: monitor.isOver(),
        }),
    }));

    return (
        <div
            ref={drop}
            style={{
                border: `1px dashed ${isOver ? 'green' : 'black'}`,
                padding: '10px',
            }}>
            Drop here
        </div>
    );
};

DropZone.propTypes = {
    onDrop: PropTypes.string.isRequired,
  };
export default DropZone;
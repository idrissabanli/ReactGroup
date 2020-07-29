import React from 'react'

function Button(props) {
    const btnText = props.btnText;
    return (
        <button className="btn btn-primary">{btnText}</button>
    )
}

export default Button;

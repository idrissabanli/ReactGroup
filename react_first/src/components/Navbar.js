import React from 'react';
import Button from './Button';
import { Link } from 'react-router-dom';

function Navbar(props) {
    const btnText = props.isAuth ? 'Log Out' : 'Sing in';
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav mr-auto">
                <li className="nav-item active">
                    <Link className="nav-link" to='/' > Home <span className="sr-only">(current)</span></Link>
                </li>
                <li className="nav-item active">
                    <Link className="nav-link" to='/add' > Add Product <span className="sr-only">(current)</span></Link>
                </li>
                <li className="nav-item active">
                    <Link className="nav-link" to='/contact' > Contact <span className="sr-only">(current)</span></Link>
                </li>
                
                </ul>
                <div>
                    <Button btnText={btnText}/>
                </div>
            </div>
        </nav>
    );
  }
  
export default Navbar;
import React, {Component} from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/Navbar';
import Contact from './components/Contact';
import Products from './components/Products';

class App extends Component {
  
  removeProduct = (product_id) => {
    this.setState({
      products: this.state.products.filter(product => { return product.id !== product_id })
    });
  }

  render(){
      const isAuthenticated = false;
      
      return (
        <div className="App">
          <Navbar isAuth={isAuthenticated}/>
          <div className="container">
            <h1 style={{ color: 'red' }} className="text-center">Hello World!</h1>
            <Products />
            <Contact/>
          </div>
        </div>
      );
  }
}

export default App;

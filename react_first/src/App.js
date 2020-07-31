import React, {Component} from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/Navbar';
import Contact from './components/Contact';
import Products from './components/Products';
import AddProduct from './components/AddProduct';

import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import NotFound from './pages/NotFound';

class App extends Component {

  constructor(props){
      super(props);
      console.log('inside constructor')
  }
  componentDidMount(){
      console.log('inside componentDidMount');
  }

  
  removeProduct = (product_id) => {
    this.setState({
      products: this.state.products.filter(product => { return product.id !== product_id })
    });
  }

  render(){
    console.log('inside render method');
      const isAuthenticated = false;
      
      return (
        <div className="App">
          <Router>
            <Navbar isAuth={isAuthenticated}/>
            <div className="container">
            <Switch>
              <Route exact path='/' component={Products}/>
              <Route exact path='/add' component={AddProduct}/>
              <Route exact path='/contact' component={Contact}/>
              <Route component={NotFound}/>
            </Switch>
            </div>
          </Router>
        </div>
      );
  }
}

export default App;

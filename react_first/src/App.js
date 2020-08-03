import React, {Component} from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/Navbar';
import Contact from './components/Contact';
import Products from './components/Products';
import AddProduct from './components/AddProduct';
import ProductDetail from './components/ProductDetail';

import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";
import NotFound from './pages/NotFound';
import UpdateProduct from './components/UpdateProduct';

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
              <Route exact path='/detail/:id' component={ProductDetail}/>
              <Route exact path='/edit/:id' component={UpdateProduct}/>
              <Route component={NotFound}/>
            </Switch>
            </div>
          </Router>
        </div>
      );
  }
}

export default App;

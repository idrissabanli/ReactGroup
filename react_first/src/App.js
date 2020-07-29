import React, {Component} from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/Navbar';
import Contact from './components/Contact';
import Products from './components/Products';

class App extends Component {
  state = {
    products : [
      {
        id: 1,
        title: 'IPhone 7',
        image: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone11-purple-select-2019?wid=940&hei=1112&fmt=png-alpha&qlt=80&.v=1566960958082',
        description: 'IPhone 7 desc'
      },
      {
        id: 2,
        title: 'IPhone 8',
        image: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone11-purple-select-2019?wid=940&hei=1112&fmt=png-alpha&qlt=80&.v=1566960958082',
        description: 'IPhone 8 desc'
      },
      {
        id: 3,
        title: 'IPhone 10',
        image: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone11-purple-select-2019?wid=940&hei=1112&fmt=png-alpha&qlt=80&.v=1566960958082',
        description: 'IPhone 10 desc'
      },
      {
        id: 4,
        title: 'IPhone 11',
        image: 'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone11-purple-select-2019?wid=940&hei=1112&fmt=png-alpha&qlt=80&.v=1566960958082',
        description: 'IPhone 11 desc'
      },
    ]
  }  

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
            <Products products={this.state.products} removeProduct={this.removeProduct} />
            <Contact/>
          </div>
        </div>
      );
  }
}

export default App;

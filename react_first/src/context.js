import React from "react";
import axios from 'axios';

const Context = React.createContext();

const reducer = (state, action) => {
    switch (action.type) {
        case "DELETE" : return { 
            ...state,
            products: state.products.filter(product => { return product.id !== action.payload }) 
        };
        case "ADD_PRODUCT" : return { 
          ...state,
          products: [...state.products, action.payload]
      };
      case "UPDATE_PRODUCT" : return { 
        ...state,
        products: [...state.products.map(product=> { return product.id === action.payload.id ? action.payload : product }) ]
    };
        default: return state;
    }
};

export class ProductProvider extends React.Component {
    
    state = {
        products : [],
        dispatch: action => {
            this.setState(state => reducer(state, action));
        },
      }
    
    componentDidMount = async () =>{
      const response = await axios.get('http://localhost:8000/api/products/');
      console.log(response);
      this.setState({
        ...this.state,
        products: response.data
      })
    }
    
    render() {
      const { children } = this.props;
      return ( 
        <Context.Provider value={this.state}>
          {children}
        </Context.Provider>
      );
    }
  }
  
export const ProductConsumer = Context.Consumer;
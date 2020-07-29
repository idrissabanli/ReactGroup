import React from "react";

const Context = React.createContext();

const reducer = (state, action) => {
    switch (action.type) {
        case "DELETE" : return { 
            ...state,
            products: state.products.filter(product => { return product.id !== action.payload }) 
        };
        default: return state;
    }
};

export class ProductProvider extends React.Component {
    
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
        ],
        dispatch: action => {
            this.setState(state => reducer(state, action));
        },
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
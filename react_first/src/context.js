import React from "react";

const Context = React.createContext();

export class ProductProvider extends React.Component {

    state = { isADuck: false };
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
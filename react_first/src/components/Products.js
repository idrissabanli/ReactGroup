import React, { Component } from 'react';
import Product from './Product'

class Products extends Component {
    render() {
        const {products, removeProduct} = this.props;

        return (
            <div className="row">
                {
                    products.map(product => {
                        return (
                            <Product removeProduct={removeProduct} key={product.id} {...product} />
                        )
                    })
                }
                
                
            </div>
        )
    }
}

export default Products;

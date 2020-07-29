import React, { Component } from 'react';
import Product from './Product';
import {ProductConsumer} from '../context';

class Products extends Component {
    render() {
        return (
            <ProductConsumer>
                {
                    value => {
                        const {products} = value;
                        return (
                            <div className="row">
                                {
                                    products.map(product => {
                                        return (
                                            <Product key={product.id} {...product} />
                                        )
                                    })
                                }
                            </div>
                        )
                    }
                }
            </ProductConsumer>
        )

        
    }
}

export default Products;

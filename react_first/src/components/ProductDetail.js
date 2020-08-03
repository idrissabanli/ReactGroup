import React, { Component } from 'react';
import axios from 'axios';

class ProductDetail extends Component {
    state = {
        name: '',
        price: '',
        image: '',
    }

    componentDidMount = async () => {
        const {id} = this.props.match.params;
        const response = await axios.get(`http://localhost:8000/api/products/${id}/`)
        const {name, price, image} = response.data;
        this.setState({
            name,
            price,
            image,
        });
    }
    render() {
        const {name, price, image} = this.state;
        return (
            <div className="card mb-3">
            <img src={image} className="card-img-top" />
            <div className="card-body">
                <h5 className="card-title">{name}</h5>
                <p className="card-text">Price: {price} </p>
    
            </div>
            </div>
        )
    }
}

export default ProductDetail

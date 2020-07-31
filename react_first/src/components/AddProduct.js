import React, { Component } from 'react';
import axios from 'axios';
import {ProductConsumer} from '../context'

class AddProduct extends Component {
    state = {
        name:"",
        price: "",
        image: null
    }
    inputChange = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        });
    }
    imageInputChange = (e) => {
        this.setState({
            [e.target.name]: e.target.files[0]
        });
    }
    createProduct = async (dispatch, e) => {
        e.preventDefault();
        const form = new FormData();
        for(var i in this.state){
            form.append(i, this.state[i]);
        }
        const response = await axios.post('http://localhost:8000/api/products/', form, 
            { headers:
                {'Content-Type': 'multipart/form-data' },
            }
        );
        if (response.status == 201){
            dispatch({type:"ADD_PRODUCT", payload:response.data});
            this.props.history.push('/');
        }
    }


    render() {
        const {name, price} = this.state;
        
        return (
            <ProductConsumer>
                {
                    value => {
                        const {dispatch} = value;
                        return (
           
                            <div>
                                <form onSubmit={this.createProduct.bind(this, dispatch)} method="POST" encType="multipart/form-data">
                                    <div className="form-group">
                                        <label htmlFor="">Name</label>
                                        <input type="text" className="form-control" value={name} name="name" onChange={this.inputChange} placeholder="Enter the name"/>
                                    </div>
                                    <div className="form-group">
                                        <label htmlFor="">Price</label>
                                        <input type="number" className="form-control" value={price} name="price" onChange={this.inputChange} placeholder="Enter the price"/>
                                    </div>
                                    <div className="form-group">
                                        <label htmlFor="">Image</label>
                                        <input type="file" className="form-control" onChange={this.imageInputChange} name="image"/>
                                    </div>
                                    <input type="submit" className="btn btn-primary" value="Create" />
                
                                </form>
                            </div>
                        )
                    }
                }
            </ProductConsumer>
        )

        
    }
}

export default AddProduct;

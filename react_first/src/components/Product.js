import React, { Component } from 'react'
import PropTypes from 'prop-types';
import {ProductConsumer} from '../context';
import axios from 'axios';

class Product extends Component {
    state = {
        isVisable: true
    }

    changeVisable() {
        this.setState({
            isVisable: !this.state.isVisable,
        })
    }
    deleteProduct  = async (dispatch) => {
        const {id} = this.props;
        const response = await axios.delete(`http://localhost:8000/api/products/${id}/`);
        if (response.status==204){
            dispatch({type:"DELETE", payload:id});
        }
    }

    componentDidUpdate(){
        console.log('inside componentDidUpdate');
    }

    
    render() {
        const {name, image, price} = this.props;
        const visibility = this.state.isVisable ? "visible" : "invisible" 
        return (
            <ProductConsumer>
                {
                    value => {
                        const {dispatch} = value;
                        return (
                                <div className="col-3 mb-5">
                                    <div className="card">
                                        <img className="card-img-top" src={image} alt="Card image cap"/>
                                        <div className="card-body">
                                            <h5 className="card-title">{name}</h5>
                                                
                                            <p className={"card-text " + visibility }>{price}</p>
                                            
                                            <div className="d-flex justify-content-between">
                                                <a href="#" className="btn btn-primary">Go</a>
                                                <button onClick={this.changeVisable.bind(this)} className="btn btn-warning">{ this.state.isVisable ? "Hide" : "Show" }</button>
                                                <button onClick={this.deleteProduct.bind(this, dispatch)} className="btn btn-danger">Delete</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            )
                    }
                }
            </ProductConsumer>
        )
        // return (
        //     <div className="col-3">
        //         <div className="card">
        //             <img className="card-img-top" src={image} alt="Card image cap"/>
        //             <div className="card-body">
        //                 <h5 className="card-title">{title}</h5>
                            
        //                 <p className={"card-text " + visibility }>{description}</p>
                        
        //                 <div className="d-flex justify-content-between">
        //                     <a href="#" className="btn btn-primary">Go</a>
        //                     <button onClick={this.changeVisable.bind(this)} className="btn btn-warning">{ this.state.isVisable ? "Hide" : "Show" }</button>
        //                     <button onClick={this.deleteProduct} className="btn btn-danger">Delete</button>
        //                 </div>
        //             </div>
        //         </div>
        //     </div>
        // )
    }
}

Product.propTypes = {
    name: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired, 
    price: PropTypes.string
}

Product.defaultProps = {
    price: 'No information'
}


export default Product;

import React, { Component } from 'react';
import Button from './Button'

class Contact extends Component {
    render() {
        return (
            <div>
                <form>
                    <div className="form-group">
                        <label htmlFor="">Full Name</label>
                        <input className="form-control" name="full_name"/>
                    </div>
                    <div className="form-group">
                        <label htmlFor="">Email</label>
                        <input className="form-control" name="email"/>
                    </div>
                    <div className="form-group">
                        <label htmlFor="">Subject</label>
                        <input className="form-control" name="subject"/>
                    </div>
                    <div className="form-group">
                        <label htmlFor="">Message</label>
                        <input className="form-control" name="message"/>
                    </div>
                <Button btnText="Gonder"/>

            </form>
            </div>
        )
    }
}

export default Contact;

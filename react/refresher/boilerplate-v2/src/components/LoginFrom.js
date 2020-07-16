import React from 'react';
import {connect} from 'react-redux';
import {startLogin} from '../actions/auth';

class LoginForm extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            username: this.props.username,
        }
    }

    onSubmit = (e) => {
        e.preventDefault();
        this.props.dispatch(startLogin());
    }

    render() {
        return (
            <div className="box-layout">
                <form onSubmit={this.onSubmit}>

                    <div className="box-layout__box">
                        <h1 className="box-layout__titile">Boilerplate App</h1>
                        <p>Tag line for app</p>
                        <button className="button">Login with Google</button>
                    </div>
                    
                </form>
            </div>
        );
    }
}

export default connect()(LoginForm);
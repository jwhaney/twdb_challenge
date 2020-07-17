import {Link} from 'react-router-dom'

import React from 'react'


const Navbar = () => {
    return (
        <div className={'navbar'}>
            <Link to={'/'}>Email Addresses</Link>
            <Link to={'/domains'}>Domains</Link>
        </div>
    )
}

export default Navbar
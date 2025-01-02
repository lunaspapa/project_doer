import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { login } from '../../Store/session';
import LogoutButton from './LogoutButton';

const Nav = () => {
  const dispatch = useDispatch();

  const userID = useSelector(state => state.session.user?.id);

  const handleDemoLogin = async (e) => {
    e.preventDefault();
    await dispatch(login('demo@doer.com', 'password'))
  }

  return (
    <div className='reach_nav_container'>
      {!userID && (
        <nav className='unauth_nav'>
          <div className='login_signup_container'>
            <NavLink to='/login' exact={true} activeClassName='active'>
              Login
            </NavLink>
            <NavLink to='/signup' exact={true} activeCLassName='active'>
              Sign Up
            </NavLink>
          </div>
          <button className='demo_login' onClick={handleDemoLogin}>Demo Login</button>
        </nav>
      )}
      {userID && (
        <nav className='user_nav'>
          <p>User Logged In</p>
          <LogoutButton />
        </nav>
      )}
    </div>
  )
};

export default Nav;

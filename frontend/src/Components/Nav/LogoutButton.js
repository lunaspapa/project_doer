import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../Store/session";

const LogoutButton = () => {
  const dispatch = useDispatch();
  const onLogout = async (e) => {
    await dispatch(logout());
  }
  return <button className="logout_button" onClick={onLogout}>Logout</button>
};

export default LogoutButton;

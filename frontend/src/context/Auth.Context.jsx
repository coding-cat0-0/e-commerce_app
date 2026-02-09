import { createContext, useState,  useEffect} from "react";
import useJwt from "react-jwt";
import PropTypes from "prop-types";
import { set } from "react-hook-form";


export const AuthContext = createContext({
    isLoggedIn: false,
    setLoggedIn: () => {},

}
);


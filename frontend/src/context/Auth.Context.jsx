import { createContext, useState,  useEffect, use} from "react";
import useJwt from "react-jwt";
import PropTypes from "prop-types";
import { set } from "react-hook-form";


export const AuthContext = createContext({
    isLoggedIn: false,
    setLoggedIn: () => {},

}
);
export default function AuthContextProvider({ children }) {
    const [isLoggedIn, setLoggedIn] = useState(false);
    const token = localStorage.getItem("token");
    const[decodedToken, isExpired] = useJwt(token);
     useEffect(() => {
        if (token && !isExpired) {
            setLoggedIn(true);
        } else {
            setLoggedIn(false);
        }

}, [decodedToken, isExpired]);
const value = {
    isLoggedIn,
    setLoggedIn,
};
return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
AuthContextProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

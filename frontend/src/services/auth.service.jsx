import axios from 'axios';
import jwt from 'jwt-decode';
import { AuthContext } from '../context/Auth.Context'; 

class AuthService {
      login(email, password) {
        return axios
        .post("api_name",{
            email,
            password
                }).then(response => {
                    if(response.data.access_token){
                        localStorage.setItem('token', JSON.stringify(response.data));
                      }
                    return response.data 
                });
      }
        logout(){
          localStorage.removeItem('token')
        }

  register(name, email, password){
          return axios.post("signup_api", {
            name,
            email,
            password
          });

}

 getAuthUser=()=>{
    const tokenData = localStorage.getItem('token');
      if (!tokenData) return null;
        try
          {
            const token = JSON.parse(tokenData).access_token;
            const decoded = jwtDecode(token);
            return {
                id: decoded.id || decoded.sub,
                role: decoded.role
            }

          }
          catch(error){
              console.error("Error decoding token:", error);
              return null;
          }
    }

isAdmin=()=>{getAuthUser()?.role==='admin'}
isSeller=()=>{getAuthUser()?.role==='seller'}
isUser=()=>{getAuthUser()?.role==='user'}

authHeader() {
  const tokenData = localStorage.getItem('token');
  if (!tokenData) return {};

  const token = JSON.parse(tokenData);
  
  // Check if the token exists. Note: 'access_token' must match your storage key
  if (token && token.access_token) {
    return { 'x-access-token': token.access_token };
  }
  return {};
}

}
export default new AuthService();
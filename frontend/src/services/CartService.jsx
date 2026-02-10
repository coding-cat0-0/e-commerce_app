import axios from "axios";
import authService from "../services/auth.service";
import { AuthContext } from "../context/Auth.Context";

class CartService{
    addToCart(productId,cartDetails){
        return axios.post(`GQL_URL`, {
            query: `
                mutation AddToCart($productId: ID!, $cartDetails: CartInput!) {
                    addToCart(productId: $productId, data: $cartDetails) {
                        id
                        price
                        tax
                        total_price
                    }
        }`,
            variables: {
                productId: productId,
                cartDetails: cartDetails
            }
        }, {
            headers: { 'Authorization': authService.authHeader()}
        });
    }
    
}
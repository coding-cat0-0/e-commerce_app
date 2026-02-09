import axios from "axios"

import { authHeader } from "./auth.service.jsx";    

class QueryService{

        serachProductsbyFilter(filterData){
        return axios.post(`GQL_URL`, {
            query: `
            query filterProducts($filterData:filterInput!){
            filterProducts(data:$filterData){
                id
                }
                }
                `, variables:{
                    filterData:filterData
                }
                }, {

                    headers: { 'Authorization': authHeader()}
                });
    
    }   

        searchProductsbyType(prodType){
        return axios.post(`GQL_URL`, {
            query: `
            query searchForProducts($prodType:String!){
            searchForProducts(prodType:$prodType){
                id
                }
                }
                `, variables:{
                    prodType:prodType
                }
                }, {
                    headers: { 'Authorization': authHeader()}
                });
    }

}

export default new QueryService();
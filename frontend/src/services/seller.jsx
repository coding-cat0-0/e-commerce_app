import axios from 'axios';
import authService from './auth.service';

class SellerService {
    flag = false;
 // Helper method to check user role based on the flag   
getRole(flag){
    if(flag === true){
    user = authService.getAuthUser();
    if(user?.role !=='seller' && user?.role !=='admin'){
        throw new Error("Unauthorized access");
    }
}else{
    if(user?.role !=='seller'){
        throw new Error("Unauthorized access");

        }
    }
}

// Helper method to get user ID from token
getId(){
    return authService.getAuthUser()?.id;
}

// Helper method to get auth header
getAuthHeader(){
    return authService.authHeader();
}

    async uploadProduct(imageFile, prodData) {
        this.flag = false;
        this.getRole(this.flag);
        // Convert image to base64 if present
        let imageBase64 = null;
        if (imageFile) {
            imageBase64 = await new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onload = () => resolve(reader.result.split(',')[1]);
                reader.onerror = reject;
                reader.readAsDataURL(imageFile);
            });
        }
        return axios.post(GQL_URL, {
            query: `
                mutation UploadProduct($data: ProductInput!) {
                    uploadProduct(data: $data) {
                        id
                        name
                    }
                }
            `,
            variables: {
                data: {
                    ...prodData,
                    image: imageBase64
                }
            }
        }, {
            headers: this.getAuthHeader()
        });
    }
    viewOrders(userId){
        this.flag = true;
        this.getRole(this.flag)
        return axios.post(`GQL_URL`, {
            query: `
            query GetOrders($userId: ID!) {
                viewOrders(userId: $userId) {
                    id
        }
    }`, 
        variables: { userId: this.getId() }
            }, {
                headers: { 'Authorization': this.getAuthHeader()}
            });
        }
    updateProductDetails(productId, updatedData){
        this.flag = false;
        this.getRole(this.flag)
        return axios.post(GQL_URL, {
        query: `
            mutation UpdateProduct($productId: ID!, $updatedData: ProductUpdateInput!) {
                updateProduct(productId: $productId, data: $updatedData) {
                    id
                }
            }
        `,
        variables: { 
            productId: productId, 
            updatedData: updatedData 
        }
    }, { 
        headers: this.getAuthHeader() 
    });
}
productDeletion(productId  ){
        this.flag = true;
        this.getRole(this.flag)
    return axios.post(GQL_URL, {
        query: `
            query DeleteProduct($productId: ID!) {
                deleteProduct(productId: $productId) {
                    id
                
        }
    }`, variables: {
            productId: productId
        }
    }, {
        headers: this.getAuthHeader()
    });
}

sellerProfileUpdate(profileData){
        this.flag = true;
        this.getRole(this.flag)
    return axios.post(GQL_URL, {
        query: `
            mutation UpdateSellerProfile($profileData: SellerProfileInput!) {
                updateProfile(data: $profileData) {
                    id
                }
            }`,

        variables: {
            profileData: profileData
        }
    }, {
        headers: this.getAuthHeader()
    });
}

}
export default new SellerService();
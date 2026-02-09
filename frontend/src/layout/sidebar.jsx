import {Link, useNavigate} from "react-router-dom";
import authService from "../services/auth.service";

function Sidebar(){
    const navigate = useNavigate();
    const user = authService.getAuthUser(); 
    return (
        <aside className="fixed left-0 top-16 h-screen w-64
         bg-slate-800 border-r border-slate-700 text-white p-6">
        <div className="group relative">
        <h3 className="font-bold mb-2 text-white cursor-pointer flex 
        items-center gap-2 hover:text-grey-200">Categories
        <span className="text-xs transition-transform group-hover:rotate-180">▼</span>
        </h3>
        <ul className="hidden group-hover:block space-y-2 pl-4 transition-all duration-300">
                    <li className="cursor-pointer text-white hover:text-grey-600">Electronics</li>
                    <li className="cursor-pointer text-white hover:text-grey-600">Fashion</li>
                    <li className="cursor-pointer text-white hover:text-grey-600">Home & Kitchen</li>
                    <li className="cursor-pointer text-white hover:text-grey-600">Books</li>
        </ul>
        </div>
        <div className="space-y-4">
                <h3 className="font-bold text-slate-700">Quick Links</h3>
                
                <ul className="space-y-3">
                    <li className="flex items-center gap-2 cursor-pointer text-slate-600 hover:text-blue-600">
                        <span>Trending</span> 
                    </li>
                    <li className="flex items-center gap-2 cursor-pointer text-slate-600 hover:text-blue-600">
                        <span>My Orders</span>
                    </li>
                    <li className="flex items-center gap-2 cursor-pointer text-slate-600 hover:text-blue-600">
                        <span>My Profile</span>
                    </li>
                </ul>
            </div>

        </aside>
    )
}
export default Sidebar;
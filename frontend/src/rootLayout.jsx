import { NavLink, Outlet } from "react-router-dom";

function RootLayout(){
    return(
        <>
        <div className="flex h-screen overflow-hidden">
            
        
        <main className="flex-1 bg-gray-100  overflow-auto">
            <Outlet/>
        </main>
        </div> 
        
            
        </>
    )
}
export default RootLayout;
import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";





const Landing = () => {

    const user = useSelector((state) => state.session.user);
    const dispatch = useDispatch();
    const userId = user?.id;
    
    useEffect(async () => {
        const data = await fetch(`/api/users/${userId}`);
        const responseData = await data.json();
        console.log("LANDING PAGE USEEFFECT");
    if(responseData.errors){
        console.log("ERRORS IN LANDING PAGE USEEFFECT");
    } else
    {
        console.log("NO ERRORS IN LANDING PAGE USEEFFECT");
    }

        const userCollections = responseData.collections;
        console.log("USER COLLECTIONS IN LANDING PAGE USEEFFECT", userCollections); 
                

    }, [dispatch]);
    
    
    return (

        <div>
            <h1>You have landed on the landing page next to the landing pad where jets land near landing aircraft</h1>
        </div>
    );
    

}

export default Landing;
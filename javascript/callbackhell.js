function getdata(id,getnextdata){
    setTimeout(() =>{
        console.log("id = ",id);
        if(getnextdata){
            getnextdata();
        }
    },2000)

    
    
}
getdata(123,() =>{
    getdata(234,() =>{
        getdata(345);
    });

    });
function getdata(id,nextdata){
    return promise = new Promise((resolve,reject) => {
        setTimeout(() =>{
            console.log("data = ",id);
            resolve("sucess");
            if(nextdata){
                nextdata();
            }
        },5000);
    });
}
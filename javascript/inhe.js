class parent{

   

    age(num){
        this.num = num;
        console.log(this.num);
    }

    name(fullname){
        this.fullname = fullname;
        console.log(this.fullname);
    }
    

    
}


c1 = new parent();
console.log(c1);
c1.age(23);
c1.name("vidhi");



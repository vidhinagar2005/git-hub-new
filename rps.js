let user_score = 0;
let comp_score = 0;

const choices = document.querySelectorAll(".choice");
console.log(choices);

const usermodi = document.querySelector("#user-score");
const compmodi = document.querySelector("#comp-score");

const msg = document.querySelector("#msg");
const showWin = (userwin,userchoice,comchoice) =>{
    if(userwin == true){
        
        user_score++;
        usermodi.innerText = user_score;
        
        msg.innerText = ` you win! your choice ${userchoice} com choice ${comchoice}`;
        msg.style.backgroundColor = "green";
        
    }else{
        
        comp_score++;
        compmodi.innerText = comp_score;
        msg.innerText = ` you loss! your choice ${userchoice} com choice ${comchoice}`;
        msg.style.backgroundColor = "red";
    
    }

}
const gencomchoice = () =>{
    option = ["rock", "paper", "scissior"];
    const randidx = Math.floor(Math.random() * 3);
    return option[randidx];
};

const drawgame = () =>{
    console.log("Draw game");
    msg.innerText = "Game Draw..";
    msg.style.backgroundColor = "#081b31";
    
}

const playgame = (userchoice) =>{
    console.log("userchoice = ", userchoice);
    const comchoice = gencomchoice();
    console.log("computer choice = ", comchoice);
    
    if(userchoice == comchoice){
        drawgame();
    }else{
        let userwin = true;
        if(userchoice == "rock"){
            //com have 2 choice
            //paper,scissor
            userwin = comchoice == "paper" ? false : true;
        }else if(userchoice == "paper"){
            //com have 2 choice
            //rock, scissor
            userwin = comchoice == "scissor" ? false : true;
        }else{
            //com have 2 choice
            //rock, paper
            userchoice = comchoice == "rock" ? false : true;
        }
        showWin(userwin,userchoice,comchoice);
    }
    
};




choices.forEach((choice) =>
{
     choice.addEventListener("click",() =>{
        const userchoice = choice.getAttribute("id");
        // console.log("choice was clicked",userchoice);
        playgame(userchoice);

    });
});
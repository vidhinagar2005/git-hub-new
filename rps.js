let user_score = 0;
let comp_score = 0;

const choices = document.querySelectorAll(".choice");
console.log(choices);


const showWin = (userwin) =>{
    if(userwin == true){
        console.log("You are win!");
    }else{
        console.log("You Loss!");
    }

}
const gencomchoice = () =>{
    option = ["rock", "paper", "scissior"];
    const randidx = Math.floor(Math.random() * 3);
    return option[randidx];
};

const drawgame = () =>{
    console.log("Draw game");
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
        showWin(userwin);
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
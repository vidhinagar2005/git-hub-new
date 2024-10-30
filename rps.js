let user_score = 0;
let comp_score = 0;

const choices = document.querySelectorAll(".choice");
console.log(choices);
choices.forEach((choice) =>
{
    
    
    
    choice.addEventListener("click",() =>{
        const userchoice = choice.getAttribute("id");
        console.log("choice was clicked",userchoice);

    });
});
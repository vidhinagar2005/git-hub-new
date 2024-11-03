let boxes = document.querySelectorAll(".box");
let resetbtn = document.querySelector("#reset-btn");

boxes.forEach((box) => {
    box.addEventListener("click",() => {
        box.innerText = "vd";
        console.log("clicked");

    });
});


// boxes.forEach((box) => {
//     box.addEventListener("click", () => {
//         box.innerText = "O";
//     });
// });
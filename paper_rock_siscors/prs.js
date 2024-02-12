
function computerChoise() {
    pastImg2.classList.add("hidden");
    let randomIndex = Math.trunc(Math.random() * 3);
    console.log(randomIndex);
    let chosenImg = rpsList[randomIndex]
    pastImg2 = chosenImg;
    chosenImg.classList.remove("hidden");
}

const paper2 = document.querySelector(".img-choice-21");
const rock2 = document.querySelector(".img-choice-22");
const siscors2 = document.querySelector(".img-choice-23");

const paper1 = document.querySelector(".img-choice-11");
const rock1 = document.querySelector(".img-choice-12");
const siscors1 = document.querySelector(".img-choice-13");

let rpsList = [paper2,rock2,siscors2];
let pastImg2 = document.querySelector(".smt");
let pastImg1 = document.querySelector(".smt-1");
let score1 = 0;
let score2 = 0;

let message = document.querySelector(".message");


const play = () => {
    computerChoise();
    calcScore();
}
// =====================================================================

function playerChosenImg(image){
    pastImg1.classList.add("hidden");

    let currentImage = document.querySelector("."+image);
    currentImage.classList.remove("hidden");
    pastImg1 = currentImage;

    message.classList.add("hidden");
}
const calcScore = () => {
    if ((pastImg1 == paper1 && pastImg2 == siscors2) || (pastImg1 == siscors1 && pastImg2 == rock2) || (pastImg1 == rock1 && pastImg2 == paper2)) {
        score2++;
        document.querySelector(".score-two").textContent = score2;
    }else if ((pastImg1 == paper1 && pastImg2 == rock2) || (pastImg1 == siscors1 && pastImg2 == paper2) || (pastImg1 == rock1 && pastImg2 == siscors2)) {
        score1++;
        document.querySelector(".score-one").textContent = score1;
    }
    else if((pastImg1 == paper1 && pastImg2 == paper2) || (pastImg1 == siscors1 && pastImg2 == siscors2) || (pastImg1 == rock1 && pastImg2 == rock2)){
        console.log(pastImg1);
        console.log(pastImg2);
        
        message.textContent = "Both players chose the same choice"
        message.classList.remove("hidden")
    }
}

const restart = () => {
    message.classList.add("hidden");

    pastImg2.classList.add("hidden");
    pastImg1.classList.add("hidden");
    
    pastImg2 = document.querySelector(".smt");
    pastImg1 = document.querySelector(".smt-1");

    score1 = 0;
    score2 = 0;

    document.querySelector(".score-one").textContent = score1;
    document.querySelector(".score-two").textContent = score2;

}
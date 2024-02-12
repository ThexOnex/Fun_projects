'strict mode' // sd

const rollTheDice = function () {
    startImg.classList.add("hidden");

    choisenImg.classList.add("hidden");
    var randomIndex = Math.trunc(Math.random() * 6);

    const imgList = [img1,img2,img3,img4,img5,img6];
    choisenImg = imgList[randomIndex];
    choisenImg.classList.remove("hidden");
    updateCurrentScore(randomIndex + 1);
    if (randomIndex == 0){
        updatePlayer();
    }
};

const updateCurrentScore = function (num){
    currentScore += num;
    if(ispos == 1){
        CurrentScoreDivOne.textContent = currentScore;
    }
    else {
        CurrentScoreDivTwo.textContent = currentScore;
    }
}

const updatePlayer = function () {
    currentScore = 0;
    ispos *= -1;
    if (ispos == -1){
    player1.classList.add("opacity-50")
    player2.classList.remove("opacity-50")
    CurrentScoreDivOne.textContent = 0;
    }
    else {
    player2.classList.add("opacity-50")// 2 lost
    player1.classList.remove("opacity-50") 
    CurrentScoreDivTwo.textContent = 0;
    }
}


const HoldScore = function () {
    if(ispos === 1){
        totalScoreOne += currentScore;
        currentPlayerTotalOne.textContent = totalScoreOne;
        updatePlayer();
    }
    else {
        totalScoreTwo += currentScore;
        currentPlayerTotalTwo.textContent = totalScoreTwo;
        updatePlayer();
    }
}

const Restart = function (){
    if(ispos != 1){
        player2.classList.add("opacity-50")// 2 lost
        player1.classList.remove("opacity-50") 
        CurrentScoreDivTwo.textContent = 0;
    }
    totalScoreOne = 0;
    totalScoreTwo = 0;
    currentScore = 0;
    ispos = 1;

    currentPlayerTotalOne.textContent = 0;
    CurrentScoreDivOne.textContent = 0;

    startImg.classList.remove("hidden");
    choisenImg.classList.add("hidden");

    currentPlayerTotalTwo.textContent = 0;
    CurrentScoreDivTwo.textContent = 0;
}

var choisenImg = document.querySelector(".dice")

var totalScoreOne = 0;
var totalScoreTwo = 0;
var currentScore = 0;
var ispos = 1;

var player1 = document.querySelector(".one");
var player2 = document.querySelector(".two");
player1.classList.remove("opacity-50")

const btnRoll = document.querySelector(".b-two");
const btnNew = document.querySelector(".b-one");
const btnHold = document.querySelector(".b-three");

var CurrentScoreDivOne = document.querySelector(".current-player-1");
var CurrentScoreDivTwo = document.querySelector(".current-player-2");
var currentPlayerTotalOne = document.querySelector(".s-one");
var currentPlayerTotalTwo = document.querySelector(".s-two");

startImg = document.querySelector(".dice");
startImg.classList.remove("hidden");
choisenImg = startImg;

img1 = document.getElementById("img-1");
img2 = document.getElementById("img-2");
img3 = document.getElementById("img-3");
img4 = document.getElementById("img-4");
img5 = document.getElementById("img-5");
img6 = document.getElementById("img-6");

btnRoll.addEventListener("click",rollTheDice);
btnHold.addEventListener("click", HoldScore);
btnNew.addEventListener("click", Restart)
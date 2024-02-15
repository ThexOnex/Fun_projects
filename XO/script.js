const case11 = document.querySelector(".div-11"); 
const case12 = document.querySelector(".div-12"); 
const case13 = document.querySelector(".div-13"); 
const case21 = document.querySelector(".div-21"); 
const case22 = document.querySelector(".div-22"); 
const case23 = document.querySelector(".div-23"); 
const case31 = document.querySelector(".div-31"); 
const case32 = document.querySelector(".div-32"); 
const case33 = document.querySelector(".div-33"); 

const cases = [case11,case12,case13,case21,case22,case23,case31,case32,case33]

const wincases = [[case11,case12,case13],[case21,case22,case23],[case31,case32,case33],[case11,case22,case33],[case13,case22,case31],[case12,case22,case32],[case11,case21,case31],[case13,case23,case33]]

const messageWin = document.querySelector(".play");
const messageLost = document.querySelector(".com");
let message;

function changeValue(caseIndex, string){
    if(cases[caseIndex-1].value == ""){
        cases[caseIndex-1].value = string;
        CheckPlayerWin()
        if (CheckPlayerWin() != -1){
            computerChoice()        
        }
    }
}

function computerChoice () {
    randomIndex = Math.trunc(Math.random() * 9);
    if((cases[randomIndex].value != 'X') && (cases[randomIndex].value != 'O')){
        cases[randomIndex].value = "O"
        CheckComputerWin()
    }
    else {
        computerChoice()
    }
}

const CheckPlayerWin = function () {
    for(let i = 0 ; i < wincases.length; i++){
        let j = 0;
        while(j < wincases[i].length){
            if (wincases[i][j].value != "X"){
                break;
            }
            j++;
            if (j === 3){
                console.log(wincases[i]);
                messageWin.classList.remove("hidden")
                message = messageWin;
                return -1;
            }
        }
    }
}

const CheckComputerWin = function () {
    for(let i = 0 ; i < wincases.length; i++){
        let j = 0;
        while(j < wincases[i].length){
            if (wincases[i][j].value != "O"){
                break;
            }
            j++;
            if (j === 3){
                console.log(wincases[i]);
                messageLost.classList.remove("hidden")
                message = messageLost;
                return -1;
            }
        }
    }
}

function restart() {
    console.log('bbbbbb');

    for (let i = 0; i<cases.length; i++){
        cases[i].value = ""
    }

    message.classList.add("hidden");
}
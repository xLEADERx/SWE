var text = 'occas sorted eved feat the wer life and humblame that the lay with bennet anxiouse patibut eps scarospect you name charlour';
var i = 0;
var active = false;
var t2 = document.getElementById("t2");
var innerHTML = t2.innerHTML;
var st_time = 0;
var curr_time = 0;
var errors = 0;
var score = 0;

function getCode(event) {
    var x = event.keyCode;
    check(x, text.charCodeAt(i))
}

function highlight(i) {
    innerHTML = text.substring(0, i) + "<span class='highlight'>" + text.charAt(i) + "</span>" + text.substring(i + 1, text.length);
    t2.innerHTML = innerHTML;
}
var dupli = false;
function check(x, letter) {
    if (x == letter) {
        if (i == 0) {
            st_time = Math.floor(Date.now() / 1000);
        } else if (i == text.length - 1) {
            curr_time = Math.floor(Date.now() / 1000);
            setWPM()
        }
        i++;
        t2.innerHTML = text;
        highlight(i)
        dupli = false;
    } else if (dupli == false) {
        errors++;
        dupli = true;
    }
}

function setfocus() {
    active = true;
    document.getElementById('myInput').focus();
    highlight(i)
}

function checkfocus() {
    if (active) {
        active = false;
    } else {
        t2.innerHTML = text;
        active = true;
    }
}

function getword() {
    t2.innerHTML = text;
}
function setWPM(secs) {
    var sec = curr_time - st_time;
    var min = sec / 60;
    var words = text.split(' ').length;
    var wpa = words / min;
    var wp = document.getElementById('wpa');
    wp.innerHTML = Math.round(wpa)


    //ERRORS
    var errorsObj = document.getElementById('errors');
    errorsObj.innerHTML = errors;

    var scoreObj = document.getElementById('score');
    scoreObj.innerHTML = wpa * words - (1.5 * errors);
}

// function blink(){
//     highlight(i);
//     var myvar =  setInterval(function(){ blink();}, 3000);  
//     t2.innerHTML = text;
// }   
// blink()
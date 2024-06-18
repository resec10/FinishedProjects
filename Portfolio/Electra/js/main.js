//Includes functions for the toolbars, header and footer
const products = document.querySelector(".products-button");
var current_rotation = 0, count = 0;
products.addEventListener('click', function () {
    count++;
    current_rotation += 180;
    document.querySelector(".products-button svg").style.transform = `rotate(${current_rotation}deg)`;
    var tab = document.querySelectorAll(".pick-menu>div>img");
    var tabDiv = document.querySelectorAll(".pick-menu>div>p");
    var tabT = document.querySelectorAll(".pick-menu>div");
    if (count % 2 !== 0) {
        for (var x = 0; x < tab.length; x++) {
            tab[x].style.visibility = "visible";
        }
        for (var x = 0; x < tabDiv.length; x++) {
            tabDiv[x].style.visibility = "visible";
        }
        for (var x = 0; x < tabT.length; x++) {
            tabT[x].style.border = "1px solid #F5F5F5";
        }
        document.querySelector(".pick-menu").style.visibility = "visible";
    } else if (count % 2 === 0) {
        for (var x = 0; x < tab.length; x++) {
            tab[x].style.visibility = "hidden";
        }
        for (var x = 0; x < tabDiv.length; x++) {
            tabDiv[x].style.visibility = "hidden";
        }
        for (var x = 0; x < tabT.length; x++) {
            tabT[x].style.border = "none";
        }
        document.querySelector(".pick-menu").style.visibility = "hidden";
    }
});

document.querySelector(".header-container").addEventListener('click', function () {
    window.location.href = "index.html";
});

document.querySelector(".completed-builds").addEventListener('click', function () {
    window.location.href = "completedBuilds.html";
});

var tab = document.querySelectorAll(".footer-item");

tab[0].addEventListener('click', function () {
    window.location.href = "buildPC.html";
});

tab[1].addEventListener('click', function () {
    window.location.href = "completedBuilds.html";
});

tab[2].addEventListener('click', function () {
    window.location.href="aboutUs.html";
});

tab[3].addEventListener("click", function(){
    window.location.href="disclosure.html";
});

tab[4].addEventListener("click", function(){
    window.location.href="contactUs.html";
});

var arr=document.querySelectorAll(".pick-menu>div");

arr[0].addEventListener("click", function(){
    window.location.href="chooseCPU.html";
});

arr[1].addEventListener("click", function(){
    window.location.href="chooseCPUCooler.html";
});

arr[2].addEventListener("click", function(){
    window.location.href="chooseMotherboards.html";
});

arr[3].addEventListener("click", function(){
    window.location.href="chooseMemory.html";
});

arr[4].addEventListener("click", function(){
    window.location.href="chooseStorage.html";
});

arr[5].addEventListener("click", function(){
    window.location.href="chooseVideoCard.html";
});

arr[6].addEventListener("click", function(){
    window.location.href="choosePowerSupply.html";
});

arr[7].addEventListener("click", function(){
    window.location.href="chooseCase.html";
});
window.onscroll = function (e) {
    if (window.scrollY >= 500){
        document.querySelector('.scroll__bar__site').style.opacity = 1;
        document.querySelector('.display__block__navigation').style.opacity = 1;
        document.querySelector('.scroll__bar__site').scrollIntoView();
    } else if (window.scrollY <= 500){
        document.querySelector('.scroll__bar__site').style.opacity = 0;
        document.querySelector('.display__block__navigation').style.opacity = 0;
    }
};
document.querySelector('.scroll__bar__site').onclick = () => {
    window.scrollTo(0, 0);
}
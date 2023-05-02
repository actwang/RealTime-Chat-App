if (document.documentElement.scrollHeight > window.innerHeight){
    // webpage exceeds one viewport height, we need to place .bot at the very bottom
    document.querySelector('.bot').classList.remove('bottom-0');
    document.querySelector('.bot').classList.add('fixed');
}
else{
    // place it at viewport's bottom
    document.querySelector('.bot').classList.remove('fixed');
    document.querySelector('.bot').classList.add('bottom-0');
}
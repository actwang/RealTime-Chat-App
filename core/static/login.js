document.cookie = "SameSite=None; Secure";

let eye = document.querySelector('.eye');
let pass_input = document.querySelector('input[name="password"]');
console.log('nice');
// only add the listener 
if (eye && pass_input){
    eye.addEventListener('click', ()=>toggleVisibility(eye, pass_input));
}

function toggleVisibility(eye, pass){
    if (pass.type === 'password'){
        // if it's password set it to text for visibility
        pass.type = 'text';
        // update the eye icon
        eye.classList.remove('fa-eye-slash');
        eye.classList.add('fa-eye');
    }
    else{
        pass.type = 'password';
        eye.classList.remove('fa-eye');
        eye.classList.add('fa-eye-slash');
    }
}


document.cookie = "SameSite=None; Secure";
// console.log('nice');
let eye1 = document.querySelector('.eye_1');
let pass1_input = document.querySelector('input[name="password1"]');

eye1.addEventListener('click', ()=>toggleVisibility(eye1, pass1_input));

let eye2 = document.querySelector('.eye_2');
let pass2_input = document.querySelector('input[name="password2"]');
eye2.addEventListener('click', ()=>toggleVisibility(eye2, pass2_input));

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


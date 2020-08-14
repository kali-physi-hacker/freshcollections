const validatePassword = (value) => {
    const validationRegex = new RegExp(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/)
    return validationRegex.test(value)
}

const signUpForm = document.querySelector("form#signup")

const validatingPassword = (e) => {
    if (validatePassword(e.target.value)) {
        e.target.setCustomValidity("")
    }
}

const validatePasswordMatch = (password1Input, password2Input) => {
    console.log("Validation")
    if (password1Input.value != password2Input.value) {
        console.log('Invalid Passwords')
        password2Input.setCustomValidity("Invalid")
        password2Input.addEventListener("input", ()=>{validatePasswordMatch(password1Input, password2Input)})
        return false;
    }else{
        password2Input.setCustomValidity("")
        return true;
    }
}
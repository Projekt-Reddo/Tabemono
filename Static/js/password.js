function passwordConfirm() {
    password = document.getElementById('password').value;
    passwordCheck = document.getElementById('passwordcheck').value;

    if (password!==passwordCheck) {
        alert("Password does not match!");
        return false;
    }
}
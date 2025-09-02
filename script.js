// script.js

// Validate Register Form
function validateRegisterForm() {
    let username = document.forms["registerForm"]["username"].value.trim();
    let email = document.forms["registerForm"]["email"].value.trim();
    let password = document.forms["registerForm"]["password"].value.trim();

    if (username.length < 3) {
        alert("Username must be at least 3 characters long.");
        return false;
    }
    if (!email.includes("@")) {
        alert("Please enter a valid email.");
        return false;
    }
    if (password.length < 6) {
        alert("Password must be at least 6 characters long.");
        return false;
    }
    return true;
}

// Validate Login Form
function validateLoginForm() {
    let username = document.forms["loginForm"]["username"].value.trim();
    let password = document.forms["loginForm"]["password"].value.trim();

    if (username === "" || password === "") {
        alert("Both fields are required.");
        return false;
    }
    return true;
}

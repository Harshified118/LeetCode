let password;
let attempts = 0;
const maxAttempts = 3;

do {
    password = prompt("Enter your password:");
    attempts++;

    if (password === "1234") {
        break;
    }
} while (attempts < maxAttempts);

if (password === "1234") {
    console.log("Access granted");
} else {
    console.log("Account locked");
}
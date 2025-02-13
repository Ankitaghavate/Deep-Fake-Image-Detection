document.addEventListener("DOMContentLoaded", () => {
    const messages = [
        "AI-Powered Fake Detection",
        "Detect Fake Media with AI",
        "Ensure Authenticity & Security"
    ];

    let index = 0;
    const textElement = document.getElementById("animated-text");

    function changeText() {
        textElement.style.opacity = "0";  // Fade out
        textElement.style.transform = "translateX(-100%)"; // Move left

        setTimeout(() => {
            textElement.innerText = messages[index]; // Change text
            textElement.style.opacity = "1"; // Fade in
            textElement.style.transform = "translateX(100%)"; // Move right

            setTimeout(() => {
                textElement.style.transform = "translateX(0)"; // Reset position
            }, 500);

            index = (index + 1) % messages.length; // Loop through messages
        }, 1000);
    }

    setInterval(changeText, 3000); // Change text every 3 seconds
});

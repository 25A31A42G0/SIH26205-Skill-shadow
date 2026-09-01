function submitChallenge() {
    const answer = document.getElementById("answer").value.trim();

    if (answer === "") {
        alert("Please submit your answer first!");
        return;
    }

    // Save the answer temporarily
    localStorage.setItem("userAnswer", answer);

    // Move to result page
    window.location.href = "result.html";
}
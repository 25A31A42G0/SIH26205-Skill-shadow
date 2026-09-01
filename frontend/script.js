function submitChallenge() {

    const answer = document.getElementById("answer").value.trim();

    if (answer === "") {
        alert("Please submit your answer first!");
        return;
    }

    // Temporary mock analysis
    // Later this will call Member 2's AI API.

    localStorage.setItem("userAnswer", answer);

    alert("Challenge submitted! AI analysis completed.");

    window.location.href = "result.html";
}
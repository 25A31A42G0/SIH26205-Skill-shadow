function submitChallenge() {

    const answer =
        document.getElementById("answer").value.trim();


    if (answer === "") {

        alert("Please submit your answer first!");

        return;
    }


    localStorage.setItem(
        "userAnswer",
        answer
    );


    window.location.href =
        "result.html";
}



/* =========================================================
   DISPLAY SUBMITTED ANSWER
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {

    const answerBox =
        document.getElementById("submittedAnswer");


    if (!answerBox) {
        return;
    }


    const answer =
        localStorage.getItem("userAnswer");


    if (answer) {

        answerBox.textContent =
            answer;

    } else {

        answerBox.textContent =
            "No response submitted yet.";

    }

});
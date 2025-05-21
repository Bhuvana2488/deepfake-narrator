document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("extractAndListenBtn").addEventListener("click", function () {
    console.log("Button clicked!"); // Debugging line

    // Extract visible text from the website dynamically
    function getVisibleText() {
      let elements = document.body.querySelectorAll("*:not(script):not(style):not(meta):not(link)");
      let textContent = "";

      elements.forEach(el => {
        let computedStyle = window.getComputedStyle(el);
        if (computedStyle.display !== "none" && computedStyle.visibility !== "hidden") {
          textContent += " " + el.innerText.trim();
        }
      });

      return textContent.trim();
    }

    const text = getVisibleText();

    if (!text) {
      alert("No readable content found on the page!");
      return;
    }

    fetch("/generate-audio", { // Ensure this matches the route in app.py
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: text }) // Send extracted content
    })
    .then(response => {
      if (response.ok) {
        return response.blob();
      } else {
        return response.json().then(data => {
          throw new Error(data.error || "Failed to generate audio");
        });
      }
    })
    .then(blob => {
      const audioUrl = URL.createObjectURL(blob);
      const audio = new Audio(audioUrl);
      audio.play();
    })
    .catch(error => {
      console.error("Error:", error);
      alert(error.message);
    });
  });
});

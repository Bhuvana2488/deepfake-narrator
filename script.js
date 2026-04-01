document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("extractAndListenBtn").addEventListener("click", async function () {
    console.log("Button clicked!");

    // Extract visible text
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

    try {
      // STEP 1: Send extracted text to chatbot (OpenAI)
      const chatResponse = await fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: text })
      });

      const chatData = await chatResponse.json();

      if (!chatResponse.ok) {
        throw new Error(chatData.error || "Chatbot failed");
      }

      const chatbotReply = chatData.response;
      console.log("Chatbot Reply:", chatbotReply);

      // STEP 2: Convert chatbot reply to speech (ElevenLabs)
      const ttsResponse = await fetch("/generate-audio", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: chatbotReply })
      });

      if (!ttsResponse.ok) {
        const errorData = await ttsResponse.json();
        throw new Error(errorData.error || "TTS failed");
      }

      const blob = await ttsResponse.blob();

      // STEP 3: Play audio
      const audioUrl = URL.createObjectURL(blob);
      const audio = new Audio(audioUrl);
      audio.play();

    } catch (error) {
      console.error("Error:", error);
      alert(error.message);
    }
  });
});

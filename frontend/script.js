let gauge = null; 

document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("#predictForm");
  const resultDiv = document.querySelector("#result");

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    resultDiv.innerHTML = "";

    const formData = new FormData(form);
    const payload = Object.fromEntries(formData.entries());

   
    ["age", "trestbps", "chol", "thalch", "oldpeak", "ca"].forEach((key) => {
      if (payload[key] !== undefined && payload[key] !== "") {
        payload[key] = parseFloat(payload[key]);
      }
    });

    try {
      const res = await fetch(`http://127.0.0.1:5000/predict?ts=${Date.now()}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await res.json();


      if (data.error) {
        resultDiv.innerHTML = `<span class="text-red-600">Error: ${data.error}</span>`;
        return;
      }

    
      resultDiv.innerHTML = `
        <span class="font-bold">${data.result}</span><br/>
        <span>Probability of Heart Disease: ${data.probability}%</span><br/>
        <div class="font-semibold mt-2">${data.risk_level}</div>
      `;

    
      if (!gauge) {
        gauge = new JustGage({
          id: "riskGauge",
          value: data.probability,
          min: 0,
          max: 100,
          title: "Risk Level",
          label: "%",
          levelColors: ["#22c55e", "#facc15", "#ef4444"], // green yellow red
          levelColorsGradient: false
        });
      } else {
        gauge.refresh(data.probability);
      }

    } catch (err) {
      console.error("Fetch error:", err);
      resultDiv.innerHTML = `<span class="text-red-600">Fetch error: ${err.message}</span>`;
    }
  });

  // ✅ Clear everything on form reset
  form.addEventListener("reset", function () {
    resultDiv.innerHTML = "";
    if (gauge) gauge.refresh(0);
  });
});

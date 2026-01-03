const API_BASE = "http://localhost:8000";

/* ---------- STATUS ---------- */
function setStatus(message, type = "info") {
  const status = document.getElementById("status");
  status.innerText = message;
  status.className = `status ${type}`;
}

/* ---------- IMPORT IMAGES ---------- */
function importImages() {
  const url = document.getElementById("folder").value.trim();
  const btn = document.getElementById("importBtn");

  if (!url) {
    setStatus("⚠️ Please enter a Google Drive folder URL", "error");
    return;
  }

  btn.disabled = true;
  btn.innerText = "Importing...";
  setStatus("⏳ Importing images from Google Drive...", "info");

  fetch(`${API_BASE}/import/google-drive`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ folder_url: url })
  })
    .then(res => {
      if (!res.ok) throw new Error("Import failed");
      return res.json();
    })
    .then(() => {
      setStatus("✅ Import completed successfully", "success");
      loadImages(); // ✅ LOAD ONLY AFTER IMPORT
    })
    .catch(err => {
      console.error(err);
      setStatus("❌ Failed to import images. Check backend.", "error");
    })
    .finally(() => {
      btn.disabled = false;
      btn.innerText = "Import Images";
    });
}

/* ---------- LOAD IMAGES ---------- */
function loadImages() {
  fetch(`${API_BASE}/images`)
    .then(res => {
      if (!res.ok) throw new Error("Failed to fetch images");
      return res.json();
    })
    .then(data => {
      const container = document.getElementById("imagesContainer");
      container.innerHTML = "";

      if (!data.length) {
        container.innerHTML = `<div class="empty">No images found</div>`;
        return;
      }

      data.forEach(img => {
        const card = document.createElement("div");
        card.className = "image-card";

        card.innerHTML = `
          <img src="${img.storage_path}" alt="${img.name}" />
          <div class="meta">
            <p class="name">${img.name}</p>
            <p>📦 ${(img.size / 1024 / 1024).toFixed(2)} MB</p>
            <p>🖼️ ${img.mime_type}</p>
            <a href="${img.storage_path}" target="_blank">Open Image</a>
          </div>
        `;

        container.appendChild(card);
      });
    })
    .catch(err => {
      console.error(err);
      document.getElementById("imagesContainer").innerHTML =
        `<div class="empty error">Failed to load images</div>`;
    });
}

/* ---------- CLEAR UI ONLY ---------- */
function clearImagesUI() {
  const confirmClear = confirm("Clear images from screen only?");
  if (!confirmClear) return;

  document.getElementById("imagesContainer").innerHTML =
    `<div class="empty">No images yet</div>`;

  setStatus("🧹 Images cleared from screen (DB unchanged)", "info");
}

/* ---------- PAGE LOAD ---------- */
/* ❌ Do NOT load images automatically */
/* ❌ Do NOT clear localStorage (not used) */

window.onload = () => {
  document.getElementById("imagesContainer").innerHTML =
    `<div class="empty">No images yet</div>`;
};

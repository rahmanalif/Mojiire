const lightbox = document.getElementById("lightbox");
const lightboxImg = document.getElementById("lightbox-img");
const lightboxTitle = document.getElementById("lightbox-title");
const closeBtn = document.getElementById("lightbox-close");

document.querySelectorAll(".gallery-item img").forEach(img => {
  img.addEventListener("click", () => {
    lightboxImg.src = img.src;
    lightboxTitle.textContent = document.querySelector(".gallery-item p").innerHTML;
    lightboxTitle.style.color = "white";
    lightbox.style.display = "flex";
  });
});

closeBtn.addEventListener("click", () => {
  lightbox.style.display = "none";
});

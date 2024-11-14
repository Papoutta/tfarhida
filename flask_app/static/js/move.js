document.addEventListener("DOMContentLoaded", function () {
  const slideBox = document.getElementById("slideBox");
  const topLayer = document.querySelector(".topLayer");

  document.getElementById("goRight").addEventListener("click", function () {
    slideBox.animate(
      [{ marginLeft: "50%" }, { marginLeft: "0" }],
      { duration: 500, easing: "ease-in-out", fill: "forwards" }
    );
    topLayer.animate(
      [{ marginLeft: "0" }, { marginLeft: "100%" }],
      { duration: 500, easing: "ease-in-out", fill: "forwards" }
    );
  });

  document.getElementById("goLeft").addEventListener("click", function () {
    slideBox.animate(
      [{ marginLeft: "0" }, { marginLeft: "50%" }],
      { duration: 500, easing: "ease-in-out", fill: "forwards" }
    );
    topLayer.animate(
      [{ marginLeft: "100%" }, { marginLeft: "0" }],
      { duration: 500, easing: "ease-in-out", fill: "forwards" }
    );
  });
});

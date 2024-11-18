// Array of image sources
const images = [
"static/img/lastt.jpg",
"static/img/lastt2.jpg",
"static/img/lastt3.jpg",
"static/img/lastt4.jpg"]; 
let currentIndex = 0;

function changeImage() {
  const imgElement = document.getElementById("slideshow-image");

  // Slide the current image out to the left
  imgElement.classList.remove("visible");
  imgElement.classList.add("slide-out");

  // After the slide-out transition, change the image source and slide the new one in
  setTimeout(() => {
    currentIndex = (currentIndex + 1) % images.length; // Cycle to the next image
    imgElement.src = images[currentIndex];

    // Reset the classes to slide the new image in from the right
    imgElement.classList.remove("slide-out");
    imgElement.classList.add("slide-in");

    // After a brief delay, make the new image fully visible in the center
    setTimeout(() => {
      imgElement.classList.remove("slide-in");
      imgElement.classList.add("visible");
    }, 50); // Short delay to ensure the new image starts from the right
  }, 1000); // Matches the CSS transition duration (1 second)
}

// Change image every 3 seconds (3000 milliseconds)
setInterval(changeImage, 3000);




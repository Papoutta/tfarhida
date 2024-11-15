// Array of image sources
const photos = [
    "static/img/3018022022143229.jpg",
    "static/img/second_one.jpg",
    "static/img/third_one.jpg",
    "static/img/fourth_one.jpg"
];
let Index = 0;

function changeImage() {
    const imgElement = document.querySelector(".second_container img");
    const h2Element = document.querySelector(".second_container h2");


    // Wait a bit before adding it back to trigger the animation again
    setTimeout(() => {
        // Update the image source
        Index = (Index + 1) % photos.length; // Cycle to the next image
        imgElement.src = photos[Index];

        // Add the slide-in class for animation
        imgElement.classList.add("slide-in");

        // Fade in the title
        h2Element.classList.add("fade-in");
    }, 100); // Slight delay before applying the animation class
}

// Change the image every 4 seconds (5000 milliseconds)
// onload.apply(setInterval(changeImage, 4000))
setInterval(changeImage, 4000)


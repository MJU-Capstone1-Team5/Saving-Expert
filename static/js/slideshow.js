var slides = document.querySelectorAll("#slides > img");
var prev = document.getElementById("prev");
var next = document.getElementById("next");
var current = 0;

showSlides(current);
prev.onclick = prevSlide;
next.onclick = nextSlide;

function showSlides(n) {
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[n].style.display = "block";
}

function prevSlide() {
  if (current > 0) current -= 1;
  else
    current = slides.length - 1;
    showSlides(current);
}

function nextSlide() {
  if (current < slides.length - 1) current += 1;
  else
    current = 0;
    showSlides(current);  
}

// var imageContainer = document.getElementById('links');

// imageContainer.addEventListener('scroll', function() {
//   var scrollTop = imageContainer.scrollTop;
//   var imageHeight = imageContainer.clientHeight;
//   var totalScrollHeight = imageContainer.scrollHeight;
//   var scrollPercentage = (scrollTop / (totalScrollHeight - imageHeight)) * 100;

//   if (scrollPercentage < 33) {
//     imageContainer.classList = 'show-image1';
//   } else if (scrollPercentage < 66) {
//     imageContainer.classList = 'show-image2';
//   } else {
//     imageContainer.classList = 'show-image3';
//   }
// });

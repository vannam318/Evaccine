// Set the speed of the scroll
const scrollSpeed = 1000;

// Set the easing function for the scroll
const easingFunction = (t) => t * t;

// Get the current scroll position of the window
const getCurrentScrollPosition = () => window.pageYOffset || document.documentElement.scrollTop;

// Get the target scroll position based on the element's position on the page
const getTargetScrollPosition = (element) => {
  const elementPosition = element.getBoundingClientRect().top;
  const currentPosition = getCurrentScrollPosition();
  return currentPosition + elementPosition;
};

// Scroll to the target position smoothly
const scrollToTargetPosition = (targetPosition) => {
  const startPosition = getCurrentScrollPosition();
  const distance = targetPosition - startPosition;
  let startTime;

  // Define the animation function
  const animation = (currentTime) => {
    if (!startTime) {
      startTime = currentTime;
    }
    const timeElapsed = currentTime - startTime;
    const scrollPosition = startPosition + distance * easingFunction(timeElapsed / scrollSpeed);

    window.scrollTo(0, scrollPosition);

    if (timeElapsed < scrollSpeed) {
      window.requestAnimationFrame(animation);
    }
  };

  window.requestAnimationFrame(animation);
};

// Attach click event to smooth scroll links
const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
smoothScrollLinks.forEach((link) => {
  link.addEventListener('click', (event) => {
    event.preventDefault();
    const targetId = link.getAttribute('href');
    const targetElement = document.querySelector(targetId);
    const targetPosition = getTargetScrollPosition(targetElement);
    scrollToTargetPosition(targetPosition);
  });
});
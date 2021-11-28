var animateStrokeWidth = anime({
    targets: '.button',
    border: 10,
    autoplay: false
  });

  
  var animateY = anime({
    targets: '.links',
    cy: '100',
    autoplay: false
  });

  document.querySelector('.button').onclick = animateStrokeWidth.restart;
  document.getElementById('button_hide').onclick = animateY.restart;

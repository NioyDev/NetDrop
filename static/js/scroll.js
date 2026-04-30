// Inicializamos la librería
const lenis = new Lenis({
  duration: 1, // Qué tanto tarda en frenar (ajusta a tu gusto)
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -5 * t)), // La curva de suavidad
  smooth: true,
})

// Este es el "motor" que mantiene la fluidez
function raf(time) {
  lenis.raf(time)
  requestAnimationFrame(raf)
}

requestAnimationFrame(raf)
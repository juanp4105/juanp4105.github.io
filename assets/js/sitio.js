// Interacciones mínimas: menú móvil, filtro de publicaciones y el visor de la portada.
(function () {
  document.documentElement.classList.add('js');

  // Menú en pantallas pequeñas
  var boton = document.querySelector('.menu-boton');
  var nav = document.getElementById('navegacion');
  if (boton && nav) {
    boton.addEventListener('click', function () {
      var abierto = nav.classList.toggle('abierta');
      boton.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    });
  }

  // El visor "enfoca" la foto una sola vez al cargar
  var visor = document.querySelector('.visor');
  if (visor) {
    requestAnimationFrame(function () {
      setTimeout(function () { visor.classList.add('enfocado'); }, 250);
    });
  }

  // Filtro por tipo de publicación
  var filtros = document.querySelector('.filtros');
  if (filtros) {
    filtros.hidden = false;
    var botones = filtros.querySelectorAll('button');
    var anios = document.querySelectorAll('.anio');
    filtros.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      var tipo = b.getAttribute('data-filtro');
      botones.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      anios.forEach(function (anio) {
        var visibles = 0;
        anio.querySelectorAll('.ref').forEach(function (ref) {
          var mostrar = tipo === 'todas' || ref.getAttribute('data-tipo') === tipo;
          ref.hidden = !mostrar;
          if (mostrar) visibles++;
        });
        anio.hidden = visibles === 0;
      });
    });
  }

  // Contador de visitas (una visita por sesión del navegador; se muestra con una base inicial de 250)
  var contador = document.querySelector('.contador');
  if (contador && window.fetch) {
    var BASE_INICIAL = 250;
    var api = 'https://abacus.jasoncameron.dev/';
    var clave = 'juanp4105-github-io/visitas';
    var contada = false;
    try { contada = sessionStorage.getItem('visita-contada') === '1'; } catch (e) {}
    fetch(api + (contada ? 'get/' : 'hit/') + clave)
      .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
      .then(function (d) {
        if (typeof d.value !== 'number') return;
        try { sessionStorage.setItem('visita-contada', '1'); } catch (e) {}
        var num = contador.querySelector('.contador__num');
        var idioma = num.getAttribute('data-lang') || 'es';
        num.textContent = (d.value + BASE_INICIAL).toLocaleString(idioma);
        contador.hidden = false;
      })
      .catch(function () {});
  }
})();

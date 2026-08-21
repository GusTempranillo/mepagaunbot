document.querySelectorAll('.copiar-enlace').forEach(btn => {
  btn.addEventListener('click', async e => {
    e.preventDefault();
    const url = btn.dataset.url;
    try {
      await navigator.clipboard.writeText(url);
      const original = btn.textContent;
      btn.textContent = '¡Copiado!';
      setTimeout(() => btn.textContent = original, 2000);
    } catch (err) {
      console.error('Error al copiar:', err);
    }
  });
});

document.documentElement.classList.add('js');
const button = document.querySelector('.menu-button');
const nav = document.querySelector('#navigation');
if (button && nav) {
  const small = window.matchMedia('(max-width: 767px)');
  function setOpen(open) { nav.hidden = small.matches && !open; button.setAttribute('aria-expanded', String(!nav.hidden)); button.textContent = nav.hidden ? 'Menü öffnen' : 'Menü schließen'; }
  setOpen(false);
  button.addEventListener('click', () => setOpen(nav.hidden));
  small.addEventListener('change', () => setOpen(false));
  document.addEventListener('keydown', event => { if(event.key === 'Escape' && small.matches && !nav.hidden) { setOpen(false); button.focus(); } });
}

(() => {
  const t = window.noomiLocale || {};
  const player = document.getElementById('game');
  if (!player) return;
  const shell = document.getElementById('play-shell');
  const status = document.getElementById('game-status');
  const fullscreenButton = document.getElementById('fullscreen-game');
  const viewButton = document.getElementById('view-game');
  const WIDTH = 1282, HEIGHT = 786;
  let fitWindow = false, loadingTimer;
  function fitGame() {
    const fullscreen = document.fullscreenElement === shell;
    const available = fullscreen
      ? shell.clientHeight - shell.querySelector('.playbar').offsetHeight
      : Math.max(260, window.innerHeight - 230);
    const height = fitWindow || fullscreen ? Math.min(player.clientWidth * HEIGHT / WIDTH, available) : player.clientWidth * HEIGHT / WIDTH;
    player.style.height = Math.round(height) + 'px';
    const frame = document.getElementById('game-frame');
    if (frame) frame.style.transform = `translate(-50%, -50%) scale(${Math.min(player.clientWidth / WIDTH, height / HEIGHT)})`;
  }
  function startGame() {
    clearTimeout(loadingTimer);
    const frame = document.createElement('iframe');
    frame.id = 'game-frame';
    frame.title = 'NoomiClone original browser game by jamesnorth';
    frame.src = 'https://itch.io/embed-upload/3164009';
    frame.allow = 'fullscreen; autoplay; gamepad';
    frame.allowFullscreen = true;
    frame.width = WIDTH; frame.height = HEIGHT;
    frame.addEventListener('load', () => {
      // The outer iframe loading is not proof that the nested Unity game is ready.
      status.textContent = t.loaded || 'When the game appears, click inside it to use your keyboard. First load can take a minute.';
    });
    player.replaceChildren(frame);
    status.textContent = t.loading || 'Loading NoomiClone from itch.io. Keep this page open while the game starts.';
    fitGame();
    loadingTimer = setTimeout(() => {
      status.textContent = t.slow || 'Playing? Click inside the game for keyboard controls. Still blank? Try Reload or see Help.';
    }, 60000);
  }
  document.getElementById('start-game')?.addEventListener('click', startGame);
  document.getElementById('reload-game')?.addEventListener('click', startGame);
  viewButton.addEventListener('click', () => {
    fitWindow = !fitWindow;
    viewButton.textContent = fitWindow ? (t.expand || 'Expand view') : (t.fit || 'Fit to window');
    viewButton.setAttribute('aria-pressed', String(!fitWindow));
    fitGame();
  });
  fullscreenButton.addEventListener('click', async () => {
    try {
      if (document.fullscreenElement === shell) await document.exitFullscreen();
      else if (shell.requestFullscreen) await shell.requestFullscreen();
      else status.textContent = t.noFull || 'Fullscreen is unavailable here. Rotate your device or use Expand view.';
    } catch { status.textContent = t.noFull || 'Fullscreen is unavailable here. Use Expand view instead.'; }
  });
  document.addEventListener('fullscreenchange', () => {
    fullscreenButton.textContent = document.fullscreenElement === shell ? (t.exit || 'Exit fullscreen ↙') : (t.full || 'Fullscreen ↗');
    requestAnimationFrame(fitGame);
  });
  window.addEventListener('resize', fitGame);
  new ResizeObserver(fitGame).observe(player);
  fitGame();
})();

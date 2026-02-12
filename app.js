(async () => {
  const app = new PIXI.Application();
  await app.init({ width: 800, height: 600, background: 0xffffff });

  document.body.appendChild(app.canvas);

  const g = new PIXI.Graphics();
  g.rect(100, 100, 200, 100);
  g.fill(0x66CCFF);

  app.stage.addChild(g);
})();

jQuery('#responsive-title').fitText(2.0);

MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]},
  styles: {
    "#MathJax_Message": {left: "", right: 0},
    "#MathJax_MSIE_Frame": {left: "", right: 0}
  },
  TeX: {
    Macros: {
      P: ['\\mathcal{P}_{#1}\\Lambda^{#2}(\\Delta_{#3})', 3],
      Pm: ['\\mathcal{P}^-_{#1}\\Lambda^{#2}(\\Delta_{#3})', 3],
      Qm: ['\\mathcal{Q}^-_{#1}\\Lambda^{#2}(\\square_{#3})', 3],
      S: ['\\mathcal{S}_{#1}\\Lambda^{#2}(\\square_{#3})', 3],
      Pq: ['\\mathcal{P}_{#1}\\Lambda^{#2}(\\square_{#3})', 3],
      dx: ['\\mathrm{\\mathrm{d}x^{#1}}', 1],
      dof: ['#1\\times\\underbrace{\\P{#2}{#3}{#4}}_{#5}', 5],
      dofm: ['#1\\times\\underbrace{\\Pm{#2}{#3}{#4}}_{#5}', 5],
      dofq: ['#1\\times\\underbrace{\\Qm{#2}{#3}{#4}}_{#5}', 5],
      dofs: ['#1\\times\\underbrace{\\Pq{#2}{#3}{#4}}_{#5}', 5],
      pl: '\\,+\\,',
      div: '\\operatorname{div}',
      curl: '\\operatorname{curl}',
      tr: '\\operatorname{tr}',
      mH: '\\mathcal H',
      mP: '\\mathcal P',
      mQ: '\\mathcal Q',
      mS: '\\mathcal S',
    }
  }
});

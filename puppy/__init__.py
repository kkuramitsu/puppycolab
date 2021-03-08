import puppy.install

from IPython.display import HTML, SVG
from IPython.core.magic import register_cell_magic

@register_cell_magic
def p5js(line, src):
  return HTML(f"""
  <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.6.0/p5.js"></script>
  <script src="https://markknol.github.io/console-log-viewer/console-log-viewer.js?closed=true"></script>
  <script>
  new p5();
  {src.replace(" #", " //")}  // allow python-style comment
  </script>
  """)

@register_cell_magic
def matterjs(line, src):
  #処理して、JS変換して
  return HTML(f"""
  <canvas id="canvas" touch-action="none" width="800px" height="600px"></canvas>
  <script src="/nbextensions/google.colab/matter.js"></script>
  <script src="https://markknol.github.io/console-log-viewer/console-log-viewer.js?closed=true"></script>
  <script>
  {src}  // allow python-style comment
  </script>
  """)
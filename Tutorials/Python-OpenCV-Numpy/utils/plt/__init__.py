import pylab
from pylab import plt as _plt
from pylab import get_current_fig_manager
matplotlib_backend=pylab.matplotlib.backends.backend

def axis_ij(g=None):
	if g is None:
		g = _plt.gca()
	bottom, top = g.get_ylim()
	if top > bottom:
		g.set_ylim(top, bottom)
	else:
		pass

def maximize_figure(fig=None):
	if fig is None:
		fig = _plt.gcf()
	mng = _plt.get_current_fig_manager()
	try:
		mng.frame.Maximize(True)
	except AttributrError:
		print("Failed to maximize figure.")
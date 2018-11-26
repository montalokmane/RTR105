Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')
>>> from numpy import *
>>> x = linspace(0, 7, 70)
>>> 
======================== RESTART: /home/user/test1.py ========================
>>> 
======================== RESTART: /home/user/test1.py ========================
>>> 
======================== RESTART: /home/user/test1.py ========================
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
======================== RESTART: /home/user/test1.py ========================
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, '__name__': '__main__', '__doc__': None}

Traceback (most recent call last):
  File "/home/user/test1.py", line 11, in <module>
    y = cosx
NameError: name 'cosx' is not defined
>>> 
======================== RESTART: /home/user/test1.py ========================
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, '__name__': '__main__', '__doc__': None}
{'cos': <ufunc 'cos'>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, 'sys': <module 'sys' (built-in)>, 'linspace': <function linspace at 0x7f4de4130230>, 'x': array([ 0.        ,  0.10144928,  0.20289855,  0.30434783,  0.4057971 ,
        0.50724638,  0.60869565,  0.71014493,  0.8115942 ,  0.91304348,
        1.01449275,  1.11594203,  1.2173913 ,  1.31884058,  1.42028986,
        1.52173913,  1.62318841,  1.72463768,  1.82608696,  1.92753623,
        2.02898551,  2.13043478,  2.23188406,  2.33333333,  2.43478261,
        2.53623188,  2.63768116,  2.73913043,  2.84057971,  2.94202899,
        3.04347826,  3.14492754,  3.24637681,  3.34782609,  3.44927536,
        3.55072464,  3.65217391,  3.75362319,  3.85507246,  3.95652174,
        4.05797101,  4.15942029,  4.26086957,  4.36231884,  4.46376812,
        4.56521739,  4.66666667,  4.76811594,  4.86956522,  4.97101449,
        5.07246377,  5.17391304,  5.27536232,  5.37681159,  5.47826087,
        5.57971014,  5.68115942,  5.7826087 ,  5.88405797,  5.98550725,
        6.08695652,  6.1884058 ,  6.28985507,  6.39130435,  6.49275362,
        6.5942029 ,  6.69565217,  6.79710145,  6.89855072,  7.        ]), 'y': array([ 1.        ,  0.99485843,  0.97948661,  0.95404259,  0.91878803,
        0.87408545,  0.82039454,  0.7582674 ,  0.6883429 ,  0.61134007,
        0.52805076,  0.43933143,  0.3460944 ,  0.24929843,  0.1499389 ,
        0.04903752, -0.05236811, -0.15323524, -0.25252663, -0.34922125,
       -0.44232479, -0.53087984, -0.61397579, -0.69075814, -0.76043733,
       -0.82229685, -0.87570058, -0.92009937, -0.95503665, -0.98015317,
       -0.99519064, -0.99999444, -0.99451516, -0.97880915, -0.95303792,
       -0.91746648, -0.8724606 , -0.8184831 , -0.75608903, -0.68592   ,
       -0.60869756, -0.5252158 , -0.43633318, -0.34296369, -0.24606746,
       -0.14664089, -0.04570638,  0.05569812,  0.15652988,  0.25575202,
        0.35234423,  0.44531323,  0.53370302,  0.61660468,  0.6931657 ,
        0.76259881,  0.82419002,  0.87730597,  0.92140047,  0.95602009,
        0.98080883,  0.99551178,  0.99997776,  0.99416083,  0.97812081,
        0.95202265,  0.91613472,  0.87082605,  0.81656256,  0.75390225]), '__name__': '__main__', '__doc__': None}
>>> 
======================== RESTART: /home/user/test1.py ========================
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, '__name__': '__main__', '__doc__': None}
{'cos': <ufunc 'cos'>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, 'sys': <module 'sys' (built-in)>, 'linspace': <function linspace at 0x7f120e3c3230>, 'x': array([ 0. ,  0.4,  0.8,  1.2,  1.6,  2. ,  2.4,  2.8,  3.2,  3.6,  4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362]), '__name__': '__main__', '__doc__': None}
>>> x
array([ 0. ,  0.4,  0.8,  1.2,  1.6,  2. ,  2.4,  2.8,  3.2,  3.6,  4. ])
>>> x[0]
0.0
>>> x[10]
4.0
>>> x[5]
2.0
>>> len(y)
11
>>> 
======================== RESTART: /home/user/test1.py ========================
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, '__name__': '__main__', '__doc__': None}
{'cos': <ufunc 'cos'>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, 'sys': <module 'sys' (built-in)>, 'linspace': <function linspace at 0x7fdef8afb2a8>, 'x': array([ 0. ,  0.4,  0.8,  1.2,  1.6,  2. ,  2.4,  2.8,  3.2,  3.6,  4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362]), '__name__': '__main__', '__doc__': None}

Warning (from warnings module):
  File "/usr/lib/python2.7/dist-packages/matplotlib/font_manager.py", line 273
    warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')
UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.

======================== RESTART: /home/user/test1.py ========================
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, '__name__': '__main__', '__doc__': None}
{'cos': <ufunc 'cos'>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, 'sys': <module 'sys' (built-in)>, 'linspace': <function linspace at 0x7f089c040230>, 'x': array([ 0. ,  0.4,  0.8,  1.2,  1.6,  2. ,  2.4,  2.8,  3.2,  3.6,  4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362]), '__name__': '__main__', '__doc__': None}

======================== RESTART: /home/user/test1.py ========================
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, '__name__': '__main__', '__doc__': None}
{'cos': <ufunc 'cos'>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, 'sys': <module 'sys' (built-in)>, 'linspace': <function linspace at 0x7f4bdd59d230>, 'x': array([ 0. ,  0.4,  0.8,  1.2,  1.6,  2. ,  2.4,  2.8,  3.2,  3.6,  4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362]), '__name__': '__main__', '__doc__': None}

======================== RESTART: /home/user/test1.py ========================
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, '__name__': '__main__', '__doc__': None}
{'cos': <ufunc 'cos'>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, 'sys': <module 'sys' (built-in)>, 'linspace': <function linspace at 0x7f3da9c85230>, 'x': array([ 0. ,  0.4,  0.8,  1.2,  1.6,  2. ,  2.4,  2.8,  3.2,  3.6,  4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362]), '__name__': '__main__', '__doc__': None}

print(plt.plot.__doc__)


>>> print(plt.plot.__doc__)
Plot lines and/or markers to the
:class:`~matplotlib.axes.Axes`.  *args* is a variable length
argument, allowing for multiple *x*, *y* pairs with an
optional format string.  For example, each of the following is
legal::

    plot(x, y)        # plot x and y using default line style and color
    plot(x, y, 'bo')  # plot x and y using blue circle markers
    plot(y)           # plot y using x as index array 0..N-1
    plot(y, 'r+')     # ditto, but with red plusses

If *x* and/or *y* is 2-dimensional, then the corresponding columns
will be plotted.

If used with labeled data, make sure that the color spec is not
included as an element in data, as otherwise the last case
``plot("v","r", data={"v":..., "r":...)``
can be interpreted as the first case which would do ``plot(v, r)``
using the default line style and color.

If not used with labeled data (i.e., without a data argument),
an arbitrary number of *x*, *y*, *fmt* groups can be specified, as in::

    a.plot(x1, y1, 'g^', x2, y2, 'g-')

Return value is a list of lines that were added.

By default, each line is assigned a different style specified by a
'style cycle'.  To change this behavior, you can edit the
axes.prop_cycle rcParam.

The following format string characters are accepted to control
the line style or marker:

================    ===============================
character           description
================    ===============================
``'-'``             solid line style
``'--'``            dashed line style
``'-.'``            dash-dot line style
``':'``             dotted line style
``'.'``             point marker
``','``             pixel marker
``'o'``             circle marker
``'v'``             triangle_down marker
``'^'``             triangle_up marker
``'<'``             triangle_left marker
``'>'``             triangle_right marker
``'1'``             tri_down marker
``'2'``             tri_up marker
``'3'``             tri_left marker
``'4'``             tri_right marker
``'s'``             square marker
``'p'``             pentagon marker
``'*'``             star marker
``'h'``             hexagon1 marker
``'H'``             hexagon2 marker
``'+'``             plus marker
``'x'``             x marker
``'D'``             diamond marker
``'d'``             thin_diamond marker
``'|'``             vline marker
``'_'``             hline marker
================    ===============================


The following color abbreviations are supported:

==========  ========
character   color
==========  ========
'b'         blue
'g'         green
'r'         red
'c'         cyan
'm'         magenta
'y'         yellow
'k'         black
'w'         white
==========  ========

In addition, you can specify colors in many weird and
wonderful ways, including full names (``'green'``), hex
strings (``'#008000'``), RGB or RGBA tuples (``(0,1,0,1)``) or
grayscale intensities as a string (``'0.8'``).  Of these, the
string specifications can be used in place of a ``fmt`` group,
but the tuple forms can be used only as ``kwargs``.

Line styles and colors are combined in a single format string, as in
``'bo'`` for blue circles.

The *kwargs* can be used to set line properties (any property that has
a ``set_*`` method).  You can use this to set a line label (for auto
legends), linewidth, anitialising, marker face color, etc.  Here is an
example::

    plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
    plot([1,2,3], [1,4,9], 'rs',  label='line 2')
    axis([0, 4, 0, 10])
    legend()

If you make multiple lines with one plot command, the kwargs
apply to all those lines, e.g.::

    plot(x1, y1, x2, y2, antialiased=False)

Neither line will be antialiased.

You do not need to use format strings, which are just
abbreviations.  All of the line properties can be controlled
by keyword arguments.  For example, you can set the color,
marker, linestyle, and markercolor with::

    plot(x, y, color='green', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=12).

See :class:`~matplotlib.lines.Line2D` for details.

The kwargs are :class:`~matplotlib.lines.Line2D` properties:

  agg_filter: unknown
  alpha: float (0.0 transparent through 1.0 opaque) 
  animated: [True | False] 
  antialiased or aa: [True | False] 
  axes: an :class:`~matplotlib.axes.Axes` instance 
  clip_box: a :class:`matplotlib.transforms.Bbox` instance 
  clip_on: [True | False] 
  clip_path: [ (:class:`~matplotlib.path.Path`, :class:`~matplotlib.transforms.Transform`) | :class:`~matplotlib.patches.Patch` | None ] 
  color or c: any matplotlib color 
  contains: a callable function 
  dash_capstyle: ['butt' | 'round' | 'projecting'] 
  dash_joinstyle: ['miter' | 'round' | 'bevel'] 
  dashes: sequence of on/off ink in points 
  drawstyle: ['default' | 'steps' | 'steps-pre' | 'steps-mid' | 'steps-post'] 
  figure: a :class:`matplotlib.figure.Figure` instance 
  fillstyle: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none'] 
  gid: an id string 
  label: string or anything printable with '%s' conversion. 
  linestyle or ls: ['solid' | 'dashed', 'dashdot', 'dotted' | (offset, on-off-dash-seq) | ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` | ``' '`` | ``''``]
  linewidth or lw: float value in points 
  marker: :mod:`A valid marker style <matplotlib.markers>`
  markeredgecolor or mec: any matplotlib color 
  markeredgewidth or mew: float value in points 
  markerfacecolor or mfc: any matplotlib color 
  markerfacecoloralt or mfcalt: any matplotlib color 
  markersize or ms: float 
  markevery: [None | int | length-2 tuple of int | slice | list/array of int | float | length-2 tuple of float]
  path_effects: unknown
  picker: float distance in points or callable pick function ``fn(artist, event)`` 
  pickradius: float distance in points 
  rasterized: [True | False | None] 
  sketch_params: unknown
  snap: unknown
  solid_capstyle: ['butt' | 'round' |  'projecting'] 
  solid_joinstyle: ['miter' | 'round' | 'bevel'] 
  transform: a :class:`matplotlib.transforms.Transform` instance 
  url: a url string 
  visible: [True | False] 
  xdata: 1D array 
  ydata: 1D array 
  zorder: any number 

kwargs *scalex* and *scaley*, if defined, are passed on to
:meth:`~matplotlib.axes.Axes.autoscale_view` to determine
whether the *x* and *y* axes are autoscaled; the default is
*True*.

Notes
-----

In addition to the above described arguments, this function can take a
**data** keyword argument. If such a **data** argument is given, the
following arguments are replaced by **data[<arg>]**:

* All arguments with the following names: 'y', 'x'.




Additional kwargs: hold = [True|False] overrides default hold state
>>> 
======================== RESTART: /home/user/test1.py ========================
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, '__name__': '__main__', '__doc__': None}
{'cos': <ufunc 'cos'>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, 'sys': <module 'sys' (built-in)>, 'linspace': <function linspace at 0x7f570a98b230>, 'x': array([ 0. ,  0.4,  0.8,  1.2,  1.6,  2. ,  2.4,  2.8,  3.2,  3.6,  4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362]), '__name__': '__main__', '__doc__': None}
>>> 
======================== RESTART: /home/user/test1.py ========================
{'__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, '__name__': '__main__', '__doc__': None}
{'cos': <ufunc 'cos'>, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/test1.py', '__package__': None, 'sys': <module 'sys' (built-in)>, 'linspace': <function linspace at 0x7f2bef2fc230>, 'x': array([ 0. ,  0.4,  0.8,  1.2,  1.6,  2. ,  2.4,  2.8,  3.2,  3.6,  4. ]), 'y': array([ 1.        ,  0.92106099,  0.69670671,  0.36235775, -0.02919952,
       -0.41614684, -0.73739372, -0.94222234, -0.99829478, -0.89675842,
       -0.65364362]), '__name__': '__main__', '__doc__': None}
>>> 

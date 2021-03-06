import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib.animation import *
from PIL import ImageTk
from PIL import Image
import sys
from time import sleep

try:
	import tkinter as tk
	from tkinter.colorchooser import askcolor
except ImportError:
	import Tkinter as tk
	from tkColorChooser import askcolor

## 
sys.path.append('../In Development/')

sys.path.append('../Current Models/')
sys.path.append('../Current Models/Hyperbolic/')
sys.path.append('../Current Models/Misc./')
sys.path.append('../Current Models/Platonic Solids/')
sys.path.append('../Current Models/Surfaces/')
sys.path.append('../Current Models/Topological/')
sys.path.append('../Current Models/Two Space/')
sys.path.append('../Current Models/Archimedean/')

import prism, pyramid, sphere
import hyperbolic_octahedron, hyperbolic_paraboloid, one_sheet_hyperboloid, hyperbolic_helicoid, hyperbolic_cylinder
import three_dodecahedron, crescent, funnel, gabriel_horn, rose_spiral, shell, tesseract, spiral, seashell, steinbach_screw
import breather_surface, kuen_surface, steiner_surface, boys_surface, roman_surface, sine_surface, henneberg_surface, unk_surface, dini_surface, enneper_surface, corkscrew_surface, shoe_surface
import cube, dodecahedron, icosahedron, octahedron
import cross_cap, klein, mobius, torus
import neat, testing, vase, something_strange, great_dodecahedron
import cuboctahedron, great_rombicosidodecahedron, snub_cube, truncated_cube, hecatonicosihedron, great_icosahedron
import deltoid, log_spiral, parabola, penrose_square, penrose_circle, line, penrose_triangle

##
s = {	 "Prism"					: prism,
		 "Pyramid"					: pyramid,
		 "Sphere"					: sphere,

		 "Hyperbolic Octahedron"	: hyperbolic_octahedron,
		 "Hyperbolic Paraboloid"	: hyperbolic_paraboloid,
		 "One Sheet Hyperboloid"	: one_sheet_hyperboloid,
		 "Hyperbolic Cylinder"		: hyperbolic_cylinder,
		 "Hyperbolic Helicoid"		: hyperbolic_helicoid,

		 "Three Dodecahedon"		: three_dodecahedron,
		 "Crescent"					: crescent,
		 "Funnel"					: funnel,
		 "Gabriel's Horn"			: gabriel_horn,
		 "Rose Spiral"				: rose_spiral,
		 "Shell"					: shell,
		 "Tesseract"				: tesseract,
		 "Spiral"					: spiral,
		 "Seashell"					: seashell,
		 "Steinbach Screw"			: steinbach_screw,

		 "Breather's Surface"		: breather_surface,
		 "Kuen's Surface"			: kuen_surface,
		 "Steiner's Surface"		: steiner_surface,
		 "Boy's Surface"			: boys_surface,
		 "Roman Surface"			: roman_surface,
		 "Sine Surface"				: sine_surface,
		 "Henneberg's Surface"		: henneberg_surface,
		 "Dini's Surface"			: dini_surface,
		 "Enneper's Surface"		: enneper_surface,
		 "Corkscrew Surface"		: corkscrew_surface,
		 "Shoe Surface"				: shoe_surface,
		 "Unk Surface"				: unk_surface,

		 "Cube"						: cube,
		 "Dodecahedron"				: dodecahedron,
		 "Icosahedron"				: icosahedron,
		 "Octahedron"				: octahedron,

		 "Cross Cap"				: cross_cap,
		 "Klein Bottle"				: klein,
		 "Mobius Strip"				: mobius,
		 "Torus"					: torus,

		 "Neat"						: neat,
		 "Testing"					: testing,
		 "Great Dodecahedron"		: great_dodecahedron,
		 "Vase"						: vase,
		 "Something Strange"		: something_strange,

		 "Cuboctahedron"			: cuboctahedron,
		 "Hecatonicosihedron"		: hecatonicosihedron,
		 "Great Rombicosidodecahedron": great_rombicosidodecahedron,
		 "Snub Cube"				: snub_cube,
		 "Truncated Cube"			: truncated_cube,
		 "Great Icosahedron"		: great_icosahedron,

		 "Line"						: line,
		 "Deltoid"					: deltoid,
		 "Log Spiral"				: log_spiral,
		 "Parabola"					: parabola,
		 "Penrose Circle"			: penrose_circle,
		 "Penrose Square"			: penrose_square,
		 "Penrose Triangle"			: penrose_triangle,

}

gen 	= ["Prism", "Pyramid", "Sphere"]
hyper	= ["Hyperbolic Octahedron", "Hyperbolic Paraboloid", "One Sheet Hyperboloid", "Hyperbolic Cylinder", "Hyperbolic Helicoid"]
misc 	= ["Three Dodecahedron", "Crescent", "Funnel", "Gabriel's Horn", "Rose Spiral", "Shell", "Tesseract", "Spiral", "Seashell", "Steinbach Screw"]
surf 	= ["Breather's Surface", "Kuen's Surface", "Steiner's Surface", "Boy's Surface", "Roman Surface", "Sine Surface", "Henneberg's Surface", "Dini's Surface", "Enneper's Surface", "Corkscrew Surface", "Shoe Surface", "Unk Surface"]
topo 	= ["Cross Cap", "Klein Bottle", "Mobius Strip", "Torus"]
deve 	= ["Neat", "Testing", "Great Dodecahedron", "Vase", "Something Strange"]
arch 	= ["Cuboctahedron", "Hecatonicosihedron", "Great Rombicosidodecahedron", "Snub Cube", "Truncated Cube", "Great Icosahedron"]
plat    = ["Cube", "Dodecahedron", "Octahedron", "Icosahedron"]
two 	= ["Line", "Deltoid", "Log Spiral", "Parabola"]
pen		= ["Penrose Circle", "Penrose Triangle", "Penrose Square"]

dim = "#303030"  #   Background
dimf = "#00C0FF"  #   Font Color

disa = "#d400ff" #   Disabled Text

class Geometry(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self,master)
		self.createWidgets()

	def createWidgets(self):
		global icon
		self.fig = plt.figure(figsize=(8, 8), facecolor="black", edgecolor="white")
		ax = p3.Axes3D(self.fig)
		ax.set_facecolor('black')
		plt.axis("off")

		canvas = FigureCanvasTkAgg(self.fig,root)
		canvas.get_tk_widget().grid(row=0,column=0, sticky='new')	
		root.update_idletasks()
		canvas.draw()

# 		# Vars

		self.grid_axis 		= tk.StringVar()
		self.axis_limits 	= tk.StringVar()
		self.scroll			= tk.DoubleVar()
		self.shape_set 		= tk.StringVar()
		self.alpha 			= tk.StringVar()
		self.two_three 		= tk.StringVar()
		self.rot 			= tk.StringVar()
		self.format_save 	= tk.StringVar()

# 		# Functions
		def axi():
			plt.axis(str(self.grid_axis.get()))
			plt.xlabel("X-Axis", color="white")
			plt.ylabel("Y-Axis", color="white")
			ax.set_zlabel("Z-Axis", color="white")
			plt.xticks(color="white")
			plt.yticks(color="white")

		def space():
			plt.figure(1)
			plt.gca()
			ax.set_facecolor('white')
			plt.axis('on')

		def adjust():
			root.geometry("800x800+520+280")

		def FaceColor(self):
			self.c_entry = askcolor(parent=self, title="Face Color")[1]
			self.fck.config(bg=self.c_entry, text=str(self.c_entry))
			return self.c_entry

		def FaceColor2(self):
			self.c_entry2 = askcolor(title="Face Color 2")[1]
			self.f2.config(bg=self.c_entry2, text=str(self.c_entry2))
			return self.c_entry2

		def FaceColor3(self):
			self.c_entry3 = askcolor(title="Face Color 3")[1]
			self.f3.config(bg=self.c_entry3, text=str(self.c_entry3))
			return self.c_entry3

		def EdgeColor(self):
			self.ec_entry = askcolor(title="Edge Color")[1]
			self.eck.config(bg=self.ec_entry, text=str(self.ec_entry))
			return self.ec_entry
#
		def popup_shape():
			top = tk.Toplevel(self)
			top.title("Shapes")
			top.config(background=dim)
			top.tk.call('wm', 'iconphoto', top._w, icon)

			pop = tk.Button(top, text="POP!", command=top.destroy)
			pop.grid(row=0, column=0, sticky='new')
			pop.config(bg=dim,fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

			plotter = tk.Button(top, text="Plot", command=lambda: self.plot(canvas, ax))
			plotter.grid(row=0, column=2, sticky="new")
			plotter.config(bg=dim,fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

			if self.two_three.get() == "3d":
				for n in range(len(gen)):
					tk.Radiobutton(top, text=gen[n], variable=self.shape_set, value=gen[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim).grid(row=n+1, column=0, sticky='w')

				##
				hyperbolic = tk.Label(top, text="--- Hyperbolic Objects ---", font=('Times', 12, 'bold'))
				hyperbolic.grid(row=4, column=0, sticky="nsew")
				hyperbolic.config(bg=dim, fg=dimf, activebackground=dim)

				for n in range(len(hyper)):
					tk.Radiobutton(top, text=hyper[n], variable=self.shape_set, value=hyper[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim).grid(row=n+5, column=0, sticky='w')

				##
				miscellaneous = tk.Label(top, text="--- Miscellaneous ---", font=('Times', 12, 'bold'))
				miscellaneous.grid(row=10, column=0, sticky='nsew')
				miscellaneous.config(bg=dim, fg=dimf, activebackground=dim)

				for n in range(len(misc)):
					tk.Radiobutton(top, text=misc[n], variable=self.shape_set, value=misc[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim).grid(row=n+11, column=0, sticky='w')

				##
				surface = tk.Label(top, text="--- Surfaces ---", font=('Times', 12, 'bold'))
				surface.grid(row=1, column=2, sticky='new')
				surface.config(bg=dim, fg=dimf, activebackground=dim)
				for n in range(len(surf)):
					tk.Radiobutton(top, text=surf[n], variable=self.shape_set, value=surf[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim).grid(row=n+2, column=2, sticky='w')

				##
				topological = tk.Label(top, text="--- Topological ---", font=('Times', 12, 'bold'))
				topological.grid(row=14, column=2, sticky='nsew')
				topological.config(bg=dim, fg=dimf, activebackground=dim)
				for n in range(len(topo)):
					tk.Radiobutton(top, text=topo[n], variable=self.shape_set, value=topo[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim).grid(row=n+15, column=2, sticky='w')

				##
				development = tk.Label(top, text="--- In Development ---", font=('Times', 12, 'bold'))
				development.grid(row=1, column=4, sticky='nsew')
				development.config(bg=dim, fg=dimf, activebackground=dim)
				for n in range(len(deve)):
					tk.Radiobutton(top, text=deve[n], variable=self.shape_set, value=deve[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim).grid(row=n+2, column=4, sticky='w')

				##
				archimedean = tk.Label(top, text="--- Archimedean Solids ---", font=('Times', 12, 'bold'))
				archimedean.grid(row=1, column=5, sticky='nsew')
				archimedean.config(bg=dim, fg=dimf, activebackground=dim)
				for n in range(len(arch)):
					tk.Radiobutton(top, text=arch[n], variable=self.shape_set, value=arch[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim).grid(row=n+2, column=5, sticky='w')
			
				##
				platonic = tk.Label(top, text="--- Platonic Solids ---", font=('Times', 12, 'bold'))
				platonic.grid(row=9, column=5, sticky='nsew')
				platonic.config(bg=dim, fg=dimf, activebackground=dim)
				for n in range(len(plat)):
					tk.Radiobutton(top, text=plat[n], variable=self.shape_set, value=plat[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim).grid(row=n+10, column=5, sticky='w')

				# cube_hover = CreateToolTip(cube, ImageTk.PhotoImage(file="./Visual/Cube.png"),"test")

				self.shape_set.set("Unk Surface")

			elif self.two_three.get() == "2d":
				for n in range(len(two)):
					tk.Radiobutton(top, text=two[n], variable=self.shape_set, value=two[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim).grid(row=n+1, column=0, sticky='w')

				penrose = tk.Label(top, text="--- Penrose Projections ---", font=('Times', 12, 'bold'))
				penrose.grid(row=1, column=2, sticky='nsew')
				penrose.config(bg=dim, fg=dimf, activebackground=dim)
				for n in range(len(pen)):
					tk.Radiobutton(top, text=pen[n], variable=self.shape_set, value=pen[n], bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,selectcolor=dim).grid(row=n+2, column=2, sticky='w')

	#
		def popup_save():
			top = tk.Toplevel(self)
			top.title("Save Figure")
			top.tk.call('wm', 'iconphoto', top._w, icon)
			top.config(background=dim)

			top.update_idletasks()
			top.update()

			pop = tk.Button(top, text="POP!", command=top.destroy)
			pop.grid(row=0, column=0)
			pop.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

			self.format_save = tk.StringVar()

			def vid():
				plt.axis("off")
				ax.set_facecolor('black')
				ax.grid(False)
				ax.axis('off')
				ax.set_xticks([])
				ax.set_yticks([])
				ax.set_zticks([])

				plt.axis('off')
				plt.axis('equal')

				def init():
					return testing.test,

				def animate(i):
					ax.view_init(elev=i, azim=i)
					return testing.test,

			#            Animate
				ani = FuncAnimation(self.fig, animate, init_func=init, interval=1, frames=500, repeat=True)

				Writer = writers['ffmpeg']
				writer = Writer(fps=15, bitrate=1800)
				ani.save('{}.{}'.format(s[self.shape_set.get(), self.format_save.get()]),writer=writer)

				plt.ion()
				plt.show()
				sleep(0)
				plt.close()

			clt = tk.Radiobutton(top, text="Transparent On")
			clt.grid(row=1, column=2)
			clt.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,
					   selectcolor=dim)

			clf = tk.Radiobutton(top, text="Transparent Off")
			clf.grid(row=2, column=2)
			clf.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0,  activeforeground=dimf,
					   selectcolor=dim)

			png = tk.Radiobutton(top, text="png", variable=self.format_save, value="png", width=5)
			png.grid(row=1, column=0)
			png.config(bg=dim, fg=dimf, activebackground=dim,  highlightthickness=0, activeforeground=dimf,
					   selectcolor=dim)

			jpg = tk.Radiobutton(top, text="jpg", variable=self.format_save, value="jpg", width=5)
			jpg.grid(row=1, column=1)
			jpg.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,
					   selectcolor=dim)

			mp4 = tk.Radiobutton(top, text="mp4", variable=self.format_save,    value="mp4", width=5)
			mp4.grid(row=2, column=0)
			mp4.config(bg=dim, 	fg=dimf, activebackground=dim,  highlightthickness=0, activeforeground=dimf, selectcolor=dim)

			save_img = tk.Button(top, text="save img")
			save_img.grid(row=0, column=1)
			save_img.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

			save_img.config(command=lambda: plt.savefig("{}.{}".format(s[self.shape_set.get()].name, self.format_save.get()),  transparent=True))

			save_vid = tk.Button(top, text="save video")
			save_vid.grid(row=0, column=2)
			save_vid.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)

			self.format_save.set("png")

			top.update()
			top.update_idletasks()
			top.mainloop()

		menu = tk.Menu(root)
		root.config(menu=menu)

		filemenu = tk.Menu(menu)
		menu.add_cascade(label="File", menu=filemenu)

		filemenu.add_command(label="Save", command=popup_save)
		filemenu.add_separator()
		filemenu.add_command(label="Quit", command=quit)

		menu.add_command(label="Figure", command=adjust)
		menu.add_command(label="Full", command=lambda: root.geometry("1232x801"))

	# 	# # Transparency
		self.a_label = tk.Label(root, text="Transparency")
		self.a_label.grid(row=0, column=1, sticky='nw', pady=110)
		self.a_entry = tk.Scale(root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL)
		self.a_entry.grid(row=0, column=2, sticky='nw', pady=90)
		self.a_entry.set(0.4)
	#
	# 	# # Height
		self.h_label = tk.Label(root, text="Height")
		self.h_label.grid(row=0, column=3, sticky='nw', pady=110, padx=10)
		self.h_entry = tk.Scale(root, from_=1, to=10, resolution=0.1, orient=tk.HORIZONTAL)
		self.h_entry.grid(row=0, column=4, sticky='nw', pady=90)
		self.h_entry.set(1)
	#
	# 	# Entry of the number of sides
		self.si_label = tk.Label(root, text="Number of Sides")
		self.si_label.grid(row=0, column=1, sticky='nw', pady=150)
		self.si_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.si_entry.grid(row=0, column=2, sticky='nw', pady=130)
		self.si_entry.set(20)
	#
	# 	# Entry of the number of edges
		self.ed_label = tk.Label(root, text="Number of Edges")
		self.ed_label.grid(row=0, column=1, sticky='nw', pady=190)
		self.ed_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.ed_entry.grid(row=0, column=2, sticky='nw', pady=170)
		self.ed_entry.set(2)

	# 	# Multiple of Pi
		self.pi_label = tk.Label(root, text=r"Multiple of " u'\u03C0')
		self.pi_label.grid(row=0, column=1, sticky='nw', pady=230)
		self.pi_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.pi_entry.grid(row=0, column=2, sticky='nw', pady=210)
		self.pi_entry.set(2)
	#
	# 	# Edge Width
		self.ew_label = tk.Label(root, text="Edge Width")
		self.ew_label.grid(row=0, column=1, sticky='nw', pady=270)
		self.ew_entry = tk.Scale(root, from_=0, to=10, resolution=0.5, orient=tk.HORIZONTAL)
		self.ew_entry.grid(row=0, column=2, sticky='nw', pady=250)
		self.ew_entry.set(1)
	#
	# 	# Radius
		self.ram_label = tk.Label(root, text="Radius (Main)")
		self.ram_label.grid(row=0, column=3, sticky='nw', pady=150, padx=10)
		self.ram_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.ram_entry.grid(row=0, column=4, sticky='nw', pady=130)
	#
	# 	# Radius
		self.raa_label = tk.Label(root, text="Radius (Alt)")
		self.raa_label.grid(row=0, column=3, sticky='nw', pady=190, padx=10)
		self.raa_entry = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL)
		self.raa_entry.grid(row=0, column=4, sticky='nw', pady=170)

		# Edge Color
		self.edge = tk.Button(text="Edge Color", command=lambda: EdgeColor(self))
		self.edge.grid(row=0, column=1, sticky='new', pady=30, padx=0)

		self.eck = tk.Message(root, width=200000000,
							  text=" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ", borderwidth=5,
							  relief=tk.GROOVE)
		self.eck.grid(row=0, column=1, sticky='new', pady=60)

		# Face Color
		self.face = tk.Button(text="Face Color", command=lambda: FaceColor(self))
		self.face.grid(row=0, column=2, sticky='new', pady=30, padx=0)

		self.fck = tk.Message(root, width=200000000,
							  text=" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ", borderwidth=5,
							  relief=tk.GROOVE)
		self.fck.grid(row=0, column=2, sticky='new', pady=60, padx=0)

		# Edge Color
		self.face2 = tk.Button(text="Face Color 2", command=lambda: FaceColor2(self), state=tk.NORMAL)
		self.face2.grid(row=0, column=3, sticky='new', pady=30, padx=0)

		self.f2 = tk.Message(root, width=2000000, text=" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ",
							 borderwidth=5, relief=tk.GROOVE)
		self.f2.grid(row=0, column=3, sticky='new', pady=60, padx=0)

		# Face Color
		self.face3 = tk.Button(text="Face Color 3", command=lambda: FaceColor3(self), state=tk.NORMAL)
		self.face3.grid(row=0, column=4, sticky='new', pady=30, padx=0)

		self.f3 = tk.Message(root, width=2000000, text=" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ",
							 borderwidth=5, relief=tk.GROOVE)
		self.f3.grid(row=0, column=4, sticky='new', pady=60, padx=0)

		# Plotting,
		self.plotting = tk.Button(root, text="Update", command=lambda: self.plot(canvas, ax), height=4)
		self.plotting.grid(row=0, column=1, columnspan=2, sticky="new", pady=430)

	# 	# Grid Functions (on/off)
		self.grid_on = tk.Radiobutton(root, text="Grid On", variable=self.grid_axis, value='on', command=axi)
		self.grid_on.grid(row=0, column=1, sticky='n')

		self.grid_off = tk.Radiobutton(root, text='Grid Off', variable=self.grid_axis, value='off', command=axi)
		self.grid_off.grid(row=0, column=2, sticky='n')
		self.grid_axis.set('off')
	#
	# 	# 2D or 3D
		self.two_space = tk.Radiobutton(root, text="2D", variable=self.two_three, value='2d', command=space)
		self.two_space.grid(row=0, column=2, sticky='nw', pady=350)

		self.three_space = tk.Radiobutton(root, text="3D", variable=self.two_three, value='3d', command=space)
		self.three_space.grid(row=0, column=2, sticky='nw', pady=380)
		self.two_three.set('3d')
	#
	# 	# Rotation
		self.rot_on = tk.Radiobutton(root, text="Rot On", variable=self.rot, value='on')
		self.rot_on.grid(row=0, column=3, sticky='new')

		self.rot_off = tk.Radiobutton(root, text='Rot Off', variable=self.rot, value='off')
		self.rot_off.grid(row=0, column=4, sticky='new')

	# 	# Shape Popup
		self.shapes = tk.Button(root, text="Shapes", command=popup_shape, height=4)
		self.shapes.grid(row=0, column=3, columnspan=2, sticky='new', pady=430)

		def dark(self):
			scales = [self.a_entry, self.h_entry, self.si_entry, self.ed_entry, self.pi_entry, self.ew_entry,
					  self.ram_entry, self.raa_entry]
			labels = [self.a_label, self.h_label, self.si_label, self.ed_label, self.pi_label, self.ew_label,
					  self.ram_label, self.raa_label]
			radio = [self.grid_on, self.grid_off, self.two_space, self.three_space, self.rot_on, self.rot_off]
			button = [self.plotting, self.face, self.face2, self.face3, self.edge, self.shapes]
			menus = [menu, filemenu]
			root.config(background=dim)

			for m in scales:
				m.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, troughcolor=dimf)
			for n in labels:
				n.config(bg=dim, fg=dimf, activebackground=dim)
			for o in radio:
				o.config(bg=dim, fg=dimf, activebackground=dim, highlightthickness=0, activeforeground=dimf,
						 selectcolor=dim)
			for p in button:
				p.config(bg=dim, fg=dimf, activebackground=dim, highlightbackground=dimf, activeforeground=dimf)
			for q in menus:
				q.config(bg=dim, fg=dimf, activebackground=dim, activeforeground=dimf)
		return dark(self)
	#
	def plot(self, canvas, ax):
		try:
			edge_c = self.ec_entry
		except AttributeError:
			edge_c = "#f608ff"
			self.eck.config(bg=edge_c, text=str(edge_c))
		try:
			color = self.c_entry
		except AttributeError:
			color = "#00c4ff"
			self.fck.config(bg=color,text=str(color))
		try:
			color2 = self.c_entry2
		except AttributeError:
			color2 = "#000001"
			self.f2.config(bg=color2, text=str(color2))
		try:
			color3 = self.c_entry3
		except AttributeError:
			color3 = "#000000"
			self.f3.config(bg=color3, text=str(color3))

		alpha = self.a_entry.get()
		grid = self.grid_axis.get()
		edge_w = self.ew_entry.get()
		edges = self.ed_entry.get()
		sides = self.si_entry.get()
		multi_pi = self.pi_entry.get()
		radiusa = self.raa_entry.get()
		radiusm = self.ram_entry.get()
		rot = self.rot.get()
		save = self.format_save.get()
		height = self.h_entry.get()

		name = self.shape_set.get()
		root.title("GeoMetrics ({})".format(name))

		ax.clear()
		plt.cla()
		plt.clf()

		try:  # Count: 14
			s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, radiusm,
										  radiusa, color2, color3, height, rot, save)
		except KeyError:

			root.title("GeoMetrics (Testing)")
			testing.shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi, rot)
			active = [self.a_entry, self.si_entry, self.ed_entry, self.pi_entry]
			active_label = [self.a_label, self.si_label, self.ed_label, self.pi_label]
			disable = [self.ram_entry, self.raa_entry, self.h_entry]
			disable_label = [self.ram_label, self.raa_label, self.h_label]
			color = [self.face2, self.face3]
			color_label = [self.f2, self.f3]

			for m in disable:
				m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
				for n in disable_label:
					n.config(fg=disa)
					for o in color:
						o.config(state=tk.DISABLED, highlightbackground=disa)
						for p in color_label:
							p.config(bg=dim, fg=dim, relief=tk.RIDGE)
			for m in active:
				m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
				self.face.config(state=tk.ACTIVE, highlightbackground=dimf)
				for n in active_label:
					n.config(fg=dimf)
					self.fck.config(relief=tk.GROOVE)
		except TypeError:
			try:  # Count: 12
				s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi,
											  radiusm, radiusa, height)

				active 			= [self.a_entry, self.si_entry, self.ed_entry, self.pi_entry, self.raa_entry, self.ram_entry, self.h_entry]
				active_label 	= [self.a_label, self.si_label, self.ed_label, self.pi_label, self.raa_label, self.ram_label,
									self.h_label]
				color 			= [self.face2, self.face3]
				color_label 	= [self.f2, self.f3]

				for n in color:
					n.config(state=tk.DISABLED, highlightbackground=disa)
					for m in color_label:
						m.config(bg=dim, fg=dim, relief=tk.RIDGE)

				for n in active:
					n.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
					self.face.config(state=tk.ACTIVE, highlightbackground=dimf)
					for m in active_label:
						m.config(fg=dimf)
						self.fck.config(relief=tk.GROOVE)
			except TypeError:
				try:  # Count: 11
					s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges, multi_pi,
												  radiusm, height)
					active = [self.a_entry, self.si_entry, self.ed_entry, self.pi_entry, self.ram_entry, self.h_entry]
					active_label = [self.a_label, self.si_label, self.ed_label, self.pi_label, self.ram_label, self.h_label]
					disable = [self.raa_entry]
					disable_label = [self.raa_label]
					color = [self.face2, self.face3]
					color_label = [self.f2, self.f3]

					for m in disable:
						m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
						for n in disable_label:
							n.config(fg=disa)
							for o in color:
								o.config(state=tk.DISABLED, highlightbackground=disa)
								for p in color_label:
									p.config(bg=dim, fg=dim, relief=tk.RIDGE)

					for m in active:
						m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
						self.face.config(state=tk.ACTIVE, highlightbackground=dimf)
						for n in active_label:
							n.config(fg=dimf)
							self.fck.config(relief=tk.GROOVE)

				except TypeError:
					try:  # Count: 10
						s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges,
													  multi_pi, radiusm)
						active = [self.a_entry, self.si_entry, self.ed_entry, self.pi_entry, self.ram_entry]
						active_label = [self.a_label, self.si_label, self.ed_label, self.pi_label, self.ram_label]
						disable = [self.raa_entry, self.h_entry]
						disable_label = [self.raa_label, self.h_label]
						color = [self.face2, self.face3]
						color_label = [self.f2, self.f3]

						for m in disable:
							m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
							for n in disable_label:
								n.config(fg=disa)
								for o in color:
									o.config(state=tk.DISABLED, highlightbackground=disa)
									for p in color_label:
										p.config(bg=dim, fg=dim, relief=tk.RIDGE)

						for m in active:
							m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
							self.face.config(state=tk.ACTIVE, highlightbackground=dimf)
							for n in active_label:
								n.config(fg=dimf)
								self.fck.config(relief=tk.GROOVE)

					except TypeError:
						try:  # Count: 9
							s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides, edges,
														  multi_pi)
							active = [self.a_entry, self.si_entry, self.ed_entry, self.pi_entry]
							active_label = [self.a_label, self.si_label, self.ed_label, self.pi_label]
							disable = [self.raa_entry, self.h_entry, self.ram_entry]
							disable_label = [self.raa_label, self.h_label, self.ram_label]
							color = [self.face2, self.face3]
							color_label = [self.f2, self.f3]

							for m in disable:
								m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
								for n in disable_label:
									n.config(fg=disa)
									for o in color:
										o.config(state=tk.DISABLED, highlightbackground=disa)
										for p in color_label:
											p.config(bg=dim, fg=dim, relief=tk.RIDGE)

							for m in active:
								m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
								self.face.config(state=tk.ACTIVE, highlightbackground=dimf)
								for n in active_label:
									n.config(fg=dimf)
									self.fck.config(relief=tk.GROOVE)

						except TypeError:
							try:  # Count: 8
								s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, radiusm,
															  color2)
								active = [self.a_entry, self.ram_entry]
								active_label = [self.a_label, self.ram_label]
								disable = [self.si_entry, self.ed_entry, self.pi_entry, self.raa_entry, self.h_entry]
								disable_label = [self.si_label, self.ed_label, self.pi_label, self.raa_label,
												 self.h_label]
								color = [self.face2, self.face3]
								color_label = [self.f2, self.f3]

								for m in disable:
									m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
									for n in disable_label:
										n.config(fg=disa)
										for o in color:
											self.face3.config(state=tk.DISABLED, highlightbackground=disa)
											for p in color_label:
												self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)

								for m in active:
									m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
									for n in active_label:
										n.config(fg=dimf)
										for o in color:
											self.face2.config(state=tk.ACTIVE, highlightbackground=dimf)
											self.face.config(state=tk.ACTIVE, highlightbackground=dimf)
											for p in color_label:
												self.f2.config(relief=tk.GROOVE)
												self.fck.config(relief=tk.GROOVE)

							except ValueError:
								s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, sides,
															  edges)
								active = [self.a_entry, self.si_entry, self.ed_entry]
								active_label = [self.a_label, self.si_label, self.ed_label]
								disable = [self.pi_entry, self.raa_entry, self.h_entry, self.ram_entry]
								disable_label = [self.pi_label, self.raa_label, self.h_label, self.ram_label]
								color = [self.face2, self.face3]
								color_label = [self.f2, self.f3]

								for m in disable:
									m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
									for n in disable_label:
										n.config(fg=disa)
										for o in color:
											o.config(state=tk.DISABLED, highlightbackground=disa)
											for p in color_label:
												p.config(bg=dim, fg=dim, relief=tk.RIDGE)

								for m in active:
									m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
									self.face.config(state=tk.ACTIVE, highlightbackground=dimf)
									for n in active_label:
										n.config(fg=dimf)
										self.fck.config(relief=tk.GROOVE)

							except TypeError:
								try:  # Count: 8
									s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, color2,
																  color3)
									active  = [self.a_entry]
									active_label = [self.a_label]
									disable = [self.pi_entry, self.raa_entry, self.h_entry, self.ram_entry,
											   self.si_entry, self.ed_entry]
									disable_label = [self.pi_label, self.raa_label, self.h_label, self.ram_label,
													 self.si_label, self.ed_label]
									color = [self.face2, self.face3]
									color_label = [self.f2, self.f3]

									for m in disable:
										m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim,
												 troughcolor=dim)
										for n in disable_label:
											n.config(fg=disa)
											for o in color:
												o.config(state=tk.ACTIVE, highlightbackground=dimf)
												for p in color_label:
													p.config(relief=tk.GROOVE)
									for m in active:
										m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim, troughcolor=dimf)
										self.face.config(state=tk.ACTIVE, highlightbackground=dimf)
										for n in active_label:
											n.config(fg=dimf)
											self.fck.config(relief=tk.GROOVE)

								except TypeError:
									try:  # Count:7
										s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid, radiusm)
										active = [self.ram_entry, self.a_entry]
										active_label = [self.ram_label, self.a_label]
										disable = [self.pi_entry, self.raa_entry, self.h_entry, self.si_entry,
												   self.ed_entry]
										disable_label = [self.pi_label, self.raa_label, self.h_label, self.si_label,
														 self.ed_label]
										color = [self.face2, self.face3]
										color_label = [self.f2, self.f3]

										for m in disable:
											m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim,
													 troughcolor=dim)
											for n in disable_label:
												n.config(fg=disa)
												for o in color:
													o.config(state=tk.DISABLED, highlightbackground=disa)
													for p in color_label:
														p.config(bg=dim, fg=dim, relief=tk.RIDGE)

										for m in active:
											m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim,
													 troughcolor=dimf)
											self.face.config(state=tk.ACTIVE, highlightbackground=dimf)
											for n in active_label:
												n.config(fg=dimf)
												self.fck.config(relief=tk.GROOVE)

									except TypeError:
										try:  # Count: 7
											s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w, grid,
																		  color2)
											active  = [self.a_entry]
											active_label = [self.a_label]
											disable = [self.pi_entry, self.raa_entry, self.h_entry, self.si_entry,
													   self.ed_entry, self.ram_entry]
											disable_label = [self.pi_label, self.raa_label, self.h_label, self.si_label,
															 self.ed_label, self.ram_label]
											color = [self.face2, self.face3]
											color_label = [self.f2, self.f3]

											for m in disable:
												m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim,
														 troughcolor=dim)
												for n in disable_label:
													n.config(fg=disa)
													for o in color:
														self.face3.config(state=tk.DISABLED, highlightbackground=disa)
														for p in color_label:
															self.f3.config(bg=dim, fg=dim, relief=tk.RIDGE)

											for m in active:
												m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim,
														 troughcolor=dimf)
												for n in active_label:
													n.config(fg=dimf)
													for o in color:
														self.face2.config(state=tk.ACTIVE, highlightbackground=dimf)
														self.face.config(state=tk.ACTIVE, highlightbackground=dimf)
														for p in color_label:
															self.f2.config(relief=tk.GROOVE)
															self.fck.config(relief=tk.GROOVE)

										except TypeError:
											try:  # Count: 6
												s[self.shape_set.get()].shape(self.fig, alpha, color, edge_c, edge_w,
																			  grid)
												active  = [self.a_entry]
												active_label = [self.a_label]
												disable = [self.pi_entry, self.raa_entry, self.h_entry, self.si_entry,self.ed_entry, self.ram_entry]
												disable_label = [self.pi_label, self.raa_label, self.h_label, self.si_label, self.ed_label, self.ram_label]
												color = [self.face2, self.face3]
												color_label = [self.f2, self.f3]

												for m in disable:
													m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim,
															 troughcolor=dim)
													for n in disable_label:
														n.config(fg=disa)
														for o in color:
															o.config(state=tk.DISABLED, highlightbackground=disa)
															for p in color_label:
																p.config(bg=dim, fg=dim, relief=tk.RIDGE)
												for m in active:
													m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim,
														 troughcolor=dimf)
													self.face.config(state=tk.ACTIVE, highlightbackground=dimf)
													for n in active_label:
														n.config(fg=dimf)
														self.fck.config(relief=tk.GROOVE)

											except TypeError:
												try:
													s[self.shape_set.get()].shape(self.fig, edge_c, edge_w, grid)
													disable 	  = [self.pi_entry, self.raa_entry, self.h_entry, self.si_entry, self.ed_entry,  self.a_entry, self.ram_entry]
													disable_label = [self.pi_label, self.raa_label, self.h_label, self.si_label, self.ed_label, self.a_label, self.ram_label]
													color 		  = [self.face, self.face2, self.face3]
													color_label   = [self.fck, self.f2, self.f3]

													for m in disable:
														m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
														for n in disable_label:
															n.config(fg=disa)
															for o in color:
																o.config(state=tk.DISABLED, highlightbackground=disa)
																for p in color_label:
																	p.config(bg=dim, fg=dim, relief=tk.RIDGE)
												except TypeError:
													try:
														s[self.shape_set.get()].shape(self.fig, edge_c, edge_w, grid, radiusm)
														active 		  = [self.ram_entry]
														active_label  = [self.ram_label]
														disable 	  = [self.pi_entry, self.raa_entry, self.h_entry, self.si_entry, self.ed_entry,  self.a_entry]
														disable_label = [self.pi_label, self.raa_label, self.h_label, self.si_label, self.ed_label, self.a_label]
														color 		  = [self.face, self.face2, self.face3]
														color_label   = [self.fck, self.f2, self.f3]

														for m in disable:
															m.config(state=tk.DISABLED, bg=dim, fg=dim, activebackground=dim, troughcolor=dim)
															for n in disable_label:
																n.config(fg=disa)
																for o in color:
																	o.config(state=tk.DISABLED, highlightbackground=disa)
																	for p in color_label:
																		p.config(bg=dim, fg=dim, relief=tk.RIDGE)

														for m in active:
															m.config(state=tk.ACTIVE, bg=dim, fg=dimf, activebackground=dim,troughcolor=dimf)
															for n in active_label:
																n.config(fg=dimf)

													except TypeError:
														print("Welp")



		canvas.draw()


if __name__ == '__main__':
	root = tk.Tk()

	root.title("GeoMetrics")
	root.geometry("1232x801")
	icon = ImageTk.PhotoImage(file='icon.png')

	def quit():
		global root
		root.quit()
		root.destroy()


	root.tk.call('wm', 'iconphoto', root._w, icon)
	root.protocol("WM_DELETE_WINDOW", quit)
	root.update()
	root.update_idletasks()

	def quit():
		global root
		root.quit()
		root.destroy()

	geo = Geometry(master=root)
	geo.mainloop()

'''
Created on 2015/07/27

@author: smallcat
'''

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# 
# def data_gen():
#     t = data_gen.t
#     cnt = 0
#     while cnt < 1000:
#         cnt+=1
#         t += 0.05
#         yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
# data_gen.t = 0
# 
# fig, ax = plt.subplots()
# line, = ax.plot([], [], lw=2)
# ax.set_ylim(-1.1, 1.1)
# ax.set_xlim(0, 5)
# ax.grid()
# xdata, ydata = [], []
# def run(data):
#     # update the data
#     t,y = data
#     xdata.append(t)
#     ydata.append(y)
#     xmin, xmax = ax.get_xlim()
# 
#     if t >= xmax:
#         ax.set_xlim(xmin, 2*xmax)
#         ax.figure.canvas.draw()
#     line.set_data(xdata, ydata)
# 
#     return line,
# 
# ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,
#     repeat=False)
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# 
# def update_line(num, data, line):
#     line.set_data(data[...,:num])
#     return line,
# 
# fig1 = plt.figure()
# 
# data = np.random.rand(2, 25)
# l, = plt.plot([], [], 'r-')
# plt.xlim(0, 1)
# plt.ylim(0, 1)
# plt.xlabel('x')
# plt.title('test')
# line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l),
#     interval=50, blit=True)
# #line_ani.save('lines.mp4')
# 
# fig2 = plt.figure()
# 
# x = np.arange(-9, 10)
# y = np.arange(-9, 10).reshape(-1, 1)
# base = np.hypot(x, y)
# ims = []
# for add in np.arange(15):
#     ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))
# 
# im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000,
#     blit=True)
# #im_ani.save('im.mp4', metadata={'artist':'Guido'})
# 
# plt.show()




# #!/usr/bin/env python
# """
# An animated image
# """
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# 
# fig = plt.figure()
# 
# def f(x, y):
#     return np.sin(x) + np.cos(y)
# 
# x = np.linspace(0, 2 * np.pi, 120)
# y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
# 
# im = plt.imshow(f(x, y), cmap=plt.get_cmap('jet'))
# 
# def updatefig(*args):
#     global x,y
#     x += np.pi / 15.
#     y += np.pi / 20.
#     im.set_array(f(x,y))
#     return im,
# 
# ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
# plt.show()



# 
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# 
# fig, ax = plt.subplots()
# line, = ax.plot(np.random.rand(10))
# ax.set_ylim(0, 1)
# 
# def update(data):
#     line.set_ydata(data)
#     return line,
# 
# def data_gen():
#     while True: yield np.random.rand(10)
# 
# ani = animation.FuncAnimation(fig, update, data_gen, interval=100)
# plt.show()




# #!/usr/bin/env python
# """
# An example of how to use wx or wxagg in an application with a custom
# toolbar
# """
# 
# # Used to guarantee to use at least Wx2.8
# import wxversion
# wxversion.ensureMinimal('2.8')
# 
# from numpy import arange, sin, pi
# 
# import matplotlib
# 
# matplotlib.use('WXAgg')
# from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg
# 
# from matplotlib.backends.backend_wx import _load_bitmap
# from matplotlib.figure import Figure
# from numpy.random import rand
# 
# import wx
# 
# 
# class MyNavigationToolbar(NavigationToolbar2WxAgg):
#     """
#     Extend the default wx toolbar with your own event handlers
#     """
#     ON_CUSTOM = wx.NewId()
#     def __init__(self, canvas, cankill):
#         NavigationToolbar2WxAgg.__init__(self, canvas)
# 
#         # for simplicity I'm going to reuse a bitmap from wx, you'll
#         # probably want to add your own.
#         self.AddSimpleTool(self.ON_CUSTOM, _load_bitmap('stock_left.xpm'),
#                            'Click me', 'Activate custom contol')
#         wx.EVT_TOOL(self, self.ON_CUSTOM, self._on_custom)
# 
#     def _on_custom(self, evt):
#         # add some text to the axes in a random location in axes (0,1)
#         # coords) with a random color
# 
#         # get the axes
#         ax = self.canvas.figure.axes[0]
# 
#         # generate a random location can color
#         x,y = tuple(rand(2))
#         rgb = tuple(rand(3))
# 
#         # add the text and draw
#         ax.text(x, y, 'You clicked me',
#                 transform=ax.transAxes,
#                 color=rgb)
#         self.canvas.draw()
#         evt.Skip()
# 
# 
# class CanvasFrame(wx.Frame):
# 
#     def __init__(self):
#         wx.Frame.__init__(self,None,-1,
#                          'CanvasFrame',size=(550,350))
# 
#         self.SetBackgroundColour(wx.NamedColor("WHITE"))
# 
#         self.figure = Figure(figsize=(5,4), dpi=100)
#         self.axes = self.figure.add_subplot(111)
# 
#         # the NetworkX part
#         import networkx as nx
#         G=nx.path_graph(10)
#         pos=nx.spring_layout(G)
#         nx.draw_networkx(G,pos,ax=self.axes)
# 
#         self.canvas = FigureCanvas(self, -1, self.figure)
# 
#         self.sizer = wx.BoxSizer(wx.VERTICAL)
#         self.sizer.Add(self.canvas, 1, wx.TOP | wx.LEFT | wx.EXPAND)
#         # Capture the paint message
#         wx.EVT_PAINT(self, self.OnPaint)
# 
#         self.toolbar = MyNavigationToolbar(self.canvas, True)
#         self.toolbar.Realize()
#         if wx.Platform == '__WXMAC__':
#             # Mac platform (OSX 10.3, MacPython) does not seem to cope with
#             # having a toolbar in a sizer. This work-around gets the buttons
#             # back, but at the expense of having the toolbar at the top
#             self.SetToolBar(self.toolbar)
#         else:
#             # On Windows platform, default window size is incorrect, so set
#             # toolbar width to figure width.
#             tw, th = self.toolbar.GetSizeTuple()
#             fw, fh = self.canvas.GetSizeTuple()
#             # By adding toolbar in sizer, we are able to put it at the bottom
#             # of the frame - so appearance is closer to GTK version.
#             # As noted above, doesn't work for Mac.
#             self.toolbar.SetSize(wx.Size(fw, th))
#             self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
# 
#         # update the axes menu on the toolbar
#         self.toolbar.update()
#         self.SetSizer(self.sizer)
#         self.Fit()
# 
# 
#     def OnPaint(self, event):
#         self.canvas.draw()
#         event.Skip()
# 
# class App(wx.App):
# 
#     def OnInit(self):
#         'Create the main window and insert the custom frame'
#         frame = CanvasFrame()
#         frame.Show(True)
# 
#         return True
# 
# app = App(0)
# app.MainLoop()



# import threading
# 
# a = {1:"a"}
# c = 'xxx'
# 
# def unlock(b): 
#     b[1] = "b"
#    
#     
# t = threading.Timer(5, unlock, (a,)) #required processing time
# t.start()
#  
# def printa(b,c):
#     
#     print b,c
#     
# t1 = threading.Timer(7, printa, (a, c,)) #required processing time
# t1.start()

#printa(a)

# print 109/10000000000000000000000.0

# from __future__ import division

# a = 1
# b = 2
# print float(a)/b

# import datetime
# d = str(datetime.datetime.now())
# print d.replace(" ", "-")

# b = {2:(5,5,6), 1:(7,6,9)}
# a = b.items()
# a.append((3,(8,7,9)))
# a = sorted(a, key=lambda abc:abc[1], reverse=True)
# a = sorted(a, key=lambda abc:abc[1])
# print a
# print len(a)

# a = [(2,3),(4,5)]
# first = a[0]
# a = [(4,5)]
# print first
# print a[0]

# import os
# import pandas as pd
# print os.getcwd()
# archive1 = "stat_su_2015-08-21-12-39-48-647000_4096_FIFO_normal_LLNL-Thunder-2007-1-1-cln-swf-2"
# archive2 = "stat_su_2015-08-21-13-43-52-481000_4096_FIFO_FSO_LLNL-Thunder-2007-1-1-cln-swf-2"
# archive3 = "stat_su_2015-08-21-14-18-57-437000_4096_BF_normal_LLNL-Thunder-2007-1-1-cln-swf-2"
# archive4 = "stat_su_2015-08-21-13-14-09-412000_4096_BF_FSO_LLNL-Thunder-2007-1-1-cln-swf-2"
# archive5 = "stat_su_2015-08-21-22-13-38-544000_4096_SF_normal_LLNL-Thunder-2007-1-1-cln-swf-2"
# archive6 = "stat_su_2015-08-21-23-02-22-572000_4096_SF_FSO_LLNL-Thunder-2007-1-1-cln-swf-2"
# archive7 = "stat_su_2015-08-25-15-03-38-461000_4096_LIFO_normal_LLNL-Thunder-2007-1-1-cln-swf"
# archive8 = "stat_su_2015-08-25-13-38-44-070000_4096_LIFO_FSO_LLNL-Thunder-2007-1-1-cln-swf"
# archive9 = "stat_su_2015-08-28-11-58-59-850000_9216_FIFO_FSO_LLNL-Atlas-2006-2-1-cln-swf"
# archive10 = "stat_su_2015-08-28-11-17-16-492000_9216_FIFO_normal_LLNL-Atlas-2006-2-1-cln-swf"
# archive11 = "stat_su_2015-08-28-15-03-37-018000_1681_FIFO_normal_SDSC-DS-2004-2-1-cln-swf"
# archive12 = "stat_su_2015-08-28-16-26-00-804000_1681_FIFO_FSO_SDSC-DS-2004-2-1-cln-swf"
# archive13 = "stat_su_2015-08-28-18-48-47-964000_100_FIFO_normal_KTH-SP2-1996-2-1-cln-swf"
# archive14 = "stat_su_2015-08-28-20-37-14-120000_100_FIFO_FSO_KTH-SP2-1996-2-1-cln-swf"
# archive15 = "stat_su_2015-08-30-15-36-08-555000_400_FIFO_normal_SDSC-Par-1995-3-1-cln-swf"
# archive16 = "stat_su_2015-08-30-16-33-48-216000_400_FIFO_FSO_SDSC-Par-1995-3-1-cln-swf"
# archive17 = "stat_su_2015-09-23-17-21-17-127000_2-torus_4096_FIFO_normal_LLNL-Thunder-2007-1-1-cln-swf"
# archive18 = "stat_su_2015-09-23-22-26-14-998000_3-torus_4096_FIFO_normal_LLNL-Thunder-2007-1-1-cln-swf"
# archive19 = "stat_su_2015-09-23-23-08-12-786000_4-torus_4096_FIFO_normal_LLNL-Thunder-2007-1-1-cln-swf"
# archive20 = "stat_su_2015-09-23-23-47-15-978000_5-torus_4096_FIFO_normal_LLNL-Thunder-2007-1-1-cln-swf"
# archive21 = "stat_su_2015-09-24-00-27-15-258000_2-torus_4096_FIFO_FSO_LLNL-Thunder-2007-1-1-cln-swf"
# archive22 = "stat_su_2015-09-24-01-05-28-246000_3-torus_4096_FIFO_FSO_LLNL-Thunder-2007-1-1-cln-swf"
# archive23 = "stat_su_2015-09-24-07-34-35-309000_4-torus_4096_FIFO_FSO_LLNL-Thunder-2007-1-1-cln-swf"
# archive24 = "stat_su_2015-09-24-08-14-35-753000_5-torus_4096_FIFO_FSO_LLNL-Thunder-2007-1-1-cln-swf"
# archive25 = "stat_su_2015-10-08-20-02-46-069000_2-torus_2048_FIFO_normal_1.0_UniLu-Gaia-2014-2-swf"
# archive26 = "stat_su_2015-10-08-23-39-19-075000_2-torus_2048_FIFO_FSO_1.0_UniLu-Gaia-2014-2-swf"
# # 
# names = ["timestep", 
#         "occupied", 
#         "Timetotal", 
#         "utilization"]
# 
# 
# data1 = pd.read_csv(archive1, comment="#", sep="\s+", names=names) 
# data2 = pd.read_csv(archive2, comment="#", sep="\s+", names=names) 
# data3 = pd.read_csv(archive3, comment="#", sep="\s+", names=names) 
# data4 = pd.read_csv(archive4, comment="#", sep="\s+", names=names) 
# data5 = pd.read_csv(archive5, comment="#", sep="\s+", names=names) 
# data6 = pd.read_csv(archive6, comment="#", sep="\s+", names=names) 
# data7 = pd.read_csv(archive7, comment="#", sep="\s+", names=names) 
# data8 = pd.read_csv(archive8, comment="#", sep="\s+", names=names)
# data9 = pd.read_csv(archive9, comment="#", sep="\s+", names=names) 
# data10 = pd.read_csv(archive10, comment="#", sep="\s+", names=names)
# data11 = pd.read_csv(archive11, comment="#", sep="\s+", names=names) 
# data12 = pd.read_csv(archive12, comment="#", sep="\s+", names=names)
# data13 = pd.read_csv(archive13, comment="#", sep="\s+", names=names) 
# data14 = pd.read_csv(archive14, comment="#", sep="\s+", names=names)
# data15 = pd.read_csv(archive15, comment="#", sep="\s+", names=names) 
# data16 = pd.read_csv(archive16, comment="#", sep="\s+", names=names)
# data17 = pd.read_csv(archive17, comment="#", sep="\s+", names=names) 
# data18 = pd.read_csv(archive18, comment="#", sep="\s+", names=names)
# data19 = pd.read_csv(archive19, comment="#", sep="\s+", names=names) 
# data20 = pd.read_csv(archive20, comment="#", sep="\s+", names=names)
# data21 = pd.read_csv(archive21, comment="#", sep="\s+", names=names) 
# data22 = pd.read_csv(archive22, comment="#", sep="\s+", names=names)
# data23 = pd.read_csv(archive23, comment="#", sep="\s+", names=names) 
# data24 = pd.read_csv(archive24, comment="#", sep="\s+", names=names)
# data25 = pd.read_csv(archive25, comment="#", sep="\s+", names=names) 
# data26 = pd.read_csv(archive26, comment="#", sep="\s+", names=names)
# 
# print sum(data1["utilization"])/len(data1)
# print sum(data2["utilization"])/len(data2)
# print sum(data3["utilization"])/len(data3)
# print sum(data4["utilization"])/len(data4)
# print sum(data5["utilization"])/len(data5)
# print sum(data6["utilization"])/len(data6)
# print sum(data7["utilization"])/len(data7)
# print sum(data8["utilization"])/len(data8)
# print sum(data9["utilization"])/len(data9)
# print sum(data10["utilization"])/len(data10)
# print sum(data11["utilization"])/len(data11)
# print sum(data12["utilization"])/len(data12)
# print sum(data13["utilization"])/len(data13)
# print sum(data14["utilization"])/len(data14)
# print sum(data15["utilization"])/len(data15)
# print sum(data16["utilization"])/len(data16)
# print sum(data17["utilization"])/len(data17)
# print sum(data18["utilization"])/len(data18)
# print sum(data19["utilization"])/len(data19)
# print sum(data20["utilization"])/len(data20)
# print sum(data21["utilization"])/len(data21)
# print sum(data22["utilization"])/len(data22)
# print sum(data23["utilization"])/len(data23)
# print sum(data24["utilization"])/len(data24)
# print sum(data25["utilization"])/len(data25)
# print sum(data26["utilization"])/len(data26)

# li = [3,4,5,2,8]
# one = li.pop(0)
# li = sorted(li)
# li.insert(0, one)
# print li
# print li


# import networkx as nx
# import matplotlib.pyplot as plt
# 
# RG = nx.grid_graph(dim=[3,3], periodic=True)
# # pos = dict(zip(RG,RG))
# print RG.nodes()
# 
# nx.draw(RG)  
# plt.show() 

# torus_d = 3
#  
# def divi_torus(n):  
#     di = []
#     while(n!=1):
#         for i in range(2,n+1):
#             if (n%i)==0:
#                 n/=i
#                 di.append(i)
#                 break
#     dim = len(di)
#     dis = dim-torus_d
#     dis_abs = abs(dis)
#     if(dis<0):
#         for i in range(dis_abs):
#             di.append(1)
#     if(dis>0):   
#         for i in range(dis_abs):
#             di[i%torus_d] = di[i%torus_d]*di.pop(-1)      
#     return di
# 
# print divi_torus(1)
# print divi_torus(2)
# print divi_torus(3)
# print divi_torus(4)

# 
# print divi_torus(8)
# print divi_torus(24)
# d = divi_torus(24)
# d.insert(0, d.pop(-1))
# print d
# print divi_torus(33)
# print divi_torus(37)
# 
# a = [2,4,5]
# 
# print a[2]

# a = [5,6,4]
# c = a
# a = [12,2]
# 
# print c

# import networkx as nx
# 
# RG = nx.grid_graph(dim=[3,4,5,6,7], periodic=True)
# print RG.degree((1,1,1,1,3))

# import networkx as nx
#    
# RG = nx.grid_graph(dim=[2,3], periodic=True)
 
# H = RG.subgraph([(1,2),(1,3),(2,3),(4,4)])
# print H
# print H.edges()
# print list(H.edges())
# print RG.edges()
# print len(RG.edges())
# X = RG.copy()
# X.remove_nodes_from([(1,1),(2,2)]) 
# print RG.edges()
# print len(RG.edges())
# print X.edges()
# print len(X.edges())
 
# print list(nx.connected_component_subgraphs(H))
# x = list(nx.connected_components(H))
# print x
# # for i in x:
# #     for j in i:
# #         print j
# #         i.remove(j)
# #         print i
# for i in x:
#     print i.pop()      
#     print x
#     print len(i)
        
        
# print RG.edges()
# print len(RG.edges())
# 
# print 20/100.0
# print int("20")/100.0

# 
# fso_links = [((0, 1), (0, 0)), ((0, 1), (1, 1)), ((0, 1), (2, 1)), ((0, 1), (0, 2))]
# for link in fso_links:
#     print link[0]
#     print link[1]

# print RG.neighbors((1,2))

# def a():
#     print "a"
#     
# def b():
#     a()
#     print "b"
# 
# b()

# a = [(1,2), (4,5), (6,7)]
# b = (4,5)
# c = (5,6)
# print b in a
# print c in a
# 
# a.append((7,8))
# a.append((7,8))
# print a

# a = [((1,2),4), ((3,4),5),((3,4),5)]
# print a[0][1]
# print a[1][1]
# print list(set(a))
# print a.count(((3,4),5))
# a.remove(((3,4),5))
# print a

# a = 80
# b = 60
# print float(a)/b>1
# 
# c = 7.8
# print int(c)

# a = [3,4,5]
# for i in a:
#     if(i==a[-1]):
#         print i

# import time
# print time.time()
# print int(time.time())
# 
# f = open("hh", "w")    #system utilization 
# f.write("#job_number  submit  dispatch  queue\n")   
# for i in range(2):
#     s = "  xx  " + "  yy  " + "\n"
#     f.write(s)
# f.close()

# a = [6,7,8]
# b = [4,5]
# a = b
# print a

# a = 4094
# b = a*0.01
# print int(b)

# list = [3,5.8,7]
# print sum(list)
# 
# x = 1
# 
# print "x", str(x), "y"

# x = [(0,(2,4,5)), (4,(4,5,6)), (8,(3,3,7))]
# # x = sorted(x, key=lambda abc:abc[1][1], reverse=True)
# print len(x)
# for i in range(len(x)):
#     if x[i][1][0] == 3:
#         x.insert(0, x.pop(i))
#         break
# print x

# first_time = 3.8
# tn = 16
# first_cpu = 1
# tb = (2*tn-1+first_cpu)/(2*float(first_cpu)) #t before
# first_cpu = 4
# ta = (2*tn-1+first_cpu)/(2*float(first_cpu))
# first_time = int((ta/tb)*first_time)
# print tb
# print ta
# print first_time

# tn = 1024
# specified_cpu = 32
# specified_time = 2
# nodes_in_cabinet = 64
# 
# tb = (2*tn-1+specified_cpu)/(2*float(specified_cpu)) #time before
# first_cpu = (specified_cpu+nodes_in_cabinet-1)/nodes_in_cabinet
# nodes = first_cpu*nodes_in_cabinet
# ta = (2*tn-1+nodes)/(2*float(nodes))
# first_time = (ta/tb)*specified_time
# 
# print tb 
# print ta
# print first_cpu
# print first_time

# 1296 racks = 432*3 = 18*24*3 = 54*24
# cpu_in_one_unit = 4
# ssd_in_one_unit = 16
# gpu_in_one_unit = 64
# racks = 1296
# #rackscale
# rs_cpu_unit_in_one_rack = 1
# rs_ssd_unit_in_one_rack = 1
# rs_gpu_unit_in_one_rack = 1
# rs_cpu_in_one_rack = rs_cpu_unit_in_one_rack*cpu_in_one_unit # 4
# rs_ssd_in_one_rack = rs_ssd_unit_in_one_rack*ssd_in_one_unit # 16
# rs_gpu_in_one_rack = rs_gpu_unit_in_one_rack*gpu_in_one_unit # 64
# rs_cpu_racks = rs_cpu_in_one_rack*racks # 4*1296=5184
# rs_ssd_racks = rs_ssd_in_one_rack*racks # 16*1296=20736
# rs_gpu_racks = rs_gpu_in_one_rack*racks # 64*1296=82944
# #interrackscale
# irs_cpu_unit_in_one_rack = 3
# irs_ssd_unit_in_one_rack = 3
# irs_gpu_unit_in_one_rack = 3
# irs_cpu_in_one_rack = irs_cpu_unit_in_one_rack*cpu_in_one_unit # 12
# irs_ssd_in_one_rack = irs_ssd_unit_in_one_rack*ssd_in_one_unit # 48
# irs_gpu_in_one_rack = irs_gpu_unit_in_one_rack*gpu_in_one_unit # 192
# irs_cpu_racks = irs_cpu_in_one_rack*racks/3 # 12*1296/3=5184
# irs_ssd_racks = irs_ssd_in_one_rack*racks/3 # 48*1296/3=20736
# irs_gpu_racks = irs_gpu_in_one_rack*racks/3 # 192*1296/3=82944
# 
# print rs_gpu_racks, irs_cpu_racks


# for a in range(5,8):
#     print a
    
# import networkx as nx
# 
# RG = nx.grid_graph(dim=[2,2], periodic=True)    
# for node in RG.nodes():
#     print node[0]

# x = "sdfsjao"
# print x.startswith("sdf")
# print x.startswith("dsf")

# import networkx as nx
# from networkx.algorithms.distance_measures import diameter
# from networkx.algorithms.components.connected import is_connected
# RG = nx.grid_graph(dim=[4,4], periodic=True)
# print is_connected(RG)
# print RG.number_of_edges()
# subs = RG.subgraph([(0,0), (0,1), (0,2), (2,0), (2,1), (2,2)])
# print is_connected(subs)
# print subs.number_of_edges()
# #subs.add_weighted_edges_from([((0,0),(2,0),2),((0,1),(2,1),2),((0,2),(2,2),2)])
# subs.add_edge((0,0),(2,0),weight=2)
# print is_connected(subs)
# print diameter(subs)
# print nx.johnson(subs)

# import networkx as nx
# RG = nx.graph()

# 
# print 5*3+4*2
# 
# n= 6
# di = []
# torus_d = 3
# while(n!=1):
#     for i in range(2,n+1):
#         if (n%i)==0:
#             n/=i
#             di.append(i)
#             break
# dim = len(di)
# dis = dim-torus_d
# dis_abs = abs(dis)
# if(dis<0):
#     for i in range(dis_abs):
#         di.append(1)
# if(dis>0):   
#     for i in range(dis_abs):
#         i_mod=i%torus_d
#         di[i_mod] = di[i_mod]*di.pop(-1) 
# print di

# a = {}
# a[1] = 2
# a[2] = 3
# print a.has_key(2)
# print a.has_key(3)

# import copy
# a = [(1,2), (3,4)]
# b = copy.copy(a)
# a.pop(0)
# print a
# print b

# import random
# a=[]
# for i in range(2000):
#     a.append(random.expovariate(20.0))
# print sum(a)

# avg_ssd_gpu_three = (5.6131+10.8374)/2
# avg_ssd_gpu_twenty = (24.2011+27.0112)/2
# avg_ssd_gpu_six = (8.8011+13.6172)/2
# print avg_ssd_gpu_three, avg_ssd_gpu_twenty, avg_ssd_gpu_six
# print avg_ssd_gpu_three/25, avg_ssd_gpu_twenty/25, avg_ssd_gpu_six/25
# print (avg_ssd_gpu_three/25)/(avg_ssd_gpu_twenty/25), (avg_ssd_gpu_three/25)/(avg_ssd_gpu_six/25)
# fso = [0.4842, 0.4340, 0.4109, 0.4007, 0.3963, 
#        0.8170, 0.7713, 0.7550, 0.7392, 0.7317,
#        0.9436, 0.9337, 0.9249, 0.9225, 0.9218,
#        0.9891, 0.9890, 0.9889, 0.9875, 0.9881]
# for i in range(len(fso)):
#     avg_latency_between_fso_and_ssdgpu = fso[i]*avg_ssd_gpu_three + (1-fso[i])*avg_ssd_gpu_twenty
#     print (avg_latency_between_fso_and_ssdgpu/25)/(avg_ssd_gpu_twenty/25)
# fso = [0.3567, 0.3436, 0.3419, 0.3410, 0.3369, 
#        0.6659, 0.6517, 0.6496, 0.6519, 0.6451,
#        0.8805, 0.8815, 0.8734, 0.8762, 0.8786,
#        0.9716, 0.9757, 0.9735, 0.9762, 0.9745]
# for i in range(len(fso)):
#     avg_latency_between_fso_and_ssdgpu = fso[i]*avg_ssd_gpu_three + (1-fso[i])*avg_ssd_gpu_six
#     print (avg_latency_between_fso_and_ssdgpu/25)

# runtime = "2mesh:0.1010:0.1011:0.1013:0.1014:2torus:0.1010:0.1011:0.1013:0.1014:random:0.0832:0.0834:0.0836:0.0838"
# print runtime.split("2mesh")[1].split(":")
# print runtime.split("2torus")[1].split(":")
# print runtime.split("random")[1].split(":")
# 
# print runtime.split("2mesh")[1].split(":")[4]
# print runtime.split("2torus")[1].split(":")[4]
# print runtime.split("random")[1].split(":")[4]
# 
# # s = runtime.split("2mesh")[1].split(":")[4] + 1
# t = (float)(runtime.split("2mesh")[1].split(":")[4]) + 1
# print t
# # print s
# 
# import random
# cpu_unit = random.sample([4, 16, 64, 256], 1)[0]
# print cpu_unit
# 
# for i in range(2, 10, 2):
#     print i
#     
# a = "45"
# a = int(a)
# print a+1
# 
# a = [1,2,3,4,5]
# b = [2,3]
# for each in a:
#     if each not in b:
#         print each

# a = []
# a.append(1)
# a.append(2)
# a.append(3)
# a.append(4)
# print a
# a.pop()
# print a

# b = {}
# b[0] = []
# print b
# b[0].append(1)
# b[0].append(2)
# b[0].append(3)
# print b
# b[0].remove(2)
# print b
# b[0].append(2)
# print b

# for i in range(0):
#     print i

# a = 100
# b = 200
# res = []
# with open("/Users/smallcat/Documents/GitHub/python-test/HPL.dat", "r") as f:
#     res = f.readlines()
# res[5]=str(a) + "\t\t\t Ns\n"
# res[26]=str(b) + "\t\t\t swapping threshold\n"
# with open("/Users/smallcat/Documents/GitHub/python-test/HPL.dat", "w") as f:    
#     f.write("".join(res))  

#(nx, ny, nz, ppn, OMP_NUM_TRREADS), ppn = {1, 2, 4, 5}, ppn * OMP_NUM_THREADS = 20
# zero = (192, 192, 192, 1, 20)
# step = 32
# ppn = [1, 2, 4, 5]
# comb = []
# for p in ppn:
#     for nx in range(192, 1152, step):
#         for ny in range(192, 1152, step):
#             for nz in range(192, 1152, step):
#                 if (nx * ny * nz * p)//(192 * 192 * 192 * 1) <= 5:
#                     comb.append((nx, ny, nz, p, 20//p))
# print(comb)
a = '(1, 2, 3, 4, 5)'
print(eval(a)[0])

from readlif.reader import LifFile
import numpy as np
import napari

path = "test-files/lif1.lif"
raw_data = LifFile(path)
raw_image = raw_data.get_image(1)
z_nr_list = list(range(0,len([i for i in raw_image.get_iter_z()])))
c_nr_list = list(range(0,len([i for i in raw_image.get_iter_c()])))
m_nr_list = list(range(0,len([i for i in raw_image.get_iter_m()])))

layers_c0 = np.zeros(((1024,1024)))
layers_c1 = np.zeros(((1024,1024)))
for z_nr in z_nr_list:
    layers_c0 = np.dstack((layers_c0, np.asarray(raw_image.get_frame(z = z_nr, t = 0, c = 0, m = 0))))
    layers_c1 = np.dstack((layers_c1, np.asarray(raw_image.get_frame(z = z_nr, t = 0, c = 1, m = 0))))
    
with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(layers_c0, scale = (1,1,14),colormap='blue')
    viewer.add_image(layers_c1, scale = (1,1,14),colormap='yellow')

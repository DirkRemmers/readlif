import sys
sys.path.insert(1, '.')

from readlif.reader import LifFile
import numpy as np
import napari

path = "./tests/navi_mosaic.lif"
raw_data = LifFile(path)
img_list = [i for i in raw_data.get_iter_image()]
print(len(img_list))
raw_image = raw_data.get_image(0)
print(raw_image.name)
z_nr_list = list(range(0,len([i for i in raw_image.get_iter_z()])))
c_nr_list = list(range(0,len([i for i in raw_image.get_iter_c()])))
m_nr_list = list(range(0,len([i for i in raw_image.get_iter_m()])))

m_nr = 7

for z_nr in z_nr_list:
    if z_nr == 0:
        layers_c0 = np.asarray(raw_image.get_frame(z = z_nr, t = 0, c = 0, m = m_nr))
        layers_c1= np.asarray(raw_image.get_frame(z = z_nr, t = 0, c = 1, m = m_nr))
    else:
        layers_c0 = np.dstack((layers_c0, np.asarray(raw_image.get_frame(z = z_nr, t = 0, c = 0, m = m_nr))))
        layers_c1 = np.dstack((layers_c1, np.asarray(raw_image.get_frame(z = z_nr, t = 0, c = 1, m = m_nr))))
    
with napari.gui_qt():
    viewer = napari.Viewer()
    viewer.add_image(layers_c0, scale = (1,1,14),colormap='blue', blending='additive')
    viewer.add_image(layers_c1, scale = (1,1,14),colormap='yellow', blending='additive')
    viewer.dims.ndisplay = 3

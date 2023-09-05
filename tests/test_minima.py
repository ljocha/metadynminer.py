import pytest
import metadynminer as mm
from matplotlib import pyplot as plt
import os
import numpy as np

def test_1p():
    expected = np.array([[0.,74.,-1.313132],
       [1.631527,28.,-2.442096],
       [6.164974,167.,0.96934 ]])
    #load hills
    h1 = mm.Hills(name="./data/acealanme1d", periodic=[True])
    #find minima on FES
    minima = mm.Minima(mm.Fes(h1, resolution=256, original=False))
    minima = minima.minima.to_numpy()
    minima = minima[:,1:].astype(float)
    assert(np.allclose(minima, expected, 1e-4))
    
def test_1np():
    expected = np.array([[  0.      ,  86.      ,  -1.324176],
       [  2.260562,  55.      ,  -2.313247],
       [  6.126335, 158.      ,   0.973021],
       [ 47.687144, 211.      ,   2.664014]])
    #load hills
    h1 = mm.Hills(name="./data/acealanme1d", periodic=[False])
    #find minima on FES
    minima = mm.Minima(mm.Fes(h1, resolution=256, original=False))
    minima = minima.minima.to_numpy()
    minima = minima[:,1:].astype(float)
    assert(np.allclose(minima, expected, 1e-4))
    
def test_2p():
    expected = np.array([[  0.      ,  77.      , 235.      ,  -1.239259,   2.638265],
       [  1.63016 ,  27.      , 239.      ,  -2.466388,   2.736432],
       [  2.526665,  73.      , 117.      ,  -1.33743 ,  -0.257663],
       [  5.591042, 165.      , 150.      ,   0.920487,   0.552215],
       [ 12.878739, 169.      , 250.      ,   1.018657,   3.006392]])
    #load hills
    h2 = mm.Hills(name="./data/acealanme", periodic=[True, True])
    #find minima on FES
    minima = mm.Minima(mm.Fes(h2, resolution=256, original=False))
    minima = minima.minima.to_numpy()
    minima = minima[:,1:].astype(float)
    assert(np.allclose(minima, expected, 1e-4))

def test_2np():
    expected = np.array([[ 0.0000000e+00,  9.0000000e+01,  2.0400000e+02, -1.1963100e+00,
         2.4407040e+00],
       [ 9.9968800e-01,  8.6000000e+01,  1.1900000e+02, -1.3239310e+00,
        -2.7116100e-01],
       [ 3.3958110e+00,  5.5000000e+01,  2.0500000e+02, -2.3129970e+00,
         2.4726080e+00],
       [ 3.5844430e+00,  5.7000000e+01,  1.2800000e+02, -2.2491860e+00,
         1.5978000e-02],
       [ 3.6883250e+00,  1.5700000e+02,  1.4500000e+02,  9.4134800e-01,
         5.5835100e-01],
       [ 1.5216482e+01,  1.6200000e+02,  2.0500000e+02,  1.1008750e+00,
         2.4726080e+00],
       [ 1.5705841e+01,  1.5400000e+02,  5.3000000e+01,  8.4563200e-01,
        -2.3768450e+00],
       [ 1.6567691e+01,  5.4000000e+01,  4.8000000e+01, -2.3449020e+00,
        -2.5363660e+00],
       [ 1.7062693e+01,  7.9000000e+01,  4.8000000e+01, -1.5472690e+00,
        -2.5363660e+00],
       [ 4.3937982e+01,  2.1500000e+02,  2.0700000e+02,  2.7918580e+00,
         2.5364170e+00],
       [ 4.8816293e+01,  2.1400000e+02,  1.0800000e+02,  2.7599530e+00,
        -6.2210800e-01],
       [ 6.0844758e+01,  2.1600000e+02,  4.3000000e+01,  2.8237640e+00,
        -2.6958880e+00]])
    #load hills
    h2 = mm.Hills(name="./data/acealanme", periodic=[False,False])
    #find minima on FES
    minima = mm.Minima(mm.Fes(h2, resolution=256, original=False))
    minima = minima.minima.to_numpy()
    minima = minima[:,1:].astype(float)
    assert(np.allclose(minima, expected, 1e-4))
    
def test_3p():
    expected = np.array([[ 0.0000000e+00,  1.8000000e+01,  5.8000000e+01,  6.3000000e+01,
        -1.3253400e+00,  2.6014860e+00,  3.0924910e+00],
       [ 6.8306100e-01,  6.0000000e+00,  5.9000000e+01,  6.3000000e+01,
        -2.5034270e+00,  2.6996520e+00,  3.0924910e+00],
       [ 6.8766400e-01,  6.0000000e+00,  5.9000000e+01,  0.0000000e+00,
        -2.5034270e+00,  2.6996520e+00, -3.0924740e+00],
       [ 2.2454140e+00,  1.8000000e+01,  2.9000000e+01,  0.0000000e+00,
        -1.3253400e+00, -2.4534000e-01, -3.0924740e+00],
       [ 5.3823810e+00,  4.1000000e+01,  3.6000000e+01,  0.0000000e+00,
         9.3266100e-01,  4.4182500e-01, -3.0924740e+00],
       [ 1.2013302e+01,  4.2000000e+01,  6.3000000e+01,  0.0000000e+00,
         1.0308350e+00,  3.0923180e+00, -3.0924740e+00],
       [ 1.5878538e+01,  4.0000000e+00,  5.9000000e+01,  3.2000000e+01,
        -2.6997750e+00,  2.6996520e+00,  4.9096000e-02],
       [ 1.5924749e+01,  4.0000000e+00,  5.9000000e+01,  3.1000000e+01,
        -2.6997750e+00,  2.6996520e+00, -4.9078000e-02],
       [ 1.6156179e+01,  2.0000000e+01,  5.9000000e+01,  3.1000000e+01,
        -1.1289920e+00,  2.6996520e+00, -4.9078000e-02],
       [ 2.4853236e+01,  4.0000000e+01,  4.2000000e+01,  3.2000000e+01,
         8.3448700e-01,  1.0308240e+00,  4.9096000e-02],
       [ 2.5129005e+01,  6.0000000e+00,  4.4000000e+01,  3.2000000e+01,
        -2.5034270e+00,  1.2271560e+00,  4.9096000e-02],
       [ 2.6808114e+01,  1.9000000e+01,  2.5000000e+01,  3.0000000e+01,
        -1.2271660e+00, -6.3800500e-01, -1.4725200e-01],
       [ 2.7421158e+01,  4.3000000e+01,  5.9000000e+01,  3.1000000e+01,
         1.1290080e+00,  2.6996520e+00, -4.9078000e-02],
       [ 3.7466200e+01,  5.0000000e+00,  2.4000000e+01,  3.0000000e+01,
        -2.6016010e+00, -7.3617200e-01, -1.4725200e-01],
       [ 5.4239626e+01,  4.1000000e+01,  1.1000000e+01,  3.2000000e+01,
         9.3266100e-01, -2.0123350e+00,  4.9096000e-02]])
    #load hills
    h3 = mm.Hills(name="./data/acealanme3d", periodic=[True,True,True])
    #find minima on FES
    minima = mm.Minima(mm.Fes(h3, resolution=64, original=False))
    minima = minima.minima.to_numpy()
    minima = minima[:,1:].astype(float)
    assert(np.allclose(minima, expected, 1e-4))

def test_3np():
    expected = np.array([[ 0.      , 23.      , 51.      , 52.      , -1.084814,  2.488595,         2.616347],
       [ 0.422574, 22.      , 50.      , 11.      , -1.21244 ,  2.360978,        -2.61633 ],
       [ 1.47564 , 21.      , 29.      , 52.      , -1.340066, -0.318964,         2.616347],
       [ 1.545001, 22.      , 28.      , 10.      , -1.21244 , -0.446581,        -2.743956],
       [ 2.138148, 13.      , 51.      , 10.      , -2.361075,  2.488595,        -2.743956],
       [ 3.023587, 39.      , 36.      , 11.      ,  0.957204,  0.57435 ,        -2.61633 ],
       [ 3.097259, 12.      , 51.      , 53.      , -2.488701,  2.488595,         2.743974],
       [ 4.649499, 39.      , 35.      , 53.      ,  0.957204,  0.446734,         2.743974],
       [ 4.854876, 23.      , 51.      , 32.      , -1.084814,  2.488595,         0.063822],
       [ 4.901328, 12.      , 52.      , 32.      , -2.488701,  2.616211,         0.063822],
       [ 9.052563, 38.      , 40.      , 32.      ,  0.829578,  1.084815,         0.063822],
       [10.788269, 13.      , 42.      , 32.      , -2.361075,  1.340048,         0.063822],
       [12.311325, 22.      , 27.      , 30.      , -1.21244 , -0.574197,        -0.191431],
       [12.829716, 40.      , 51.      , 53.      ,  1.08483 ,  2.488595,         2.743974],
       [13.57842 , 13.      , 11.      , 53.      , -2.361075, -2.616058,         2.743974],
       [13.636475, 18.      , 12.      , 10.      , -1.722944, -2.488442,        -2.743956],
       [14.20011 , 38.      , 13.      , 10.      ,  0.829578, -2.360825,        -2.743956],
       [14.583503, 20.      , 11.      , 53.      , -1.467692, -2.616058,         2.743974],
       [14.664506, 39.      , 12.      , 53.      ,  0.957204, -2.488442,         2.743974],
       [14.688313, 40.      , 51.      , 10.      ,  1.08483 ,  2.488595,        -2.743956],
       [15.622219, 40.      , 52.      , 32.      ,  1.08483 ,  2.616211,         0.063822],
       [15.938178, 40.      , 52.      , 31.      ,  1.08483 ,  2.616211,        -0.063805],
       [23.088539, 12.      , 25.      , 31.      , -2.488701, -0.82943 ,        -0.063805],
       [33.959612, 12.      ,  9.      , 29.      , -2.488701, -2.871291,        -0.319057],
       [34.657294, 20.      ,  9.      , 29.      , -1.467692, -2.871291,        -0.319057],
       [36.118429, 54.      , 51.      ,  9.      ,  2.871596,  2.488595,        -2.871583],
       [36.199325, 39.      , 10.      , 30.      ,  0.957204, -2.743674,        -0.191431],
       [37.618172, 54.      , 52.      , 53.      ,  2.871596,  2.616211,         2.743974],
       [39.779488, 38.      , 16.      , 32.      ,  0.829578, -1.977976,         0.063822],
       [41.706793, 54.      , 28.      , 54.      ,  2.871596, -0.446581,         2.8716  ],
       [42.790045, 54.      , 26.      ,  9.      ,  2.871596, -0.701813,        -2.871583],
       [43.479828, 54.      , 52.      , 31.      ,  2.871596,  2.616211,        -0.063805],
       [49.584441, 54.      , 10.      ,  9.      ,  2.871596, -2.743674,        -2.871583],
       [51.788568, 55.      , 10.      , 54.      ,  2.999222, -2.743674,         2.8716  ],
       [55.592533, 55.      , 25.      , 32.      ,  2.999222, -0.82943 ,         0.063822],
       [55.745591, 55.      , 25.      , 31.      ,  2.999222, -0.82943 ,        -0.063805],
       [61.714603, 55.      ,  7.      , 29.      ,  2.999222, -3.126523,        -0.319057],
       [61.827058, 56.      ,  7.      , 25.      ,  3.126848, -3.126523,        -0.829562]])
    #load hills
    h3 = mm.Hills(name="./data/acealanme3d", periodic=[False,False,False])
    #find minima on FES
    minima = mm.Minima(mm.Fes(h3, resolution=64, original=False))
    minima = minima.minima.to_numpy()
    minima = minima[:,1:].astype(float)
    assert(np.allclose(minima, expected, 1e-4))

if __name__ == '__main__':
    pytest.main([__file__])

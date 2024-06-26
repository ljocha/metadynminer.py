import pytest
import metadynminer as mm
from matplotlib import pyplot as plt
import os
import numpy as np

def test_1p():
    expected = np.array([[0.,74.,-1.325359],
       [1.631527,28.,-2.454369],
       [6.164974,167.,0.957204]])
    #load hills
    h1 = mm.Hills(name="./data/acealanme1d", periodic=[True])
    #find minima on FES
    minima = mm.Minima(mm.Fes(h1, resolution=256, original=False))
    minima = minima.minima.to_numpy()
    minima = minima[:,1:].astype(float)
    assert(np.allclose(minima, expected, 1e-3))
    
def test_1np():
    expected = np.array([[  0.      ,  86.      ,  -1.340129],
       [  2.260562,  55.      ,  -2.3292  ],
       [  6.126335, 158.      ,   0.957069],
       [ 47.687144, 211.      ,   2.648061]])
    #load hills
    h1 = mm.Hills(name="./data/acealanme1d", periodic=[False])
    #find minima on FES
    minima = mm.Minima(mm.Fes(h1, resolution=256, original=False))
    minima = minima.minima.to_numpy()
    minima = minima[:,1:].astype(float)
    assert(np.allclose(minima, expected, 1e-4))

def test_2p():
    expected = np.array([[  0.      ,  77.      , 235.      ,  -1.251728,   2.626175],
       [  1.63016 ,  27.      , 239.      ,  -2.478913,   2.72435 ],
       [  2.526665,  73.      , 117.      ,  -1.349903,  -0.269981],
       [  5.591042, 165.      , 150.      ,   0.908117,   0.539961],
       [ 12.878739, 169.      , 250.      ,   1.006291,   2.99433 ]])
    #load hills
    h2 = mm.Hills(name="./data/acealanme", periodic=[True, True])
    #find minima on FES
    minima = mm.Minima(mm.Fes(h2, resolution=256, original=False))
    minima = minima.minima.to_numpy()
    minima = minima[:,1:].astype(float)
    assert(np.allclose(minima, expected, 1e-4))

def test_2np():
    expected = np.array([[ 0.0000000e+00,  9.0000000e+01,  2.0400000e+02, -1.2122630e+00,
         2.4247520e+00],
       [ 9.9968800e-01,  8.6000000e+01,  1.1900000e+02, -1.3398840e+00,
        -2.8711300e-01],
       [ 3.3958110e+00,  5.5000000e+01,  2.0500000e+02, -2.3289500e+00,
         2.4566560e+00],
       [ 3.5844430e+00,  5.7000000e+01,  1.2800000e+02, -2.2651390e+00,
         2.5000000e-05],
       [ 3.6883250e+00,  1.5700000e+02,  1.4500000e+02,  9.2539500e-01,
         5.4239800e-01],
       [ 1.5216482e+01,  1.6200000e+02,  2.0500000e+02,  1.0849220e+00,
         2.4566560e+00],
       [ 1.5705841e+01,  1.5400000e+02,  5.3000000e+01,  8.2967900e-01,
        -2.3927970e+00],
       [ 1.6567691e+01,  5.4000000e+01,  4.8000000e+01, -2.3608550e+00,
        -2.5523180e+00],
       [ 1.7062693e+01,  7.9000000e+01,  4.8000000e+01, -1.5632210e+00,
        -2.5523180e+00],
       [ 4.3937982e+01,  2.1500000e+02,  2.0700000e+02,  2.7759060e+00,
         2.5204650e+00],
       [ 4.8816293e+01,  2.1400000e+02,  1.0800000e+02,  2.7440000e+00,
        -6.3806100e-01],
       [ 6.0844758e+01,  2.1600000e+02,  4.3000000e+01,  2.8078110e+00,
        -2.7118400e+00]])
    #load hills
    h2 = mm.Hills(name="./data/acealanme", periodic=[False,False])
    #find minima on FES
    minima = mm.Minima(mm.Fes(h2, resolution=256, original=False))
    minima = minima.minima.to_numpy()
    minima = minima[:,1:].astype(float)
    assert(np.allclose(minima, expected, 1e-4))
    
def test_3p():
    expected = np.array([[ 0.      , 18.      , 58.      , 63.      , -1.374447,  2.552544,
         3.043418],
       [ 0.683061,  6.      , 59.      , 63.      , -2.552544,  2.650719,
         3.043418],
       [ 0.687664,  6.      , 59.      ,  0.      , -2.552544,  2.650719,
        -3.141593],
       [ 2.245414, 18.      , 29.      ,  0.      , -1.374447, -0.294524,
        -3.141593],
       [ 5.382381, 41.      , 36.      ,  0.      ,  0.883573,  0.392699,
        -3.141593],
       [12.013302, 42.      , 63.      ,  0.      ,  0.981748,  3.043418,
        -3.141593],
       [15.878538,  4.      , 59.      , 32.      , -2.748894,  2.650719,
         0.      ],
       [15.924749,  4.      , 59.      , 31.      , -2.748894,  2.650719,
        -0.098175],
       [16.156179, 20.      , 59.      , 31.      , -1.178097,  2.650719,
        -0.098175],
       [24.853236, 40.      , 42.      , 32.      ,  0.785398,  0.981748,
         0.      ],
       [25.129005,  6.      , 44.      , 32.      , -2.552544,  1.178097,
         0.      ],
       [26.808114, 19.      , 25.      , 30.      , -1.276272, -0.687223,
        -0.19635 ],
       [27.421158, 43.      , 59.      , 31.      ,  1.079922,  2.650719,
        -0.098175],
       [37.4662  ,  5.      , 24.      , 30.      , -2.650719, -0.785398,
        -0.19635 ],
       [54.239626, 41.      , 11.      , 32.      ,  0.883573, -2.06167 ,
         0.      ]])
    #load hills
    h3 = mm.Hills(name="./data/acealanme3d", periodic=[True,True,True])
    #find minima on FES
    minima = mm.Minima(mm.Fes(h3, resolution=64, original=False))
    minima = minima.minima.to_numpy()
    minima = minima[:,1:].astype(float)
    assert(np.allclose(minima, expected, 1e-4))

def test_3np():
    expected = np.array([[ 0.0000000e+00,  2.3000000e+01,  5.1000000e+01,  5.2000000e+01,
        -1.1486270e+00,  2.4247860e+00,  2.5525340e+00],
       [ 4.2257400e-01,  2.2000000e+01,  5.0000000e+01,  1.1000000e+01,
        -1.2762530e+00,  2.2971700e+00, -2.6801430e+00],
       [ 1.4756400e+00,  2.1000000e+01,  2.9000000e+01,  5.2000000e+01,
        -1.4038790e+00, -3.8277200e-01,  2.5525340e+00],
       [ 1.5450010e+00,  2.2000000e+01,  2.8000000e+01,  1.0000000e+01,
        -1.2762530e+00, -5.1038900e-01, -2.8077690e+00],
       [ 2.1381480e+00,  1.3000000e+01,  5.1000000e+01,  1.0000000e+01,
        -2.4248880e+00,  2.4247860e+00, -2.8077690e+00],
       [ 3.0235870e+00,  3.9000000e+01,  3.6000000e+01,  1.1000000e+01,
         8.9339100e-01,  5.1054200e-01, -2.6801430e+00],
       [ 3.0972590e+00,  1.2000000e+01,  5.1000000e+01,  5.3000000e+01,
        -2.5525140e+00,  2.4247860e+00,  2.6801600e+00],
       [ 4.6494990e+00,  3.9000000e+01,  3.5000000e+01,  5.3000000e+01,
         8.9339100e-01,  3.8292500e-01,  2.6801600e+00],
       [ 4.8548760e+00,  2.3000000e+01,  5.1000000e+01,  3.2000000e+01,
        -1.1486270e+00,  2.4247860e+00,  9.0000000e-06],
       [ 4.9013280e+00,  1.2000000e+01,  5.2000000e+01,  3.2000000e+01,
        -2.5525140e+00,  2.5524030e+00,  9.0000000e-06],
       [ 9.0525630e+00,  3.8000000e+01,  4.0000000e+01,  3.2000000e+01,
         7.6576500e-01,  1.0210070e+00,  9.0000000e-06],
       [ 1.0788269e+01,  1.3000000e+01,  4.2000000e+01,  3.2000000e+01,
        -2.4248880e+00,  1.2762400e+00,  9.0000000e-06],
       [ 1.2311325e+01,  2.2000000e+01,  2.7000000e+01,  3.0000000e+01,
        -1.2762530e+00, -6.3800500e-01, -2.5524400e-01],
       [ 1.2829716e+01,  4.0000000e+01,  5.1000000e+01,  5.3000000e+01,
         1.0210170e+00,  2.4247860e+00,  2.6801600e+00],
       [ 1.3578420e+01,  1.3000000e+01,  1.1000000e+01,  5.3000000e+01,
        -2.4248880e+00, -2.6798660e+00,  2.6801600e+00],
       [ 1.3636475e+01,  1.8000000e+01,  1.2000000e+01,  1.0000000e+01,
        -1.7867570e+00, -2.5522500e+00, -2.8077690e+00],
       [ 1.4200110e+01,  3.8000000e+01,  1.3000000e+01,  1.0000000e+01,
         7.6576500e-01, -2.4246340e+00, -2.8077690e+00],
       [ 1.4583503e+01,  2.0000000e+01,  1.1000000e+01,  5.3000000e+01,
        -1.5315050e+00, -2.6798660e+00,  2.6801600e+00],
       [ 1.4664506e+01,  3.9000000e+01,  1.2000000e+01,  5.3000000e+01,
         8.9339100e-01, -2.5522500e+00,  2.6801600e+00],
       [ 1.4688313e+01,  4.0000000e+01,  5.1000000e+01,  1.0000000e+01,
         1.0210170e+00,  2.4247860e+00, -2.8077690e+00],
       [ 1.5622219e+01,  4.0000000e+01,  5.2000000e+01,  3.2000000e+01,
         1.0210170e+00,  2.5524030e+00,  9.0000000e-06],
       [ 1.5938178e+01,  4.0000000e+01,  5.2000000e+01,  3.1000000e+01,
         1.0210170e+00,  2.5524030e+00, -1.2761800e-01],
       [ 2.3088539e+01,  1.2000000e+01,  2.5000000e+01,  3.1000000e+01,
        -2.5525140e+00, -8.9323800e-01, -1.2761800e-01],
       [ 3.3959612e+01,  1.2000000e+01,  9.0000000e+00,  2.9000000e+01,
        -2.5525140e+00, -2.9350990e+00, -3.8287000e-01],
       [ 3.4657294e+01,  2.0000000e+01,  9.0000000e+00,  2.9000000e+01,
        -1.5315050e+00, -2.9350990e+00, -3.8287000e-01],
       [ 3.6118429e+01,  5.4000000e+01,  5.1000000e+01,  9.0000000e+00,
         2.8077830e+00,  2.4247860e+00, -2.9353960e+00],
       [ 3.6199325e+01,  3.9000000e+01,  1.0000000e+01,  3.0000000e+01,
         8.9339100e-01, -2.8074830e+00, -2.5524400e-01],
       [ 3.7618172e+01,  5.4000000e+01,  5.2000000e+01,  5.3000000e+01,
         2.8077830e+00,  2.5524030e+00,  2.6801600e+00],
       [ 3.9779488e+01,  3.8000000e+01,  1.6000000e+01,  3.2000000e+01,
         7.6576500e-01, -2.0417850e+00,  9.0000000e-06],
       [ 4.1706793e+01,  5.4000000e+01,  2.8000000e+01,  5.4000000e+01,
         2.8077830e+00, -5.1038900e-01,  2.8077870e+00],
       [ 4.2790045e+01,  5.4000000e+01,  2.6000000e+01,  9.0000000e+00,
         2.8077830e+00, -7.6562100e-01, -2.9353960e+00],
       [ 4.3479828e+01,  5.4000000e+01,  5.2000000e+01,  3.1000000e+01,
         2.8077830e+00,  2.5524030e+00, -1.2761800e-01],
       [ 4.9584441e+01,  5.4000000e+01,  1.0000000e+01,  9.0000000e+00,
         2.8077830e+00, -2.8074830e+00, -2.9353960e+00],
       [ 5.1788568e+01,  5.5000000e+01,  1.0000000e+01,  5.4000000e+01,
         2.9354090e+00, -2.8074830e+00,  2.8077870e+00],
       [ 5.5592533e+01,  5.5000000e+01,  2.5000000e+01,  3.2000000e+01,
         2.9354090e+00, -8.9323800e-01,  9.0000000e-06],
       [ 5.5745591e+01,  5.5000000e+01,  2.5000000e+01,  3.1000000e+01,
         2.9354090e+00, -8.9323800e-01, -1.2761800e-01],
       [ 6.1714603e+01,  5.5000000e+01,  7.0000000e+00,  2.9000000e+01,
         2.9354090e+00, -3.1903310e+00, -3.8287000e-01],
       [ 6.1827058e+01,  5.6000000e+01,  7.0000000e+00,  2.5000000e+01,
         3.0630350e+00, -3.1903310e+00, -8.9337500e-01]])
    #load hills
    h3 = mm.Hills(name="./data/acealanme3d", periodic=[False,False,False])
    #find minima on FES
    minima = mm.Minima(mm.Fes(h3, resolution=64, original=False))
    minima = minima.minima.to_numpy()
    minima = minima[:,1:].astype(float)
    assert(np.allclose(minima, expected, 1e-4))

if __name__ == '__main__':
    pytest.main([__file__])

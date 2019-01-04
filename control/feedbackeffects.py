#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# This script visualizes the effects of a feedback loop on the poles and zeros 
# of a 2nd order system                                                    
# -----------------------------------------------------------------------------

import numpy as np
from matplotlib import pyplot as plt
import control
    
randcomp = lambda: np.random.rand()+1j*np.random.rand()
N = 100
Kp = 2

# Generate a random plant
cs = [np.random.rand() for i in range(2)]#range(np.random.randint(2, 4))]
bs = [np.random.rand() for i in range(3)]#range(np.random.randint(2, 4))]
p = control.tf(cs, bs)

plt.figure(figsize=(8,6))
plt.title("Effects of P control")
kps = np.linspace(-10, 10, 100)
for n in range(N):
    # Generate a random plant
    cs = [np.random.rand() for i in range(2)]#range(np.random.randint(2, 4))]
    bs = [np.random.rand() for i in range(3)]#range(np.random.randint(2, 4))]
    p = control.tf(cs, bs)
    
    # Sweep Kp values
    rs = []
    cs = []
    for kp in kps:
        # Creat a P controller
        c = control.tf([kp], [1])
        # Get the closed-loop transfer functions
        tf = control.feedback(p, c, 1)
        zs = tf.zero()
        ps = tf.pole()
        
        # Plot the transfer function poles
        # upper plane only
        for pole in ps:
            if pole.imag >=0:
                rs.append(pole.real)
                cs.append(pole.imag)
    plt.plot(rs,cs,'b-')
            
    
    # Plot the plant's zero
    zs = p.zero()
    for zero in zs:
        plt.plot([zero.real],[zero.imag],'ro')
    # Plot the plant's poles
    ps = p.pole()
    for pole in ps:
        plt.plot([pole.real],[pole.imag],'rx')
plt.xlim((-3,3))
plt.ylim((-3,3))
plt.show()


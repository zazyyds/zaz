import torch
import numpy as np
import ot
FILE_A ="gluon_latent_vectors.pt"
FILE_B ="gluon_latent_vectors.pt"

def turn_numpy(x):
    return x.detach().cpu().numpy()

A = torch.load(FILE_A)[:500]
B = torch.load(FILE_B)[500:]
XA = turn_numpy(A).astype(np.float64)
XB = turn_numpy(B).astype(np.float64)
p = ot.unif(XA.shape[0])
q = ot.unif(XB.shape[0])
C1 = ot.dist(XA, XA,metric="euclidean")
C2 = ot.dist(XB, XB,metric="euclidean")

gw2 = ot.gromov.gromov_wasserstein2(C1, C2, p, q)
print("GW^2 distance =", gw2)
print("GW distance =", np.sqrt(gw2))